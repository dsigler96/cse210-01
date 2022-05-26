class Service:
    #The main purpose of this program would be to print everything

    def show_guess(self, guess):
        print(guess.get_guess())

    def show_parachute(self, parachute):
        lives = parachute.get_lives()
        para  = parachute.get_parachute()
        if lives >= 1:
            i = 4 - lives
            k = 0
            if lives != i:
                for k in i:
                    para.pop(k)
            for row in para:
                print(para[row])
        else:
            print(parachute.get_game_over())

    def read_letter(self, prompt):
        return print(prompt)

    