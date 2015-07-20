;;;; A function f is defined by the rule that f(n) = n if n<3 and
;;;; f(n) = f(n-1) + 2(f(n-2)) + 3(f(n-3)) if n>=3. Write a
;;;; procedure that computes f by means of a recursive process.

(defun func(n)
    (if (< n 3) n
        (+ (func(- n 1)) (* 2 (func(- n 2))) (* 3 (func(- n 3))))))
