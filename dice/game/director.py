from game.die import Die

class Director:
    def __init__(self):
        self.dice = []
        self.score = 0
        self.score_total = 0
        self.cont = True

        for i in range(5):
            die= Die()
            self.dice.append(die)

    def start_game(self):
        while self.cont:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        roll_dice = input("Roll dice? [y/n] ")
        self.cont = (roll_dice == "y")

    def do_updates(self):
        if not self.cont:
            return 

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score = self.score + die.points 
        self.score_total = self.score_total + self.score

    def do_outputs(self):
        if not self.cont:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.score_total}\n")
        self.cont == (self.score > 0)
