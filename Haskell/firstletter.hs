{-|
We can create the following as-pattern: xs@(x:y:ys). This pattern will match exactly the same lists that 
x:y:ys would, but you can easily access the entire original list using xs, instead of needing to 
type out x:y:ys every time.
-}
firstletter :: String -> String
firstletter "" = "Empty string, whoops!"
firstletter all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x] ++ "."
