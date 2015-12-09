;; Replicate a Sequence
;; Write a function which replicates each element of a sequence a
;; variable number of times.

(fn [col n]
  (mapcat (fn [x]
            (repeat n x))
          col))
