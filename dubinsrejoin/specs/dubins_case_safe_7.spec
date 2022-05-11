; Dubins Rejoin property safe_7

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
(assert <= X_0 0.09531943749537336
(assert >= X_0 0.08731943749537335

; Input 1
(assert <= X_1 -0.3150010408620675
(assert >= X_1 -0.3230010408620675

; Input 2
(assert <= X_2 -0.4015917115119976
(assert >= X_2 -0.4095917115119976

; Input 3
(assert <= X_3 -0.2595095100472383
(assert >= X_3 -0.26750951004723833

; Input 4
(assert <= X_4 0.5039999999999999
(assert >= X_4 0.49599999999999994

; Input 5
(assert <= X_5 0.004000000000000036
(assert >= X_5 -0.0039999999999999645

; Input 6
(assert <= X_6 0.20439849912315625
(assert >= X_6 0.19639849912315624

; Input 7
(assert <= X_7 -0.4540834438715137
(assert >= X_7 -0.46208344387151373

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
