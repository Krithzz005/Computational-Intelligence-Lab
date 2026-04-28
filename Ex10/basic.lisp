[23bcs074@mepcolinux ex10]$cat code
STRING

(defun my-length (str)
  (if (string= str "")
      0
      (+ 1 (my-length (subseq str 1)))))

(defun my-reverse (str)
  (if (string= str "")
      ""
      (concatenate 'string
        (my-reverse (subseq str 1))
        (subseq str 0 1))))

(defun count-vowels (str)
  (if (string= str "")
      0
      (+ (if (member (char (string-downcase str) 0) '(#\a #\e #\i #\o #\u)) 1 0)
         (count-vowels (subseq str 1)))))

(defun run-string-ops ()
  (format t "Enter a string: ")
  (finish-output)
  (let ((s (read-line)))
    (format t "Length: ~a~%" (my-length s))
    (format t "Reverse: ~a~%" (my-reverse s))
    (format t "Vowels: ~a~%" (count-vowels s))
(values)))

OUTPUT

CL-USER 1 > (run-string-ops)
Enter a string: have a nice day
Length: 15
Reverse: yad ecin a evah
Vowels: 6

CL-USER 2 > (run-string-ops)
Enter a string: hello
Length: 5
Reverse: olleh
Vowels: 2

MATH

(defun my-gcd (a b)
  (if (= b 0)
      a
      (my-gcd b (mod a b))))

(defun my-lcm (a b)
  (/ (* a b) (my-gcd a b)))

(defun area (l w) (* l w))
(defun perimeter (l w) (* 2 (+ l w)))

(defun run-math-ops ()
  (format t "Enter two numbers for GCD/LCM: ")
  (finish-output)
  (let* ((val1 (read))
         (val2 (read)))
    (format t "GCD: ~a~%" (my-gcd val1 val2))
    (format t "LCM: ~a~%" (my-lcm val1 val2)))

  (format t "~%Enter Length and Width: ")
  (finish-output)
  (let* ((l (read))
         (w (read)))
    (format t "Area: ~a~%" (area l w))
    (format t "Perimeter: ~a~%" (perimeter l w)))
  (values))

OUTPUT

CL-USER 3 > (run-math-ops)
Enter two numbers for GCD/LCM: 5 24
GCD: 1
LCM: 120

Enter Length and Width: 5 7
Area: 35
Perimeter: 24

CL-USER 4 > (run-math-ops)
Enter two numbers for GCD/LCM: 253 321
GCD: 1
LCM: 81213

Enter Length and Width: 14 20
Area: 280
Perimeter: 68

CALCULATOR

(defun calc (a b op)
  (cond
    ((= op 1) (+ a b))
    ((= op 2) (- a b))
    ((= op 3) (* a b))
    ((= op 4) (if (/= b 0) (/ a b) "Cannot divide by zero"))
    (t "Invalid")))

(defun run-calculator ()
  (format t "Enter First Number: ")
  (finish-output)
  (let ((n1 (read)))
    (format t "Enter Second Number: ")
    (finish-output)
    (let ((n2 (read)))
      (format t "Enter Choice (1-Add, 2-Sub, 3-Mul, 4-Div): ")
      (finish-output)
      (let ((choice (read)))
        (format t "Result: ~a~%" (calc n1 n2 choice)))))
  (values))

OUTPUT

CL-USER 5 > (run-calculator)
Enter First Number: 24
Enter Second Number: 4
Enter Choice (1-Add, 2-Sub, 3-Mul, 4-Div): 1
Result: 28

CL-USER 6 > (run-calculator)
Enter First Number: 30
Enter Second Number: 5
Enter Choice (1-Add, 2-Sub, 3-Mul, 4-Div): 2
Result: 25

CL-USER 7 > (run-calculator)
Enter First Number: 4
Enter Second Number: 2
Enter Choice (1-Add, 2-Sub, 3-Mul, 4-Div): 3
Result: 8

CL-USER 8 > (run-calculator)
Enter First Number: 8
Enter Second Number: 2
Enter Choice (1-Add, 2-Sub, 3-Mul, 4-Div): 4
Result: 4
[23bcs074@mepcolinux ex10]$exit
exit
