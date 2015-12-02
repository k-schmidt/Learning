;; Write a function which takes a string and returns a new string containing
;; only the capital letters.

#(apply str (re-seq #"[A-Z]" %))
