; Dubins Rejoin property safe_0

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
(assert <= X_0 0.3440598423470447
(assert >= X_0 0.3420598423470447

; Input 1
(assert <= X_1 -0.5193792736273645
(assert >= X_1 -0.5213792736273645

; Input 2
(assert <= X_2 0.8311687249028403
(assert >= X_2 0.8291687249028403

; Input 3
(assert <= X_3 -0.6321841340512165
(assert >= X_3 -0.6341841340512165

; Input 4
(assert <= X_4 0.501
(assert >= X_4 0.499

; Input 5
(assert <= X_5 0.0010000000000000078
(assert >= X_5 -0.0009999999999999922

; Input 6
(assert <= X_6 -0.14486256648048382
(assert >= X_6 -0.14686256648048382

; Input 7
(assert <= X_7 0.47925109691429496
(assert >= X_7 0.47725109691429496

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
