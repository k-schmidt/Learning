;; Drop Every Nth Item
;; Write a function which drops every Nth item from a sequence.

(= (__ [1 2 3 4 5 6 7 8] 3) [1 2 4 5 7 8])
(= (__ [:a :b :c :d :e :f] 2) [:a :c :e])
(= (__ [1 2 3 4 5 6] 4) [1 2 3 5 6])

(fn drop-nth [col drop]
  (keep-indexed
   (fn [idx n]
     (if-not (= 0 (mod (inc idx) drop)) n)) col))
