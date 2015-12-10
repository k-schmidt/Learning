;; Factorial Fun
;; Write a function which calculates factorials.

(= (__ 1) 1)
(= (__ 3) 6)
(= (__ 5) 120)
(= (__ 8) 40320)

(fn [n]
  (loop [x n
         f 1]
    (if (= x 1)
      f
      (recur (dec x) (* f x)))))
