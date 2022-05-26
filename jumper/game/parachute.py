import random

class Parachute:

    def __init__(self):
        self._word_list = ["abuse","adult","agent","anger","award","beach","birth","block","board","brain","bread","break","brown","buyer","cause","chain","chair",
                           "chest","chief","child","china","claim","clock","coach","coast","court","cover","cream","crime","crowd","crown","dance","death","depth",
                           "doubt","draft","dream","drink","drive","earth","entry","faith","fault","field","fight","final","focus","force","frame","frank","front",
                           "fruit","grant","green","group","guide","heart","henry","horse","hotel","house","image","index","input","japan","jones","judge","knife",
                           "laura","layer","lewis","light","lunch","major","march","match","metal","model","money","month","mouth","music","night","noise","north",
                           "novel","nurse","order","other","owner","panel","party","peace","phase","phone","piece","pilot","pitch","place","plane","plant","plate",
                           "point","pound","power","price","pride","prize","queen","radio","range","ratio","reply","right","river","round","route","rugby","scale",
                           "scope","score","shape","share","shift","shirt","shock","sight","simon","smile","smith","smoke","sound","south","space","spite","sport",
                           "squad","stage","start","state","steam","stock","stone","store","study","style","sugar","youth","table","thing","touch","tower","track",
                           "trade","train","trend","trial","trust","truth","uncle","unity","value","video","visit","voice","waste","watch","water","while","white",
                           "whole","woman","world","youth"]
        self._word = self._word_list[random.randint(0, (len(self._word_list) - 1))]
        self._lives = 4
        self._parachute = [ "  ___",
                            " /___\\",
                            " \   /",
                            "  \ /",
                            "   O",
                            "  /|\\",
                            "  / \\",
                            "      ",
                            "^^^^^^^"]
        self._game_over = ["   X",
                           "  /|\\",
                           "  / \\",
                           "^^^^^^^"]


    def cut_line(self, cut):
        if cut == "T":
            self._lives = self._lives - 1
            self._parachute.pop(0)
        else:
            return 

    def get_parachute(self):
        if self._lives >= 1:
            return self._parachute
        else:
            return self._game_over

    def get_lives(self):
        return self._lives

    def get_parachute(self):
        return self._parachute
    
    def get_game_over(self):
        return self._game_over

    def get_word(self):
        return self._word
    
