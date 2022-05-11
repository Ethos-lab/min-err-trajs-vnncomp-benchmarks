; Dubins Rejoin property safe_6

(declare-const X_0 Real)
(declare-const X_1 Real)
(declare-const X_2 Real)
(declare-const X_3 Real)
(declare-const X_4 Real)
(declare-const X_5 Real)
(declare-const X_6 Real)
(declare-const X_7 Real)

(declare-const Y_0 Real
(declare-const Y_1 Real
(declare-const Y_2 Real
(declare-const Y_3 Real
(declare-const Y_4 Real
(declare-const Y_5 Real
(declare-const Y_6 Real
(declare-const Y_7 Real
(declare-const Y_8 Real
(declare-const Y_9 Real
(declare-const Y_10 Real
(declare-const Y_11 Real
(declare-const Y_12 Real
(declare-const Y_13 Real
(declare-const Y_14 Real
(declare-const Y_15 Real

; Input 0
(assert <= X_0 0.09331943749537336
(assert >= X_0 0.08931943749537335

; Input 1
(assert <= X_1 -0.3170010408620675
(assert >= X_1 -0.3210010408620675

; Input 2
(assert <= X_2 -0.4035917115119976
(assert >= X_2 -0.4075917115119976

; Input 3
(assert <= X_3 -0.2615095100472383
(assert >= X_3 -0.26550951004723833

; Input 4
(assert <= X_4 0.5019999999999999
(assert >= X_4 0.49799999999999994

; Input 5
(assert <= X_5 0.0020000000000000356
(assert >= X_5 -0.0019999999999999645

; Input 6
(assert <= X_6 0.20239849912315624
(assert >= X_6 0.19839849912315624

; Input 7
(assert <= X_7 -0.4560834438715137
(assert >= X_7 -0.46008344387151373

; unsafe if command is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] (spec type disjunct) 
(assert or 
	( and (<= Y_1 Y_0) (<= Y_2 Y_0) (<= Y_3 Y_0) (<= Y_4 Y_1) (<= Y_6 Y_1) (<= Y_7 Y_1) 	)
	( and (<= Y_1 Y_0) (<= Y_2 Y_0) (<= Y_3 Y_0) (<= Y_4 Y_2) (<= Y_5 Y_2) (<= Y_7 Y_2) 	)
	( and (<= Y_1 Y_0) (<= Y_2 Y_0) (<= Y_3 Y_0) (<= Y_4 Y_3) (<= Y_5 Y_3) (<= Y_6 Y_3) 	)
	( and (<= Y_0 Y_1) (<= Y_2 Y_1) (<= Y_3 Y_1) (<= Y_5 Y_0) (<= Y_6 Y_0) (<= Y_7 Y_0) 	)
	( and (<= Y_0 Y_1) (<= Y_2 Y_1) (<= Y_3 Y_1) (<= Y_4 Y_1) (<= Y_6 Y_1) (<= Y_7 Y_1) 	)
	( and (<= Y_0 Y_1) (<= Y_2 Y_1) (<= Y_3 Y_1) (<= Y_4 Y_2) (<= Y_5 Y_2) (<= Y_7 Y_2) 	)
	( and (<= Y_0 Y_1) (<= Y_2 Y_1) (<= Y_3 Y_1) (<= Y_4 Y_3) (<= Y_5 Y_3) (<= Y_6 Y_3) 	)
	( and (<= Y_0 Y_2) (<= Y_1 Y_2) (<= Y_3 Y_2) (<= Y_5 Y_0) (<= Y_6 Y_0) (<= Y_7 Y_0) 	)
	( and (<= Y_0 Y_2) (<= Y_1 Y_2) (<= Y_3 Y_2) (<= Y_4 Y_1) (<= Y_6 Y_1) (<= Y_7 Y_1) 	)
	( and (<= Y_0 Y_2) (<= Y_1 Y_2) (<= Y_3 Y_2) (<= Y_4 Y_2) (<= Y_5 Y_2) (<= Y_7 Y_2) 	)
	( and (<= Y_0 Y_2) (<= Y_1 Y_2) (<= Y_3 Y_2) (<= Y_4 Y_3) (<= Y_5 Y_3) (<= Y_6 Y_3) 	)
	( and (<= Y_0 Y_3) (<= Y_1 Y_3) (<= Y_2 Y_3) (<= Y_5 Y_0) (<= Y_6 Y_0) (<= Y_7 Y_0) 	)
	( and (<= Y_0 Y_3) (<= Y_1 Y_3) (<= Y_2 Y_3) (<= Y_4 Y_1) (<= Y_6 Y_1) (<= Y_7 Y_1) 	)
	( and (<= Y_0 Y_3) (<= Y_1 Y_3) (<= Y_2 Y_3) (<= Y_4 Y_2) (<= Y_5 Y_2) (<= Y_7 Y_2) 	)
	( and (<= Y_0 Y_3) (<= Y_1 Y_3) (<= Y_2 Y_3) (<= Y_4 Y_3) (<= Y_5 Y_3) (<= Y_6 Y_3) 	)
)
