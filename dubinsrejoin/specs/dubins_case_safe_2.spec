; Dubins Rejoin property safe_2

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
(assert <= X_0 0.3470598423470447
(assert >= X_0 0.33905984234704467

; Input 1
(assert <= X_1 -0.5163792736273645
(assert >= X_1 -0.5243792736273645

; Input 2
(assert <= X_2 0.8341687249028403
(assert >= X_2 0.8261687249028403

; Input 3
(assert <= X_3 -0.6291841340512165
(assert >= X_3 -0.6371841340512165

; Input 4
(assert <= X_4 0.504
(assert >= X_4 0.496

; Input 5
(assert <= X_5 0.004000000000000008
(assert >= X_5 -0.003999999999999992

; Input 6
(assert <= X_6 -0.14186256648048381
(assert >= X_6 -0.14986256648048382

; Input 7
(assert <= X_7 0.48225109691429496
(assert >= X_7 0.47425109691429496

; unsafe if command is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] (spec type disjunct) 
(assert or 
	( and (<= Y_1 Y_0) (<= Y_2 Y_0) (<= Y_3 Y_0) (<= Y_5 Y_0) (<= Y_6 Y_0) (<= Y_7 Y_0) 	)
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
)