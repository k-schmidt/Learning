bmitell2 :: Double -> Double -> String
bmitell2 weight height
	| bmitell <= skinny	= "You're underweight, you emo, you!"
	| bmitell <= normal	= "You're supposedly normal. Pfft, I bet you're ugly!"
	| bmitell <= fat 	= "You're fat! Lose some weight, fatty!"
	| otherwise 		= "You're a whale, congratulations!"
	where
		bmitell	= weight / height ^ 2
		skinny	= 18.5
		normal	= 25.0
		fat 	= 30.0
