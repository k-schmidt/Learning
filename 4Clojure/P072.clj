;; This problem uses the thread-last macro, ->>,
;; which is much like the thread-first macro.
;; The major difference is that it threads the expression
;; as the last argument through the forms. This is
;; especially useful if you want to use threading
;; on collection functions like map, filter, and
;; take where the collection is the last argument.

(--> [1 2 3 4 5 6 7 8] (filter even?) (take 3))
;; -> (2 4 6)

(= (apply + (map inc (take 3 (drop 2 [2 5 4 1 3 6]))))
   (->> [2 5 4 1 3 6] (drop 2) (take 3) (map inc) (apply +)))
