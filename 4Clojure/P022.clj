; Write a function which returns the total number of elements in a sequence.
;
#(reduce (fn [x y] (inc x)) 0 %)
