; Write a function which returns the first X fibonacci numbers.
;
(= (#(take % (map last (iterate (fn [[a b]] [b (+ a b)]) [0 1]))) 3) '(1 1 2))
(= (#(take % (map last (iterate (fn [[a b]] [b (+ a b)]) [0 1]))) 6) '(1 1 2 3 5 8))
(= (#(take % (map last (iterate (fn [[a b]] [b (+ a b)]) [0 1]))) 8) '(1 1 2 3 5 8 13 21))
