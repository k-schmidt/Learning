calcbmis :: [(Double, Double)] -> [Double]
calcbmis xs = [bmi w h | (w,h) <- xs]
	where
		bmi weight height = weight / height ^ 2
