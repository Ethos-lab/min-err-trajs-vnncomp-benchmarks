; Dubins Rejoin property safe_4

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
(assert <= X_0 0.3590598423470447
(assert >= X_0 0.32705984234704466

; Input 1
(assert <= X_1 -0.5043792736273645
(assert >= X_1 -0.5363792736273645

; Input 2
(assert <= X_2 0.8461687249028403
(assert >= X_2 0.8141687249028403

; Input 3
(assert <= X_3 -0.6171841340512165
(assert >= X_3 -0.6491841340512166

; Input 4
(assert <= X_4 0.516
(assert >= X_4 0.484

; Input 5
(assert <= X_5 0.01600000000000002
(assert >= X_5 -0.016000000000000007

; Input 6
(assert <= X_6 -0.1298625664804838
(assert >= X_6 -0.16186256648048383

; Input 7
(assert <= X_7 0.494251096914295
(assert >= X_7 0.46225109691429495

; unsafe if command is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14] (spec type disjunct) 
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
	( and (<= Y_0 Y_3) (<= Y_1 Y_3) (<= Y_2 Y_3) (<= Y_4 Y_2) (<= Y_5 Y_2) (<= Y_7 Y_2) 	)
)
