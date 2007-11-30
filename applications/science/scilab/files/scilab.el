;; scilab-mode.el - major mode for editing Scilab source with GNU Emacs
;;
;; This major mode for GNU Emacs provides support for editing Scilab
;; source files.  It automatically indents for block structures, line
;; continuations (e.g., ...), and comments.  The usual paren matching
;; support is included.  
;; For convient use add something like the
;; following to your .emacs start-up file:
;;
;; (global-font-lock-mode t)
;; (load "scilab")
;; (setq auto-mode-alist (cons '("\\(\\.sci$\\|\\.sce$\\)" . scilab-mode) auto-mode-alist))
;; (setq scilab-mode-hook '(lambda () (setq fill-column 74)))
;;
;;
;; Enjoy.
;;
;; Last modified Tue Oct 28 12:05:36 MET 1997
;;
;; This file was modified by Serge Steer (Serge.Steer@inria.fr ) from
;; the file octave-mode.el (Copyright (C) 1991 Matthew R. Wette.), 
;; fortran-mode.el Copyright (c) Free Software Foundation, Inc. (string handling)
;; tex-mode.el Copyright (C) Free Software Foundation, Inc. (compilation part) 
;; 
;; This file is modifed by Rainer Menzner (Rainer.Menzner@neuroinformatik.ruhr-uni-bochum.de)
;; to add font-lock support to Scilab-mode instead of hilit19.
;;
;; Everyone is granted permission to copy, modify and redistribute this
;; file provided:
;;   1. All copies contain this copyright notice.
;;   2. All modified copies shall carry a prominant notice stating who
;;      made the last modification and the date of such modification.
;;   3. No charge is made for this software or works derived from it.
;;      This clause shall not be construed as constraining other software
;;      distributed on the same medium as this software, nor is a
;;      distribution fee considered a charge.
;;

(require 'shell)
(require 'compile)
 
;; Constants used in all Scilab-mode buffers.
(defconst scilab-indent-level 2
  "*The indentation in Scilab-mode.")

(defconst scilab-comment-column 40
  "*The goal comment column in Scilab-mode buffers.")

(defconst sci-block-beg-kw "\\(for[ \t]\\|while[ \t]\\|if[ \t]\\|else[ \t,;\n]*\\|elseif[ \t]\\|select[ \t]\\|case[ \t]\\)"
  "Regular expression for keywords which begin blocks in Scilab-mode.")

(defconst sci-block-end-kw "\\(end[ \t,;\n]*\\|else[ \t,;\n]*\\|elseif[ \t]\\|case[ \t]\\)"
  "Regular expression for keywords which end blocks.")

;; variables for compilation part
(defvar sci-last-indent-type "unknown"
  "String to tell line type.")

(defvar scilab-comment-region "//"
  "*String inserted by \\[scilab-comment-region]\
 at start of each line in region.")

;;;###autoload
(defvar scilab-command "scilab"
  "Command to run Scilab. scilab must be in the path.
The option and the name of the file, will be added to this string.")

;;;###autoload
(defvar scilab-last-buffer-compiled nil
  "Buffer which was last compiled.")
;;;###autoload
(defvar scilab-zap-file nil
  "Temporary file name used for text being sent as input to Scilab.
Should be a simple file name with no extension or directory specification."
)
;;;###autoload
(defvar scilab-directory "."
  "*Directory in which temporary files are left.
You can make this /tmp if your functions has no relative directories in it.")

;;;###autoload
(defvar scilab-offer-save t
  "*If non-nil, ask about saving modified buffers before \\[scilab-file] is run.")
;;;###autoload
(defvar scilab-last-temp-file nil
  "Latest temporary file generated by \\[scilab-region] and \\[scilab-compile-buffer].
Deleted when the \\[scilab-region] or \\[scilab-compile-buffer] is next run, or when the
scilab-shell goes away.")

;;;###autoload
(defvar scilab-trailer nil
  "String appended after the end of a region sent to scilab by \\[scilab-region].")

(defvar scilab-shell-file-name nil
  "*If non-nil, the shell file name to run in the subshell used to run Scilab.")

;; Syntax Table
(defvar scilab-mode-syntax-table nil
  "Syntax table used in Scilab-mode buffers.")


(if scilab-mode-syntax-table
    ()
  (setq scilab-mode-syntax-table (make-syntax-table))
  (modify-syntax-entry ?\\ "." scilab-mode-syntax-table)
  (modify-syntax-entry ?/ "." scilab-mode-syntax-table)
  (modify-syntax-entry ?* "." scilab-mode-syntax-table)
  (modify-syntax-entry ?+ "." scilab-mode-syntax-table)
  (modify-syntax-entry ?- "." scilab-mode-syntax-table)
  (modify-syntax-entry ?= "." scilab-mode-syntax-table)
  (modify-syntax-entry ?< "." scilab-mode-syntax-table)
  (modify-syntax-entry ?> "." scilab-mode-syntax-table)
  (modify-syntax-entry ?\[ "(]" scilab-mode-syntax-table)
  (modify-syntax-entry ?\] ")[" scilab-mode-syntax-table)
  (modify-syntax-entry ?& "." scilab-mode-syntax-table)
  (modify-syntax-entry ?| "." scilab-mode-syntax-table)
  (modify-syntax-entry ?\' "'" scilab-mode-syntax-table)
  (modify-syntax-entry ?\n ">" scilab-mode-syntax-table)
  (set-syntax-table scilab-mode-syntax-table))


;; Abbrev Table
(defvar scilab-mode-abbrev-table nil
  "Abbrev table used in Scilab-mode buffers.")

(define-abbrev-table 'scilab-mode-abbrev-table ())


;; Mode Map
;(defvar scilab-mode-map nil "Keymap for Scilab mode.")
(defvar scilab-mode-map ()   "Keymap used in scilab-mode.")

(if scilab-mode-map
    nil
  (setq scilab-mode-map (make-sparse-keymap))
  (define-key scilab-mode-map "\r" 'scilab-return)
  (define-key scilab-mode-map "\t" 'scilab-indent-line)
  (define-key scilab-mode-map "\M-;" 'scilab-comment)
  (define-key scilab-mode-map "\C-ct" 'scilab-line-type)
  (define-key scilab-mode-map "\C-ci" 'scilab-indent-type)
  (define-key scilab-mode-map "\C-c\C-p" 'beginning-of-scilab-function)
  (define-key scilab-mode-map "\C-c\C-n" 'end-of-scilab-function)
  (define-key scilab-mode-map "\M-\r" 'newline))
  
(defvar menu-bar-scilab-menu (make-sparse-keymap "Scilab"))
(define-key scilab-mode-map [menu-bar scilab] (cons "Scilab" menu-bar-scilab-menu))
;(define-key menu-bar-scilab-menu [C2]
;  '("Check Buffer Syntax" . scilab-compile-buffer))
;(define-key menu-bar-scilab-menu [C3]
;  '("Check Function Syntax" . scilab-compile-function))
(define-key menu-bar-scilab-menu [C4]
  '("Indent Function" . scilab-indent-function))
(define-key menu-bar-scilab-menu [C5]
  '("Indent Buffer" . scilab-indent-buffer))
(define-key menu-bar-scilab-menu [C6]
  '("Ident Region" . scilab-indent-region))
(define-key menu-bar-scilab-menu [end-of-scilab-function]
  '("End of function C-cC-n" . end-of-scilab-function))
(define-key menu-bar-scilab-menu [beginning-of-scilab-function]
  '("Beginning of function C-cC-p" . beginning-of-scilab-function))



  (define-key scilab-mode-map [menu-bar scilab scilab-compile] 
    '(cons "Scilab Compile" scilab-compile))
 (define-key scilab-mode-map [menu-bar scilab scilab-compile-buffer] 
    '(cons "Scilab Compile Buffer" scilab-compile-buffer))
  (define-key scilab-mode-map [menu-bar scilab scilab-compile-function] 
    '(cons "Scilab Compile Function" scilab-compile-function))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Scilab font-lock support (RMz, 10/28/1997)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;
;; emacs-20:  keyword builtin warning variable-name type string reference function-name comment
;; emacs-19:  comment string keyword function-name variable-name type reference
(defvar scilab-font-lock-keywords
  '(
    ("//.*$" . font-lock-comment-face)
    ("['\"][^'\n]*['\"]" . font-lock-string-face)
    ("[ ,;\t]\\(do\\|if\\|elseif\\|then\\|else\\|for\\|end\\|while\\|select\\|case\\|break\\)[ \t\n]" . font-lock-keyword-face)
    ("^\\(do\\|if\\|elseif\\|then\\|else\\|for\\|end\\|while\\|select\\|case\\|break\\)[ ,;\t\n]" . font-lock-keyword-face)
    ("[ ,;\t]\\(resume\\|return\\|pause\\|quit\\|abort\\|^//end\\)[ ,;\t\n]" . font-lock-type-face)
    ("^ *\\(endfunction\\|function\\)[ \t\n]" . font-lock-function-name-face)
    ("[^ ,;\t]\\case\\[ \t\n]" . label)
    )
  "Default expressions to highlight in Scilab mode."
  )



;; Scilab Mode
(defun scilab-mode ()
  "Major mode for editing Scilab source files.  Version 1.0, may 1997.
Will run scilab-mode-hook if it is non-nil.  Auto-fill-mode seems to work.
Filling does not work (yet).
Special Key Bindings:
\\{scilab-mode-map}
Variables:
  scilab-indent-level                   Level to indent blocks.
  scilab-comment-column                 Goal column for on-line comments.
  fill-column                           Column used in auto-fill (default=70).
Commands:
  scilab-mode                           Enter Scilab major mode.
  scilab-return                         Handle return with indenting.
  scilab-indent-line                    Indent line for structure.
  scilab-indent-buffer                  Indent buffer for structure.
  scilab-indent-function	        Indent function for structure.  
  scilab-comment                        Add comment to current line.
  scilab-comment-indent                 Compute indent for comment.
  scilab-comment-region                 To comment a region
  scilab-line-type                      Tell current line type (for debugging).
  scilab-indent-type                    Tell last indent type (for debugging).
  scilab-compile-buffer		        Compile all scilab functions in buffer
  scilab-compile-function               Compile scilab function

To add automatic support put something like the following in your .emacs file:
  \(autoload 'scilab-mode \"scilab-mode\" \"Enter Scilab-mode.\" t\)
  \(setq auto-mode-alist \(cons '\(\"\\\\.sci$\" . scilab-mode\) \
auto-mode-alist\)\)
  \(setq scilab-mode-hook '\(lambda \(\) \(setq fill-column 74\)\)\)"
  (interactive)
  (kill-all-local-variables)
  (use-local-map scilab-mode-map)
  (setq major-mode 'scilab-mode)
  (setq mode-name "Scilab")
  (setq local-abbrev-table scilab-mode-abbrev-table)
  (set-syntax-table scilab-mode-syntax-table)
  (make-local-variable 'paragraph-start)
  (setq paragraph-start (concat "^$\\|" page-delimiter))
  (make-local-variable 'paragraph-separate)
  (setq paragraph-separate paragraph-start)
  (make-local-variable 'paragraph-ignore-fill-prefix)
  (setq paragraph-ignore-fill-prefix t)
  (make-local-variable 'indent-line-function)
  (setq indent-line-function 'scilab-indent-line)
  (make-local-variable 'comment-start-skip)
  (setq comment-start-skip "//")
  (make-local-variable 'comment-column)
  (setq comment-column 'scilab-comment-column)
  (make-local-variable 'comment-indent-hook)
  (setq comment-indent-hook 'scilab-comment-indent)
  (make-local-variable 'fill-column)
  (setq fill-column default-fill-column)
  (make-local-variable 'indent-tabs-mode)
  (setq indent-tabs-mode t)
  (run-hooks 'scilab-mode-hook)
  ;; The follwoing two entries are set by RMz for font-lock support:
  (make-local-variable 'font-lock-defaults)
  (setq font-lock-defaults '(scilab-font-lock-keywords nil t))
  )

(defun scilab-return ()
  "Handle carriage return in Scilab-mode."
  (interactive)
  (if (sci-block-end-line)
      (scilab-indent-line))
  (newline)
  (scilab-indent-line))

(defun scilab-comment ()
  "Add a comment to the following line, or format if one already exists."
  (interactive)
  (cond
   ((sci-empty-line)
    (scilab-indent-line)
    (insert "// "))
   ((sci-comment-line))
   (t
    (end-of-line)
    (re-search-backward "[^ \t^]" 0 t)
    (forward-char)
    (delete-horizontal-space)
    (if (< (current-column) scilab-comment-column)
        (indent-to scilab-comment-column)
      (insert " "))
    (insert "// "))))

(defun scilab-comment-indent ()
  "Indent a comment line in Scilab-mode."
  (sci-calc-indent))

(defun scilab-indent-line ()
  "Indent a line in Scilab-mode."
  (interactive)
  (save-excursion
    (beginning-of-line)
    (delete-horizontal-space)
    (indent-to  (sci-calc-indent)))
  (skip-chars-forward "[ \t]"))

(defun scilab-line-type ()
  "Display type of current line.  Used in debugging."
  (interactive)
  (cond
   ((sci-empty-line)
    (message "scilab-line-type: empty-line"))
   ((sci-comment-line)
    (message "scilab-line-type: comment-line"))
   ((sci-continuation-line)
    (message "scilab-line-type: continuation-line"))
   ((sci-block-beg-end-line)
    (message "scilab-line-type: block-beg-end-line"))
   ((sci-block-beg-line)
    (message "scilab-line-type: block-beg-line"))
   ((sci-block-end-line)
    (message "scilab-line-type: block-end-line"))
   (t
    (message "scilab-line-type: other"))))

(defun scilab-indent-type ()
  "Display type of current or previous nonempty line.  Used in debugging."
  (interactive)
  (message (concat "scilab-ident-type: " sci-last-indent-type)))

(defun scilab-fill-region (from to &optional justify-flag)
  "Fill the region of comments.
Prefix arg (non-nil third arg, if called from program)
means justify as well."
  (interactive)
  (message "scilab-fill-region not implemented yet."))


(defun sci-calc-indent ()
  "Return the appropriate indentation for this line as an int."
  (interactive)
  (let ((indent 0))
    (save-excursion
      (forward-line -1)                 ; compute indent based on previous
      (if (sci-empty-line)               ;   non-empty line
          (re-search-backward "[^ \t\n]" 0 t))
      (cond
       ((sci-empty-line) 
        (setq sci-last-indent-type "empty"))
       ((sci-comment-line) 
        (setq sci-last-indent-type "comment"))
       ((sci-unbal-matexp-line)
        (setq sci-last-indent-type "unbalanced-matrix-expression")
        (setq indent (sci-calc-matexp-indent))
	(if (sci-continuation-line)
	    (progn (setq sci-last-indent-type "continuation")
		   (setq indent  (+ indent (* 2 scilab-indent-level))))))
       ((sci-continuation-line)
        (setq sci-last-indent-type "continuation")
        (setq indent (* 2 scilab-indent-level))
	(message "sci-continuation-line"))
       ((sci-block-beg-end-line)
	(message "sci-block-beg-end-line")
        (setq sci-last-indent-type "block begin-end"))
       ((sci-block-beg-line)
	(message "sci-block-beg-line")
        (setq sci-last-indent-type "block begin")
	(setq indent scilab-indent-level))
       (t
        (setq sci-last-indent-type "other")))
      (setq indent (+ indent (current-indentation)))
      (if (= 0 (forward-line -1))
          (if (sci-continuation-line)
              (setq indent (- indent (* 2 scilab-indent-level))))))
    (if (and (sci-block-end-line) (not (sci-block-beg-end-line)))
	(setq indent (- indent scilab-indent-level)))
    (if (< indent 0) (setq indent 0))
    indent))


(defun sci-empty-line ()
  "Returns t if current line is empty."
  (save-excursion
    (beginning-of-line)
    (looking-at "^[ \t]*$")))

(defun sci-comment-line ()
  "Returns t if current line is an Scilab comment line."
  (save-excursion
    (beginning-of-line)
    (skip-chars-forward " \t")
    (looking-at "//")))

(defun sci-continuation-line ()
  "Returns t if current line ends in ... and optional comment."
  (save-excursion
    (beginning-of-line)
    (re-search-forward "\\.\\.+[ \t]*\\(//.*\\)?$" (sci-eoln-point) t)))

(defun sci-eoln-point ()
  "Returns point for end-of-line in Scilab-mode."
  (save-excursion
    (end-of-line)
    (point)))

(defun sci-bol-point()
  "Returns point for beginnind-of-line in Scilab-mode."
  (save-excursion
    (beginning-of-line)
    (point)))


(defun sci-block-beg-line ()
  "Returns t if line contains beginning of Scilab block."
  (save-excursion
    (beginning-of-line)
    (and (re-search-forward 
	  (concat "\\([ ,;\t]\\)?" sci-block-beg-kw) (sci-eoln-point) t )
	 (not (scilab-is-in-string))
	 (not (scilab-is-in-comment))
	 )
))


(defun sci-block-end-line ()
  "Returns t if line contains end of Scilab block."
  (save-excursion
    (beginning-of-line)
    (and (re-search-forward  
	  (concat "\\([ \t]*\\)" sci-block-end-kw) (sci-eoln-point) t )
	 (not (scilab-is-in-string))
	 (not (scilab-is-in-comment)))
))


(defun sci-block-beg-end-line ()
  "Returns t if line contains matching block begin-end in Scilab-mode."
  (save-excursion
    (beginning-of-line)
    (and (re-search-forward  
	  (concat
                 "\\([ ,;\t]\\)?" sci-block-beg-kw 
                 ".*" "\\([ ,;\t]\\)?" sci-block-end-kw)(sci-eoln-point) t )
	 (not (scilab-is-in-string))
	 (not (scilab-is-in-comment))
	 )
    ))
(defun sci-unbal-matexp-line ()
  (if (= (sci-calc-matexp-indent) 0)
    ()
    t))

(defun sci-calc-matexp-indent ()
  (let ((indent 0))
    (save-excursion
      (beginning-of-line)
      (while (< (point) (sci-eoln-point))
	(cond
	 ((looking-at "\\[")
	  (setq indent (+ indent scilab-indent-level)))
	 ((looking-at "\\]")
	  (setq indent (- indent scilab-indent-level))))
	(forward-char)))
    (* 2 indent)))

(defun sci-comment-on-line ()
  "Returns t if current line contains a comment."
  (save-excursion
    (beginning-of-line)
    (looking-at "[^\n]*//")))

(defun sci-in-comment ()
  "Returns t if point is in a comment."
  (save-excursion
    (and (/= (point) (point-max)) (forward-char))
    (search-backward "//" (save-excursion (beginning-of-line) (point)) t)))


(defun scilab-comment-region (beg-region end-region arg)
  "Comments every line in the region.
Puts scilab-comment-region at the beginning of every line in the region. 
BEG-REGION and END-REGION are args which specify the region boundaries. 
With non-nil ARG, uncomments the region."
  (interactive "*r\nP")
  (let ((end-region-mark (make-marker)) (save-point (point-marker)))
    (set-marker end-region-mark end-region)
    (goto-char beg-region)
    (beginning-of-line)
    (if (not arg)			;comment the region
	(progn (insert scilab-comment-region)
	       (while (and  (= (forward-line 1) 0)
			    (< (point) end-region-mark))
		 (insert scilab-comment-region)))
      (let ((com (regexp-quote scilab-comment-region))) ;uncomment the region
	(if (looking-at com)
	    (delete-region (point) (match-end 0)))
	(while (and  (= (forward-line 1) 0)
		     (< (point) end-region-mark))
	  (if (looking-at com)
	      (delete-region (point) (match-end 0))))))
    (goto-char save-point)
    (set-marker end-region-mark nil)
    (set-marker save-point nil)))

(defun beginning-of-scilab-function ()
  "Moves point to the beginning of the current Scilab function."
  (interactive)
  (let ((case-fold-search t))
    (beginning-of-line -1)
    (re-search-backward "^[ \t]*function" nil 'move)))

(defun end-of-scilab-function ()
  "Moves point to the end of the current Scilab subprogram."
  (interactive)
  (let ((case-fold-search t))
    (beginning-of-line 2)
    (re-search-forward "^[ \t]*function" nil 'move)
    (if (eobp)
      (end-of-buffer)
    (goto-char (match-beginning 0))
    (forward-line -1))))


(defun mark-scilab-function ()
  "Put mark at end of Scilab function, point at beginning. 
The marks are pushed."
  (interactive)
  (push-mark (point) nil t)
  (end-of-scilab-function)
  (push-mark (point) nil t)
  (beginning-of-scilab-function))

(defun scilab-indent-function ()
  "Properly indents the Scilab function  which contains point."
  (interactive)
  (save-excursion
    (mark-scilab-function)
    (message "Indenting function...")
    (indent-region (point) (mark) nil))
  (message "Indenting function...done."))

(defun scilab-indent-region ()
  "Properly indents a Scilab region."
  (interactive)
  (save-excursion
    (message "Indenting region...")
    (indent-region (mark) (point) nil))
  (message "Indenting region...done."))

(defun scilab-indent-buffer ()
  "Properly indents a Scilab buffer."
  (interactive)
  (save-excursion
    (message "Indenting buffer...")
    (indent-region (point-min) (point-max) nil))
  (message "Indenting buffer...done."))

(defun scilab-is-in-comment()
 "Return non-nil if POS (a buffer position) is inside a Scilab comment,
nil else."
 (interactive)
  (save-excursion
    (re-search-backward  "//" (sci-bol-point) t)))

(defun scilab-is-in-string()
  "Return non-nil if POS (a buffer position) is inside a Scilab string,
nil else."
 (interactive)
  (save-excursion
    (setq where (point))
    (goto-char where)
    (cond
     ((bolp) nil)			; bol is never inside a string
     ((save-excursion			; comment lines too
	(beginning-of-line)(looking-at "//")) nil)
     (t (let (;; ok, serious now. Init some local vars:
	      (parse-state '(0 nil nil nil nil nil 0))
	      (not-done t)
	      parse-limit
	      end-of-line
	      )
	  ;; move to start of current statement
	  (beginning-of-line)
	  ;; now parse up to WHERE
	  (while not-done
	    (if (or ;; skip to next line if:
		 ;; - comment line?
		 ;;(looking-at comment-line-start-skip)
		 ;; - at end of line?
		 (eolp)
		 ;; - not in a string and after comment-start?
		 ;;(and (not (nth 3 parse-state))
		 ;;     comment-start
		 ;;     (equal comment-start
		 ;;     (char-to-string (preceding-char))))
		 )
		;; get around a bug in forward-line in versions <= 18.57
		(if (or (> (forward-line 1) 0) (eobp))
		    (setq not-done nil))
	      ;; else:
	      
	      ;; find out parse-limit from here
	      (setq end-of-line (save-excursion (end-of-line)(point)))
	      (setq parse-limit (min where end-of-line))
	      ;; parse max up to comment-start, if non-nil and in current line
	      ;;(if comment-start
	      ;;  (save-excursion
	      ;;    (if (re-search-forward quoted-comment-start end-of-line t)
	      ;;	(setq parse-limit (min (point) parse-limit)))))
	      ;; now parse if still in limits
	      (if (< (point) where)
		  (setq parse-state (parse-partial-sexp
				     (point) parse-limit nil nil parse-state))
		(setq not-done nil))
	      ))
	  ;; result is
	  (if (nth 3 parse-state) 
	      t
	    ()
	    )
	  )))))

;; La suite concerne la compilation des functions
;;--------------------------------------------

(defun scilab-region (beg end)
  "Run Scilab on the current region, via a temporary file.
The file's name comes from the variable `scilab-zap-file' and the
variable `scilab-directory' says where to put it.

If the buffer has a header, the header is given to Scilab before the
region itself.  The buffer's header is all lines between the strings
defined by `scilab-start-of-header' and `scilab-end-of-header' inclusive.
The header must start in the first 100 lines of the buffer.

The value of `scilab-trailer' is given to Scilab as input after the region.

The value of `scilab-command' specifies the command to use to run Scilab."
  (interactive "r")
  (if (scilab-shell-running)
      (scilab-kill-job)
    (scilab-start-shell))
  (display-buffer (process-buffer (get-process "scilab-shell")))
  (or 
      (setq scilab-zap-file (scilab-generate-zap-file-name)))

  (let* ((temp-buffer (get-buffer-create " Scilab-Output-Buffer"))
         ; Temp file will be written and Scilab will be run in zap-directory.
         ; If the TEXINPUTS file has relative directories or if the region has
         ; \input of files, this must be the same directory as the file for
         ; Scilab to access the correct inputs.  That's why it's safest if
         ; scilab-directory is ".".
         (zap-directory
          (file-name-as-directory (expand-file-name scilab-directory)))
         (scilab-out-file (concat zap-directory scilab-zap-file)))

    (scilab-delete-last-temp-files)
    ;; Write the new temp file.
    (save-excursion
      (save-restriction
	(widen)
	(goto-char (point-min))
	(forward-line 100)
	(let ((search-end (point))
	      (hbeg (point-min)) (hend (point-min))
	      (default-directory zap-directory))
	  (goto-char (point-min))
	  ;; Initialize the temp file with either the header or nothing
	  (if (search-forward "^[ \t]*function" search-end t)
	      (progn
		(beginning-of-line)
		(setq hbeg (point))	;mark beginning of header
		(if (search-forward "[)\n]" nil t)
		    (progn (forward-line 1)
			   (setq hend (point)))	;mark end of header
		  (setq hbeg (point-min))))) ;no header
	  (write-region (min hbeg beg) hend
                        (concat scilab-out-file ".sci") nil nil)
	  (write-region (max beg hend) end (concat scilab-out-file ".sci") t nil))

	(let ((local-scilab-trailer scilab-trailer))
	  (set-buffer temp-buffer)
	  (erase-buffer)
	  ;; make sure trailer isn't hidden by a comment
	  (insert-string "\n")
	  (if local-scilab-trailer (insert-string local-scilab-trailer))
	  (scilab-set-buffer-directory temp-buffer zap-directory)
	  (write-region (point-min) (point-max)
                        (concat scilab-out-file ".sci") t nil))))


    ;; Record the file name to be deleted afterwards.
    (setq scilab-last-temp-file scilab-out-file)
    (compile-internal (concat scilab-command " -comp " scilab-out-file)
		      "No more errors" "scilab-compil"
		      nil nil nil)
    (setq scilab-last-buffer-compiled (current-buffer))))

(defun scilab-compile-buffer ()
  "Run Scilab on current buffer.  See \\[scilab-region] for more information.
Does not save the buffer, so it's useful for trying experimental versions.
See \\[scilab-file] for an alternative."
  (interactive)
  (scilab-region (point-min) (point-max)))

(defun scilab-compile-function ()
  "Run Scilab on current buffer.  See \\[scilab-region] for more information.
Does not save the buffer, so it's useful for trying experimental versions.
See \\[scilab-file] for an alternative."
  (interactive)
  (mark-scilab-function)
  (scilab-region (point) (mark)))


(defun scilab-start-shell ()
  (save-excursion
    (set-buffer
     (make-comint
      "scilab-shell"
      (or scilab-shell-file-name (getenv "ESHELL") (getenv "SHELL") "/bin/sh")
      nil))
    (let ((proc (get-process "scilab-shell")))
      (set-process-sentinel proc 'scilab-shell-sentinel)
      (process-kill-without-query proc)
      (setq scilab-shell-map (copy-keymap shell-mode-map))
      ;;(scilab-define-common-keys scilab-shell-map)
      (use-local-map scilab-shell-map)
      (run-hooks 'scilab-shell-hook)
      (while (zerop (buffer-size))
          (sleep-for 1)))))
(defun scilab-shell-running ()
  (and (get-process "scilab-shell")
       (eq (process-status (get-process "scilab-shell")) 'run)))

(defun scilab-kill-job ()
  "Kill the currently running TeX job."
  (interactive)
  (quit-process (get-process "scilab-shell") t))

(defun scilab-delete-last-temp-files ()
  "Delete any junk files from last temp file."
  (if scilab-last-temp-file
      (let* ((dir (file-name-directory scilab-last-temp-file))
             (list (file-name-all-completions
                    (file-name-nondirectory scilab-last-temp-file) dir)))
        (while list
          (delete-file (concat dir (car list)))
          (setq list (cdr list))))))

(add-hook 'kill-emacs-hook 'scilab-delete-last-temp-files)
(defun scilab-generate-zap-file-name ()
  "Generate a unique name suitable for use as a file name."
  ;; Include the shell process number and host name
  ;; in case there are multiple shells (for same or different user).
  (format "#tz%-d%s"
          (process-id (get-buffer-process "*scilab-shell*"))
	  (scilab-strip-dots (system-name))))

(defun scilab-strip-dots (s)
  (setq s (copy-sequence s))
  (while (string-match "\\." s)
    (aset s (match-beginning 0) ?-))
  s)


(defun scilab-set-buffer-directory (buffer directory)
  "Set BUFFER's default directory to be DIRECTORY."
  (setq directory (file-name-as-directory (expand-file-name directory)))
  (if (not (file-directory-p directory))
      (error "%s is not a directory" directory)
    (save-excursion
      (set-buffer buffer)
      (setq default-directory directory))))


;;Fin de la partie dediee a la compilation des functions
;;---------------------------------------------------
(provide 'scilab-mode)

;; --- last line of scilab-mode.el --- 
