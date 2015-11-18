; Write a function that retrieves the second to last element.
;
(= (#(second (reverse %)) (list 1 2 3 4 5)) 4)
(= (#(second (reverse %)) ["a" "b" "c"]) "b")
(= (#(second (reverse %)) [[1 2] [3 4]]) [1 2])
