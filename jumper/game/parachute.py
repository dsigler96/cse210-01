import random

class Parachute:

    def __init__(self):
        self._word_list = ["abuse","adult","agent","anger","apple","award","basis","beach","birth","block","blood","board","brain","bread","break","brown","buyer","cause",
                           "chain","chair","chest","chief","child","china","claim","class","clock","coach","coast","court","cover","cream","crime","cross","crowd","crown",
                           "cycle","dance","death","depth","doubt","draft","drama","dream","dress","drink","drive","earth","enemy","entry","error","event","faith","fault",
                           "field","fight","final","floor","focus","force","frame","frank","front","fruit","glass","grant","grass","green","group","guide","heart","henry",
                           "horse","hotel","house","image","index","input","issue","japan","jones","judge","knife","laura","layer","level","lewis","light","limit","lunch",
                           "major","march","match","metal","model","money","month","motor","mouth","music","night","noise","north","novel","nurse","offer","order","other",
                           "owner","panel","paper","party","peace","peter","phase","phone","piece","pilot","pitch","place","plane","plant","plate","point","pound","power",
                           "press","price","pride","prize","proof","queen","radio","range","ratio","reply","right","river","round","route","rugby","scale","scene","scope",
                           "score","sense","shape","share","sheep","sheet","shift","shirt","shock","sight","simon","skill","sleep","smile","smith","smoke","sound","south",
                           "space","speed","spite","sport","squad","staff","stage","start","state","steam","steel","stock","stone","store","study","stuff","style","sugar",
                           "youth","table","taste","terry","theme","thing","title","total","touch","tower","track","trade","train","trend","trial","trust","truth","uncle",
                           "union","unity","value","video","visit","voice","waste","watch","water","while","white","whole","woman","world","youth"]
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
        self._game_over = '''
   X
  /|\\
  / \\
     
^^^^^^^'''

    def cut_line(self):
        self._lives = self._lives - 1
        return 

    def get_lives(self):
        return self._lives

    def get_parachute(self):
        return self._parachute
    
    def get_game_over(self):
        return self._game_over

    def get_word(self):
        return self._word
    
