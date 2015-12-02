;; Recurring Theme
;; Clojure only has one non-stack-consuming looping construct: recur.
;; Either a function or a loop can be used as the recursion point.
;; Either way, recur rebinds the bindings of the recursion point to the
;; values it is passed. Recur must be called from the tail-position,
;; and calling it elsewhere will result in an error.

;; A tail-position is the place in an expression that would return a value.
;; There are no more forms evaluated after the tail-position.
(= '(7 6 5 4 3)
   (loop [x 5
          result []]
     (if (> x 0)
       (recur (dec x) (conj result (+ x 2)))
       result)))
