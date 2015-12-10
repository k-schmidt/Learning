;; Greatest Common Divisor
;; Given two integers, write a function which returns the greatest common divisor.

(= (__ 2 4) 2)
(= (__ 10 5) 5)
(= (__ 5 7) 1)
(= (__ 1023 858) 33)

(fn [x y]
  (loop [int1 x
         int2 y]
    (if (zero? int2) int1
        (recur int2 (mod int1 int2)))))
