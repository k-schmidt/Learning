; Write a function which returns the Nth element from a sequence.
;
(= (#(first (drop %2 %1)) [:a :b :c] 0) :a)  
(= (#(first (drop %2 %1)) [1 2 3 4] 1) 2)
(= (#(first (drop %2 %1)) '([1 2] [3 4] [5 6]) 2) [5 6])
