;;;; The numbers at the edge of the triangle are 1, and each number inside
;;;; the triangle is the sum of the two numbers above it. Write a procedure
;;;; that computes elements of Pascal's triangle.

(defun pascal (n)
    (genrow n '(1)))

(defun genrow (n l)
    (when (< 0 n)
        (print l)
	(genrow (1- n) (cons 1 (newrow l)))))

(defun newrow (l)
    (if (> 2 (length l))
	'(1)
	(cons (+ (car l) (cadr l)) (newrow (cdr l)))))
