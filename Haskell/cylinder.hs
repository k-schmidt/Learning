cylinder :: Double -> Double -> Double
cylinder r h = 
	let sidearea = 2 * pi * r * h;
		toparea = pi * r ^ 2
	in	sidearea + 2 * toparea
