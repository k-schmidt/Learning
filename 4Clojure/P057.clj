;; Simple Recursion
;; A recursive function is a function that calls itself.
(= '(5 4 3 2 1)
   ((fn foo [x]
      (when (> x 0)
        (conj (foo (dec x)) x))) 5))
