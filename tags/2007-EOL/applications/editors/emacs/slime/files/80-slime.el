;;; slime site-lisp configuration

(add-to-list 'load-path "/usr/share/emacs/site-lisp/sbcl/")  ; your SLIME directory
(setq inferior-lisp-program "/usr/bin/sbcl") ; your Lisp system
(require 'slime)
(slime-setup)
