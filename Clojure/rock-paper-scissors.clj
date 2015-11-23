(ns rock-paper-scissors)

(def dominates
  {:rock :scissors
   :scissors :paper
   :paper :rock})

(def choices
  (keys dominates))

(defn winner
  "Rock-paper-scissor function to determine winner"
  [p1-choice p2-choice]
  (cond
    (= p1-choice p2-choice) nil
    (= (dominates p1-choice) p2-choice) p1-choice
    :else p2-choice))

(defn draw?
  "Takes two players' choices and returns true if their decisions are the same"
  [p1-choice p2-choice]
  (= p1-choice p2-choice))

(defn iwon?
  "Takes two players' choices and returns true if the first player won"
  [p1-choice p2-choice] 
  (= (winner p1-choice p2-choice) p1-choice))

(defprotocol Player
  "A rock/paper/scissors player"
  (choose [p] "return :rock, :paper, or :scissors")
  (update-player [p me you] "return a new player based on what you and I did"))

(defrecord Random
  []
  Player
  (choose [_] (rand-nth choices))
  (update-player [this me you] this))

(defrecord Stubborn
  [choice]
  Player
  (choose [_] choice)
  (update-player [this me you] this))

(defrecord Mean
  [last-winner]
  Player
  (choose [_] (if last-winner last-winner (rand-nth choices)))
  (update-player [_ me you]
    (->Mean (when (iwon? me you) me))))

(defn game
  "Main function to play a rock-paper-scissors game"
  [player-1 player-2 rounds]
  (loop
      [player-1 player-1
       player-2 player-2
       p1-score 0
       p2-score 0
       rounds rounds]
    (if (pos? rounds)
      (let [p1-choice (choose player-1)
            p2-choice (choose player-2)
            result (winner p1-choice p2-choice)]
        (recur
         (update-player player-1 p1-choice p2-choice)
         (update-player player-2 p2-choice p1-choice)
         (+ p1-score (if (= result p1-choice) 1 0))
         (+ p2-score (if (= result p2-choice) 1 0))
         (dec rounds)))
      {:player-1 p1-score :player-2 p2-score})))
