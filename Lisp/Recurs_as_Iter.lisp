;;;; Compute Recursion as Iteration
;;;; Write a procedure that computes f by means of an iterative process
;;;; A function f is defined by the rule that f(n) = n if n < 3 and 
;;;; f(n) = f(n-1) + 2f(n-2) + 3f(n-3) if n >= 3.
;;;; Iterative process keeps track of three things:
;;;; f(n) = f(n-1) + 2f(n-2) + 3f(n-3)
;;;; Therefore, I need 3 pieces of state to track the current,
;;;; the last and the penultimate values of f. Call them a, b, c.
;;;; for _ in 2..n:
;;;;	a=NEWVALUE
;;;;	b=a
;;;;	c=b
;;;;	return a
;;;; What is NEWVALUE? Now that we have representations for 
;;;; f(n-1), f(n-2), f(n-3, it's just the recursive equation:
;;;; for _ in 2..n:
;;;;	a=a + 2*b + 3*c
;;;;	b=a
;;;;	c=b
;;;;	return a
;;;; Now all that is left is to figure out the initial values of a, b, c.
;;;; But that is easy, since we know that f(n) = n if n < 3.
;;;; if n < 3: return n
;;;;	a=2 :: f(n-1) where n = 3
;;;;	b=1 :: f(n-2) where n = 3
;;;;	c=0 :: f(n-3) where n = 3
;;;; Now start off counting at 3
;;;; for _ in 3..n:
;;;;	a = a + 2*b + 3*c
;;;;	b=a
;;;;	c=b
;;;;	return a

(defun f (n)
  (if(< n 3) n
     (f-iter 2 1 0 n)))

(defun f-iter (a b c count)
  (if (< count 3) a
      (f-iter (+ a (* 2 b) (* 3 c))
              a
              b
              (- count 1))))
