;; Flatten Sequence without explicit flatten function

#(filter (complement sequential?) (tree-seq sequential? identity %))
