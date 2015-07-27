;;;; If we list all the natural numbers below 10 that are multiples of 3 and 5,
;;;; we get 3, 5, 6, and 9. The sum of these multiples is 23. Find the sum
;;;; of all the multiples of 3 or 5 below 1000.

(defvar sumif (n x theSum)
    (if (> x n)
	    0
	(< x n)
	    (if (or (mod x 3) (mod x 5))
	        (sumif n (1+ x) (+ theSum x))
	    (sumif n (1+ x) theSum))))
