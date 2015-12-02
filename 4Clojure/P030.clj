;; Compress a Sequence
;; Write a function which removes consecutive duplicates from a sequence.

#(map first (partition-by identity %))
