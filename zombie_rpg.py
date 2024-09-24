import time
import random

# Booleans to check status
skill_check = False
sane = True
alive = True

# Colour Class
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[93m'
    OKRED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Variables for stats/name/mods
username = " "
charisma = 0    
charisma_mod = 0    # Persuasion
strength = 0
strength_mod = 0    #Strength rolls
determination = 0
dexterity = 0
dexterity_mod = 0   #Picking Locks etc
sanity = 0
health = 0
health_mod = 0
attack = 0
attack_mod = 0
all_stats = list()

# Main Inventory
inventory = []

# Spacer
def spacer(input):
    time.sleep(input)
    print(" ")

# Clear Screen
def clear_screen():
    print("\n" * 48)

# Wipes Stats for a Fresh Game
def stat_wipe():
    global username
    global charisma  
    global charisma_mod
    global strength
    global strength_mods
    global determination
    global dexterity
    global dexterity_mod
    global sanity
    global health
    global health_mod
    global attack
    global attack_mod
    global all_stats

    username = " "
    charisma = 0    
    charisma_mod = 0    # Persuassion
    strength = 0
    strength_mod = 0    #Strength rolls
    determination = 0
    dexterity = 0
    dexterity_mod = 0   #Picking Locks etc
    sanity = 0
    health = 0
    health_mod = 0
    attack = 0
    attack_mod = 0
    all_stats = list()

# Main Inventory
inventory = []

# # # ART # # #
# Text Art

def gametitle_screen():
    print(f"""{bcolors.OKGREEN}
               ████████╗██╗  ██╗███████╗
               ╚══██╔══╝██║  ██║██╔════╝
                  ██║   ███████║█████╗  
                  ██║   ██╔══██║██╔══╝  
                  ██║   ██║  ██║███████╗

       ███████╗ ██████╗ ███╗   ███╗██████╗ ██╗███████╗
       ╚══███╔╝██╔═══██╗████╗ ████║██╔══██╗██║██╔════╝
         ███╔╝ ██║   ██║██╔████╔██║██████╔╝██║█████╗  
        ███╔╝  ██║   ██║██║╚██╔╝██║██╔══██╗██║██╔══╝  
        ███████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██║███████╗
        ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝╚══════╝

     ██╗   ██╗ █████╗ ██████╗ ██╗ █████╗ ███╗   ██╗████████╗
     ██║   ██║██╔══██╗██╔══██╗██║██╔══██╗████╗  ██║╚══██╔══╝
     ██║   ██║███████║██████╔╝██║███████║██╔██╗ ██║   ██║   
     ╚██╗ ██╔╝██╔══██║██╔══██╗██║██╔══██║██║╚██╗██║   ██║   
      ╚████╔╝ ██║  ██║██║  ██║██║██║  ██║██║ ╚████║   ██║   
       ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                                       
    {bcolors.ENDC}
    """)

def bedroom_title_art():
    print(f"""{bcolors.OKRED}
     ██╗  ██╗ ██████╗ ███████╗██████╗ ██╗████████╗ █████╗ ██╗     
     ██║  ██║██╔═══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔══██╗██║     
     ███████║██║   ██║███████╗██████╔╝██║   ██║   ███████║██║     
     ██╔══██║██║   ██║╚════██║██╔═══╝ ██║   ██║   ██╔══██║██║     
     ██║  ██║╚██████╔╝███████║██║     ██║   ██║   ██║  ██║███████╗
     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝

    ██████╗ ███████╗██████╗ ██████╗  ██████╗  ██████╗ ███╗   ███╗
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
    ██████╔╝█████╗  ██║  ██║██████╔╝██║   ██║██║   ██║██╔████╔██║
    ██╔══██╗██╔══╝  ██║  ██║██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║
    ██████╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
    ╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝
    {bcolors.ENDC}""")

def morgue_title_art():
    print(f"""{bcolors.OKRED}
    ███╗   ███╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗███████╗
    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝ ██║   ██║██╔════╝
    ██╔████╔██║██║   ██║██████╔╝██║  ███╗██║   ██║█████╗  
    ██║╚██╔╝██║██║   ██║██╔══██╗██║   ██║██║   ██║██╔══╝  
    ██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝███████╗
    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
    {bcolors.ENDC}""")

def surgery_title_art():
    print(f"""{bcolors.OKRED}
    ███████╗██╗   ██╗██████╗  ██████╗ ███████╗██████╗ ██╗   ██╗
    ██╔════╝██║   ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗╚██╗ ██╔╝
    ███████╗██║   ██║██████╔╝██║  ███╗█████╗  ██████╔╝ ╚████╔╝ 
    ╚════██║██║   ██║██╔══██╗██║   ██║██╔══╝  ██╔══██╗  ╚██╔╝  
    ███████║╚██████╔╝██║  ██║╚██████╔╝███████╗██║  ██║   ██║   
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝
    {bcolors.ENDC}""")

def basement_title_art():
    print(f"""{bcolors.OKRED}
    ██████╗  █████╗ ███████╗███████╗███╗   ███╗███████╗███╗   ██╗████████╗
    ██╔══██╗██╔══██╗██╔════╝██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
    ██████╔╝███████║███████╗█████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
    ██╔══██╗██╔══██║╚════██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
    ██████╔╝██║  ██║███████║███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
    {bcolors.ENDC}""")

def gameover_art_win():
    print(f"""{bcolors.OKGREEN}
     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                            CREATED BY: TEAM RED
        Lorell Boscoe, Thom Butterworth, Jordan Richmond, and John Rowbotham
    {bcolors.ENDC}""")

def gameover_art_fail():
    print(f"""{bcolors.OKRED}
     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                            CREATED BY: TEAM RED
        Lorell Boscoe, Thom Butterworth, Jordan Richmond, and John Rowbotham
    {bcolors.ENDC}""")

def gameover_screen_fail():
    spacer(1)
    gameover_art_fail()
    play_again = input("""
    Would you like to play again? \nYes  |  No \n""")
    play_again = play_again.lower()
    if play_again == "yes":
        spacer(2)
        stat_wipe()
        print("\033c")
        intro()
    if play_again == "no":
        spacer(2)
        print("Thanks for playing!")
        spacer(15)
        print("\033c")
    else:
        spacer(1)
        print("I'm just going to take that as a no.")
        spacer(15)
        print("\033c")

def gamewin_art():
    print(f"""{bcolors.OKGREEN}
                                ______.........--=T=--.........______
                                .             |:|
                            :-. //           /""""""-.
                            ': '-._____..--""(""""""()`---.__
                            /:   _..__   ''  ":""""'[] |""`'' \
                            ': :'     `-.     _:._     '"""" :
                            ::          '--=:____:.___....-"
                                                O"       O"
    ██╗   ██╗ ██████╗ ██╗   ██╗    ███████╗███████╗ ██████╗ █████╗ ██████╗ ███████╗██████╗ 
    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ╚████╔╝ ██║   ██║██║   ██║    █████╗  ███████╗██║     ███████║██████╔╝█████╗  ██║  ██║
    ╚██╔╝  ██║   ██║██║   ██║    ██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝  ██║  ██║
     ██║   ╚██████╔╝╚██████╔╝    ███████╗███████║╚██████╗██║  ██║██║     ███████╗██████╔╝
     ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═════╝
                                CREATED BY: TEAM RED
        Lorell Boscoe, Thom Butterworth, Jordan Richmond, and John Rowbotham
    """)

def gamewin_screen():
    spacer(1)
    gamewin_art()
    play_again = input("""
    Would you like to play again? \nYes  |  No \n""")
    play_again = play_again.lower()
    if play_again == "Yes":
        spacer(2)
        stat_wipe()
        print("\033c")
        intro()
    if play_again == "No":
        spacer(2)
        print("Thanks for playing!")
        spacer(15)
        print("\033c")
    else:
        spacer(1)
        print("I'm just going to take that as a no.")
        spacer(15)
        print("\033c")

def scanning_art():
    print(f"""{bcolors.OKRED}
                             _                   
                            (_)                  
     ___  ___ __ _ _ __  _ __  _ _ __   __ _       
    / __|/ __/ _` | '_ \| '_ \| | '_ \ / _` |      
    \__ \ (_| (_| | | | | | | | | | | | (_| |_ _ _ 
    |___/\___\__,_|_| |_|_| |_|_|_| |_|\__, (_|_|_)
                                        __/ |      
                                        |___/                                       
    {bcolors.ENDC}""")

def success_art():
    print(f"""{bcolors.OKGREEN}
                                  
     ___ _   _  ___ ___ ___  ___ ___ 
    / __| | | |/ __/ __/ _ \/ __/ __|
    \__ \ |_| | (_| (_|  __/\__ \__ \       
    |___/\__,_|\___\___\___||___/___/
                                  
    {bcolors.ENDC}""")

# Inventory Art
def zombiefinger_art():
    print("         /-\            ")
    print("        |\./|           ")
    print("        |   |           ")
    print("        |   |           ")
    print("        |>~<|           ")
    print("        |   |           ")
    print("        |   |           ")
    print("        |   |           ")
    print("        |   |           ")
    print(f"        -{bcolors.OKRED}~~~{bcolors.ENDC}-           ")
    print(f"        {bcolors.OKRED}; : ;{bcolors.ENDC}           ")
    print(f"          {bcolors.OKRED};{bcolors.ENDC}             ")

def terminatorhand_art():
    print("         /-\            ")
    print("     /-\|\./|/ \        ")
    print("    |\./|   |\./|       ")
    print("    |   |   |   |       ")
    print("    |   |>~<|   |/-\    ")
    print("    |>~<|   |>~<|\./|   ")
    print("    |   |   |   |   |   ")
    print("/~T\|   |   =[@]=   |   ")
    print("|_/ |   |   |   |   |   ")
    print("|   | ~   ~   ~ |   |   ")
    print("|~< |             ~ |   ")
    print("|   '               |   ")
    print("\                   |   ")
    print(" \   S K Y N E T   /    ")
    print("  \               /     ")
    print("   \.            /      ")
    print("     |          |       ")
    print("     |          |       ")
    print("                        ")

def scalpel_art():
    print("      ______________________________ ______________________   ")
    print("    .'                              | (_)     (_)    (_)   \  ")
    print("  .'                                |  __________________   } ")
    print(".'_.............................____|_(                  )_/  ")
    print("                                                              ")

def sceptre_art():
    print("               .::.                              ")
    print("            .      `.                            ")
    print(f"          :   {bcolors.OKCYAN}~*~{bcolors.ENDC}   :                           ") 
    print(f"          :    {bcolors.OKCYAN}***{bcolors.ENDC}   :       ::                 ")
    print(f"          :   {bcolors.OKCYAN}*****{bcolors.ENDC}  :         ::               ")
    print(f"          .   {bcolors.OKCYAN}***{bcolors.ENDC}   .          ::              ")
    print(f"           .  {bcolors.OKCYAN}~*~{bcolors.ENDC}  .              ::            ") 
    print("             `.    .                ::           ")
    print("              :/\/\:                :;          ")
    print("              :/\/\:                :;        ")
    print("              :/\/\:               :;       ")
    print("              :/\/\:              :;      ")
    print("              :/\/\:             :     ")
    print("              :/\/\:             :    ")
    print("              :/\/\:            :    ")
    print("              :/\/\:           :    ")
    print("              ::::::          :   ")
    print("              [LOKI]         :  ")
    print("              [POKI]        :   ")
    print("              [STIK]       :   ")
    print("              [____]     :    ")
    print("              [____]   .:`   ")

def lockclosed_image():
    print("                                    ████████                                  ")
    print("                              ██████        ██████                            ")
    print("                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░▓▓██                        ")
    print("                      ██░░░░░░░░▒▒▒▒████████▒▒▒▒░░░░░░░░██                    ")
    print("                    ██  ░░░░▒▒▒▒████        ████▒▒▒▒░░░░  ██                  ")
    print("                  ▓▓░░░░░░▒▒████                ████▒▒░░░░░░▓▓                ")
    print("                  ██░░░░▒▒██                        ██▒▒░░░░██                ")
    print("                ██░░░░▒▒██                            ██▒▒░░░░██              ")
    print("                ██░░▒▒██                                ██▒▒░░██              ")
    print("              ██░░░░▒▒██                                ██▒▒░░░░██            ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("      ▒▒▒▒▒▒██░░░░▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒░░░░██▒▒▒▒▒▒    ")
    print("    ██░░░░░░██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒██░░░░░░██  ")
    print("  ██░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░██")
    print("  ██▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒██")
    print("  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
    print("   ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██   ")
    print("      ████████████████████████████████████████████████████████████████████    ")

def lockopen_image():
    print("                                    ████████                                  ")
    print("                              ██████        ██████                            ")
    print("                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░▓▓██                        ")
    print("                      ██░░░░░░░░▒▒▒▒████████▒▒▒▒░░░░░░░░██                    ")
    print("                    ██  ░░░░▒▒▒▒████        ████▒▒▒▒░░░░  ██                  ")
    print("                  ▓▓░░░░░░▒▒████                ████▒▒░░░░░░▓▓                ")
    print("                  ██░░░░▒▒██                        ██▒▒░░░░██                ")
    print("                ██░░░░▒▒██                            ██▒▒░░░░██              ")
    print("                ██░░▒▒██                                ██▒▒░░██              ")
    print("              ██░░░░▒▒██                                ██▒▒░░░░██            ")
    print("            ██░░░░▒▒██                                                        ")
    print("            ██░░░░▒▒██                                                        ")
    print("            ██░░░░▒▒██                                                        ")
    print("            ██░░░░▒▒██                                                        ")
    print("            ██░░░░▒▒██                                                        ")
    print("      ▒▒▒▒▒▒██░░░░▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ")
    print("    ██░░░░░░██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░██")
    print("  ██▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒██")
    print("  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
    print("   ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██   ")
    print("      ████████████████████████████████████████████████████████████████████    ")

def lock_animation():   # Animates Lock Opening
    for i in range(1):
        clear_screen()
        lockclosed_image()
        time.sleep(2)
        clear_screen()
        lockopen_image()
        time.sleep(0.5)

# Stat Table
def stat_table():
    print(f"            {bcolors.OKYELLOW}Your Stats{bcolors.ENDC}")
    print(f"{bcolors.OKRED}Sanity{bcolors.ENDC}: {sanity}        {bcolors.OKRED}Dexterity{bcolors.ENDC}: {dexterity}")
    print(f"{bcolors.OKRED}Strength{bcolors.ENDC}: {strength}        {bcolors.OKRED}Charisma{bcolors.ENDC}: {charisma}")
    print(f"{bcolors.OKRED}Determination{bcolors.ENDC}: {determination}\n")
# Sanity & Health Checks
# Called on loss of these stats to check level/punish/reward
def health_check():
    global alive
    global health
    if health <= 0:
        alive = False
        spacer(1)
        print("Unfortunately, your health is now zero...")
        spacer(0.5)
        print("You have died...")
        spacer(3)
        clear_screen()
        gameover_screen_fail()
    else:
        alive = True

def sanity_check():
    global sane
    global sanity
    global health

    sanity_attempt = 0

    if sanity <= 0:
        sane = False
        spacer(1)
        print("Bad luck, you've gone completely insane...")
        spacer(1)
        print("An abandoned hospital is no place for the insane.")
        spacer(1)
        print("You get lost amongst the commotion, muttering something about an all seeing eye, ironically, never to be seen again.")
        spacer(3)
        clear_screen()
        gameover_screen_fail()
    elif sanity in range(11, 15) and sanity_attempt == 0:
        spacer(1)
        print("You're starting to go a bit mad?")
        spacer(1)
        print("QUICK! Let's do some simple maths to keep you sharp!")
        spacer(0.5)
        sanity_maths = input("What's 46 multiplied by 82? \n")
        if sanity_maths == str(46*82):
            spacer(3)
            print("Good work! You're still sharp")
            sanity += 1
            sanity_attempt += 1
        else:
            spacer(3)
            print("I thought that would be easy for you...guess not.")
            sanity -= 2
            spacer(1)
            print("The confusion of doing maths has somehow injured you.")
            health -= 2
            health_check()
            print(f"Your health is now {bcolors.BOLD}{bcolors.OKRED}{health}{bcolors.ENDC}HP!")
            sanity_attempt += 1
            sane = True
    elif sanity in range(6, 10) and sanity_attempt == 0:
        spacer(1)
        print("You're going even madder!")
        spacer(1)
        print("WHAT'S THAT?!")
        spacer(2)
        print("You've lashed out to attack the figure...it was your own arm...2 damage!")
        health -= 2
        health_check()
        spacer(1)
        print(f"Your health is now {bcolors.BOLD}{bcolors.OKRED}{health}{bcolors.ENDC}HP!")
        sanity_attempt += 1
        sane = True
    elif sanity in range(1, 5) and sanity_attempt == 0:
        sanity_attempt += 1
        spacer(1)
        print("You're properly mad...")
        spacer(1)
        print("We're going to need some real brain teaser to bring you back...")
        spacer(1)
        sanity_ceaser = input("""
        DECODE THIS SENTENCE: Lw'v RN wr eh pdg vrphwlphv
        """)
        sanity_ceaser = sanity_ceaser.lower()
        if sanity_ceaser.strip() == "it's ok to be mad sometimes" or "its ok to be mad sometimes":
            spacer(1)
            print("HAIL CEASER! You got it!")
            sanity += 2
            health += 2
            spacer(0.5)
            print("You've had a little pick me up, how smug.")
            print(f"Your health is now {bcolors.BOLD}{bcolors.OKRED}{health}{bcolors.ENDC}HP!")
            sane = True
        else:
            spacer(1)
            print("Sorry...wkdw'v qrw lw.")
            spacer(2)
            health -= 2
            health_check()
            print("You've hit yourself in frustration...but a bit too hard.")
            print(f"You now have {bcolors.BOLD}{bcolors.OKRED}{health}{bcolors.ENDC}HP!")
            sane = True
    else:
        sane = True

# Skill Checks
# Uses player mods to roll against a random number (emulating D&D DC rolls)
def veryeasy_skill(modifier):
    global charisma_mod
    global dexterity_mod
    global strength_mod
    global skill_check

    skill_roll = random.randint(1, 20)

    if skill_roll + modifier <= 5:
        print("You have failed the check!")
        print(f"You only rolled a {bcolors.BOLD}{bcolors.OKRED}{skill_roll}{bcolors.ENDC}, which wasn't enough even with your + {bcolors.BOLD}{bcolors.OKRED}{modifier}{bcolors.ENDC}!")
        skill_check = False
    else:
        print(f"That's a {bcolors.BOLD}{bcolors.OKRED}{skill_roll}{bcolors.ENDC} + {bcolors.BOLD}{bcolors.OKRED}{modifier}{bcolors.ENDC}! You pass the check!")
        skill_check = True

def easy_skill(modifier):
    global charisma_mod
    global dexterity_mod
    global strength_mod
    global skill_check

    skill_roll = random.randint(1, 20)

    if skill_roll + modifier <= 10:
        print("You have failed the check!")
        print(f"You only rolled a {bcolors.BOLD}{bcolors.OKRED}{skill_roll}{bcolors.ENDC}, which wasn't enough even with your + {bcolors.BOLD}{bcolors.OKRED}{modifier}{bcolors.ENDC}!")
        skill_check = False
    else:
        print(f"That's a {bcolors.BOLD}{bcolors.OKRED}{skill_roll}{bcolors.ENDC} + {bcolors.BOLD}{bcolors.OKRED}{modifier}{bcolors.ENDC}! You pass the check!")
        skill_check = True


def med_skill(modifier):
    global charisma_mod
    global dexterity_mod
    global strength_mod
    global skill_check

    skill_roll = random.randint(1, 20)

    if skill_roll + modifier <= 15:
        print("You have failed the check!")
        print(f"You only rolled a {bcolors.BOLD}{bcolors.OKRED}{skill_roll}{bcolors.ENDC}, which wasn't enough even with your + {bcolors.BOLD}{bcolors.OKRED}{modifier}{bcolors.ENDC}!")
        skill_check = False
    else:
        print(f"That's a {bcolors.BOLD}{bcolors.OKRED}{skill_roll}{bcolors.ENDC} + {bcolors.BOLD}{bcolors.OKRED}{modifier}{bcolors.ENDC}! You pass the check!")
        skill_check = True


def hard_skill(modifier):
    global charisma_mod
    global dexterity_mod
    global strength_mod
    global skill_check

    skill_roll = random.randint(1, 20)

    if skill_roll + modifier <= 20:
        print("You have failed the check!")
        print(f"You only rolled a {bcolors.BOLD}{bcolors.OKRED}{skill_roll}{bcolors.ENDC}, which wasn't enough even with your + {bcolors.BOLD}{bcolors.OKRED}{modifier}{bcolors.ENDC}!")
        skill_check = False
    else:
        print(f"That's a {bcolors.BOLD}{bcolors.OKRED}{skill_roll}{bcolors.ENDC} + {bcolors.BOLD}{bcolors.OKRED}{modifier}{bcolors.ENDC}! You pass the check!")
        skill_check = True

def veryhard_skill(modifier):    # Basically Impossible
    global charisma_mod
    global dexterity_mod
    global strength_mod
    global skill_check

    skill_roll = random.randint(1, 20)

    if skill_roll + modifier <= 23:
        print("You have failed the check!")
        print(f"You only rolled a {bcolors.BOLD}{bcolors.OKRED}{skill_roll}{bcolors.ENDC}, which wasn't enough even with your + {bcolors.BOLD}{bcolors.OKRED}{modifier}{bcolors.ENDC}!")
        skill_check = False
    else:
        print(f"That's a {bcolors.BOLD}{bcolors.OKRED}{skill_roll}{bcolors.ENDC} + {bcolors.BOLD}{bcolors.OKRED}{modifier}{bcolors.ENDC}! You pass the check!")
        skill_check = True

# # # Character Creator Functions # # #
# Stats Roller - Rolls 4d20, removes the lowest values, adds them together
def stats_roll():
    stats = list()
    while len(stats) < 4:
        stats.append(random.randint(1, 6))
    stats.remove(min(stats))
    stat_indv = sum(stats)
    all_stats.append(stat_indv)

# Assigns Modifers based on stat scores
def mods_assign():
    global strength
    global strength_mod
    global charisma
    global charisma_mod
    global dexterity
    global dexterity_mod

    if strength in range(18,20):
        strength_mod = 4
    elif strength in range(16,17):
        strength_mod = 3
    elif strength in range(14,15):
        strength_mod = 2
    elif strength in range(12,13):
        strength_mod = 1
    elif strength in range(8,9):
        strength_mod -= 1
    elif strength in range(6,7):
        strength_mod -= 2
    elif strength in range(4,5):
        strength_mod -= 3
    else:
        strength_mod = strength_mod
    
    if charisma in range(18,20):
        charisma_mod = 4
    elif charisma in range(16,17):
        charisma_mod = 3
    elif charisma in range(14,15):
        charisma_mod = 2
    elif charisma in range(12,13):
        charisma_mod = 1
    elif charisma in range(8,9):
        charisma_mod -= 1
    elif charisma in range(6,7):
        charisma_mod -= 2
    elif charisma in range(4,5):
        charisma_mod -= 3
    else:
        charisma_mod = charisma_mod

    if dexterity in range(18,20):
        dexterity_mod = 4
    elif dexterity in range(16,17):
        dexterity_mod = 3
    elif dexterity in range(14,15):
        dexterity_mod = 2
    elif dexterity in range(12,13):
        dexterity_mod = 1
    elif dexterity in range(8,9):
        dexterity_mod -= 1
    elif dexterity in range(6,7):
        dexterity_mod -= 2
    elif dexterity in range(4,5):
        dexterity_mod -= 3
    else:
        dexterity_mod = dexterity_mod 

# Attack/Health Generators
def attack_scorer():
    global strength
    global sanity
    global dexterity
    global attack_mod
    global attack_score
    attack_base = strength + dexterity + sanity
    attack_base = attack_base / 3
    attack_score = int(attack_base + attack_mod)
    return attack_score

def health_scorer():
    global charisma
    global determination
    global sanity
    global health
    global health_mod

    health_base = determination + sanity + charisma
    health_base = health_base / 3
    health = int(health_base + health_mod)
    return health

# # # GAME STORY # # #
# Intro/Character Creation
def intro():
    global username

    spacer(1)
    gametitle_screen()
    spacer(5)
    print(f"Your nightmare begins in the {bcolors.BOLD}{bcolors.OKYELLOW}City of London{bcolors.ENDC}.")
    spacer(1)
    print("The Capital has been under strict lockdown rules for several months.")
    spacer(1)
    print(f"The population is being overun by a {bcolors.BOLD}{bcolors.OKYELLOW}new variant{bcolors.ENDC} which is 99 percent infectious.")
    spacer(1)
    print("Your last memory is calling 999 as you begin to feel unwell...")
    spacer(1)
    username = input("Survivor, What Is Your Name? ")
    username = username.capitalize()
    spacer(1)
    print(f"Wakey Wakey {bcolors.OKBLUE}{username}{bcolors.ENDC}!")
    spacer(2)
    print(f"{bcolors.OKBLUE}{username}'s{bcolors.ENDC} eyes open")
    spacer(1)
    print("You find yourself in a hospital bed.")
    spacer(0.5)
    print(f"Take in your surroundings {bcolors.OKBLUE}{username}{bcolors.ENDC}. Things aren't what they seem out there!")
    spacer(2)
    create_char()

# Runs full chacter creation script (all the stats)
def create_char():
    stats_roll()
    stats_roll()
    stats_roll()
    stats_roll()
    stats_roll()
    stats_assign()

# Player assigns their own stats
def stats_assign():
    global all_stats
    global charisma
    global strength
    global determination
    global sanity
    global dexterity
    global username
    
    print(f"OK {bcolors.OKBLUE}{username}{bcolors.ENDC}. Let's roll your stats...")
    spacer(2)
    print(f"You rolled {bcolors.BOLD}{bcolors.OKRED}{all_stats}{bcolors.ENDC}")
    spacer(0.5)
    print("Let's put the highest number on what you think is most important.")
    spacer(1)
    print(f"{bcolors.BOLD}{bcolors.OKRED}Dexterity{bcolors.ENDC} and {bcolors.BOLD}{bcolors.OKRED}Strength{bcolors.ENDC} decide how hard you hit.")
    spacer(0.5)
    print(f"{bcolors.BOLD}{bcolors.OKRED}Charisma{bcolors.ENDC} and {bcolors.BOLD}{bcolors.OKRED}Determination{bcolors.ENDC} effect how long you'll live.")
    spacer(0.5)
    print(f"but {bcolors.BOLD}{bcolors.OKRED}Sanity{bcolors.ENDC} holds it all together...")
    spacer(2)
    while len(all_stats) != 0:
        spacer(1)
        stat_table()
        stat_request = input(f"""
        What is your most important stat?
        {bcolors.OKRED}Charisma | Sanity | Strength | Determination | Dexterity{bcolors.ENDC}?
        """)
        quest = stat_request.lower()
        if stat_request == "charisma" and charisma == 0:
            charisma = max(all_stats)
            print(f"Your {bcolors.BOLD}{bcolors.OKRED}Charisma{bcolors.ENDC} score is {bcolors.BOLD}{bcolors.OKRED}{charisma}{bcolors.ENDC}")
            all_stats.remove(max(all_stats))
            print(f"Your remaining stats are {bcolors.BOLD}{bcolors.OKRED}{all_stats}{bcolors.ENDC}")
            spacer(1)
        elif stat_request == "dexterity" and dexterity == 0:
            dexterity = max(all_stats)
            print(f"Your {bcolors.BOLD}{bcolors.OKRED}Dexterity{bcolors.ENDC} score is {bcolors.BOLD}{bcolors.OKRED}{dexterity}{bcolors.ENDC}")
            all_stats.remove(max(all_stats))
            print(f"Your remaining stats are {bcolors.BOLD}{bcolors.OKRED}{all_stats}{bcolors.ENDC}")
            spacer(1)
        elif stat_request == "strength" and strength == 0:
            strength = max(all_stats)
            print(f"Your {bcolors.BOLD}{bcolors.OKRED}Strength{bcolors.ENDC} score is {bcolors.BOLD}{bcolors.OKRED}{strength}{bcolors.ENDC}")
            all_stats.remove(max(all_stats))
            print(f"Your remaining stats are {bcolors.BOLD}{bcolors.OKRED}{all_stats}{bcolors.ENDC}")
            spacer(1)
        elif stat_request == "sanity" and sanity == 0:
            sanity = max(all_stats)
            print(f"Your {bcolors.BOLD}{bcolors.OKRED}Sanity{bcolors.ENDC} score is {bcolors.BOLD}{bcolors.OKRED}{sanity}{bcolors.ENDC}")
            all_stats.remove(max(all_stats))
            print(f"Your remaining stats are {bcolors.BOLD}{bcolors.OKRED}{all_stats}{bcolors.ENDC}")
            spacer(1)
        elif stat_request == "determination" and determination == 0:
            determination = max(all_stats)
            print(f"Your {bcolors.BOLD}{bcolors.OKRED}Determination{bcolors.ENDC} score is {bcolors.BOLD}{bcolors.OKRED}{determination}{bcolors.ENDC}")
            all_stats.remove(max(all_stats))
            print(f"Your remaining stats are {bcolors.BOLD}{bcolors.OKRED}{all_stats}{bcolors.ENDC}")
            spacer(1)
        else:
            print("Sorry, can you say that again?")
            spacer(1)
    spacer(2)
    attack_scorer()
    print(f"Your {bcolors.OKCYAN}attack score{bcolors.ENDC} is {bcolors.OKCYAN}{attack_score}{bcolors.ENDC}!")
    spacer(2)
    health_scorer()
    print(f"Your {bcolors.HEADER}health{bcolors.ENDC} is {bcolors.OKRED}{health}HP{bcolors.ENDC}!")
    spacer(3)
    sleep_or_go()

# Gives the option to restart the game
def sleep_or_go():
    print(f"OK {bcolors.OKBLUE}{username}{bcolors.ENDC}! Shall we get on with it?")
    sleep_choice = input("""Or would you like to move forward, or sleep and try again tomorrow?
    Go  |  Sleep

    """)
    sleep_choice = sleep_choice.lower()
    if sleep_choice.strip() == "go":
        spacer(1)
        print(f"OK {bcolors.OKBLUE}{username}{bcolors.ENDC}! Let's go!")
        spacer(1)
        bedroom()
    elif sleep_choice.strip() == "sleep":
        spacer(1)
        print(f"OK {bcolors.OKBLUE}{username}{bcolors.ENDC}, let's have a snooze...")
        spacer(1)
        stat_wipe()
        intro()
    else:
        spacer(1)
        print("Sorry, I didn't quite get that?")
        sleep_or_go()
    

# ROOM TWO - BEDROOM
def bedroom():
    spacer(1)
    bedroom_title_art()
    print("You look around the room, the lights are flickering on and off.")
    spacer(2)
    print(f"Whilst searching the room you come across a {bcolors.BOLD}{bcolors.OKYELLOW}chest of drawers{bcolors.ENDC}, a {bcolors.BOLD}{bcolors.OKYELLOW}wardrobe{bcolors.ENDC} and a {bcolors.BOLD}{bcolors.OKYELLOW}medicine cabinet{bcolors.ENDC}.")
    spacer(2)
    bedroom_choice1()
    
def bedroom_choice1():
    response = input(f"Would you like to loot the {bcolors.BOLD}{bcolors.OKYELLOW}chest of drawers{bcolors.ENDC}? \nYes / No?\n")
    response = response.lower()
    if response == "yes":
        spacer(2)
        print(f"You loot the {bcolors.BOLD}{bcolors.OKYELLOW}chest of drawers{bcolors.ENDC} and find a {bcolors.BOLD}{bcolors.OKCYAN}bottle of water{bcolors.ENDC}.")
        spacer(1)
        bedroom_choice2()
    elif response == "no":
        spacer(2)
        print ("You carry on looking around the room for loot.")
        spacer(1)
        bedroom_choice2()
    else: 
        spacer(2)
        print ("I didn't understand that. Please try the command again. \n")
        bedroom_choice1()
        
def bedroom_choice2():
    response = input(f"Would you like to loot the {bcolors.BOLD}{bcolors.OKYELLOW}wardrobe{bcolors.ENDC}? \nYes / No?\n")
    response = response.lower()
    if response == "yes":
        spacer(2)
        print(f"You loot the {bcolors.BOLD}{bcolors.OKYELLOW}wardrobe{bcolors.ENDC} and find nothing of use.")
        spacer(1)
        bedroom_choice3()
    elif response == "no":
        spacer(2)
        print ("You carry on looking around the room for loot.")
        spacer(1)
        bedroom_choice3()
    else: 
        spacer(2)
        print ("I didn't understand that. Please try the command again. \n")
        bedroom_choice2()

def bedroom_choice3():
    global health
    response = input(f"Would you like to loot the {bcolors.BOLD}{bcolors.OKYELLOW}medicine cabinet{bcolors.ENDC}? \nYes / No?\n")
    response = response.lower()
    if response == "yes":
        spacer(2)
        print(f"You loot the {bcolors.BOLD}{bcolors.OKYELLOW}medicine cabinet{bcolors.ENDC} and find a {bcolors.BOLD}{bcolors.OKCYAN}first aid kit{bcolors.ENDC} and then you head for the exit.")
        health += 3
        print(f"Your {bcolors.HEADER}health{bcolors.ENDC} is now {bcolors.OKRED}{health}HP{bcolors.ENDC}!")
        spacer(1)
        hallway()
        
    elif response == "no":
        spacer(2)
        print ("You head towards the exit.")
        spacer(1)
        hallway()
    else: 
        spacer(2)
        print ("I didn't understand that. Please try the command again. \n") 
        spacer(1)
        bedroom_choice3()

# ROOM THREE - HALLWAY

def hallway():
    print("Entering a dimly lit hallway, you take in your surroudings.")
    spacer(1)
    print("You see 2 doors, the right is closed and the other thrown wide open, from a quick glance it looks to be a surgery room.")
    spacer(3)
    hallwayoptions()

def hallwayoptions():
    response = input("Do you want to go right or left?\n")
    response = response.lower()
    spacer(1)
    if response == "left":
        print("Eager to see if you can arm yourself, you step into the room.")
        spacer(1)
        surgery_room()
    elif response == "right":
        print("The door opens with ease as you step inside.")
        spacer(1)
        morgue()
    else:
        print("I know the hallway is nice but you can't stay here.")
        hallwayoptions()

#ROOM THREE POINT FIVE - SURGERY

def surgery_room():
    surgery_title_art()
    spacer(2)
    attack_scorer()
    print("You find yourself in a cold, barren room.")
    spacer(1)
    print(f"It looks like this was once a surgery, but all that's now left is {bcolors.BOLD}{bcolors.OKYELLOW}blood-stained scrubs{bcolors.ENDC} and chilled tables.")
    surgery_options()

def surgery_options():
    global attack_mod
    global attack_score
    global strength
    global dexterity
    global sanity
    global health
    global response

    spacer(2)    
    print("You can see:")
    print(f"{bcolors.BOLD}{bcolors.OKYELLOW}A pile of bloody scrubs{bcolors.ENDC} to your left.")
    print(f"{bcolors.BOLD}{bcolors.OKYELLOW}A surgeons drawer{bcolors.ENDC} in front of you.")
    print(f"{bcolors.BOLD}{bcolors.OKYELLOW}A door{bcolors.ENDC} to the right.")
    spacer(0.5)
    print("The door is still open behind you.")
    spacer(0.5)
    surgery_choices()

def surgery_choices():
    global response
    global attack_mod
    global sanity
    print("Which direction would you like to go?")
    response = input("Left  |  Right  |  Forward  |  Back  \n")
    response = response.lower()
    if response == "forward" and "scalpel" not in inventory:
        spacer(1)
        print(f"You loot the {bcolors.BOLD}{bcolors.OKYELLOW}surgeons drawer{bcolors.ENDC} and find a {bcolors.BOLD}{bcolors.OKCYAN}scalpel{bcolors.ENDC}.")
        attack_mod += 2 
        inventory.append("scalpel")
        response = input("Left  |  Right  |  Back  \n")
        response = response.lower()
        if response == "left" and "zombie finger" not in inventory:
            spacer(1)
            zombie_scrubs()
        elif response == "right":
            spacer(1)
            print("You walk down a long, winding corridor...")
            morgue()
        elif response == "back":
            spacer(1)
            surgery_choices()
        else:
            surgery_choices()
    elif response == "left" and "zombie finger" not in inventory:
        spacer(1)
        zombie_scrubs()
    elif response == "left" and "zombie finger" in inventory:
        spacer(0.5)
        print("You've done this already, better cheese it in case there's more zombies!")
        sanity -= 1
        sanity_check()
        spacer(1)
        print("The repetition is driving you slowly insane")
        surgery_options()    
    elif response == "right":
        spacer(1)
        print("You walk down a long, winding corridor...")
        morgue()
    elif response == "back":
        spacer(1)
        hallwayoptions()
    else:
        spacer(1)
        print ("I didn't understand that. Please try the command again.")
        response = input("Left  |  Right  |  Forward  |  Back  \n")
        response = response.lower()
        if response == "forward" and "scalpel" not in inventory:
            spacer(1)
            print("You loot the drawer and find a SCALPEL.")
            attack_mod = attack_mod + 2
            inventory.append("scalpel")
            surgery_choices()
        elif response == "left" and "zombie finger" not in inventory:
            spacer(1)
            zombie_scrubs()
        elif response == "forward" and "scalpel" in inventory:
            spacer(0.5)
            print("You've already got the scalpel, get a move on please!")
            sanity -= 1
            sanity_check()
            spacer(1)
            print("The repitition is driving you slowly insane")
            surgery_options()
        elif response == "left" and "zombie finger" in inventory:
            spacer(0.5)
            print("You've done this already, better cheese it in case there's more zombies!")
            sanity -= 1
            sanity_check()
            spacer(1)
            print("The repitition is driving you slowly insane")
            surgery_options()
        elif response == "right":
            spacer(1)
            print("You walk down a long, winding corridor...")
            morgue()
        elif response == "back":
            spacer(1)
            hallwayoptions()
        else:
            surgery_choices()

# ROOM FOUR - MORGUE

def morgue():
    morgue_title_art()
    spacer(1)
    print(f"\n{bcolors.OKBLUE}{username}{bcolors.ENDC}" + " enters the morgue.")
    spacer(1)
    print("'These places are supposed to be clean!'")
    spacer(1)
    print("But there was blood all over the place.")
    spacer(1)
    print("The room had an eerie feel to it.")
    spacer(1)
    print("Not only did it look like a massacre had gone on in here, but it was half ransacked!")
    spacer(1)
    print(f"{bcolors.OKBLUE}{username}{bcolors.ENDC} spots an unopened works {bcolors.BOLD}{bcolors.OKYELLOW}locker{bcolors.ENDC} and an unlocked {bcolors.BOLD}{bcolors.OKYELLOW}freezer drawer{bcolors.ENDC}.")
    spacer(1)
    morgue1()

def morgue1():
    response = input(f"Would you like to look in the {bcolors.BOLD}{bcolors.OKYELLOW}freezer drawer{bcolors.ENDC}? \nYes / No?\n")
    response = response.lower()
    if response == "yes":
        spacer(1)
        print(f"You look inside the {bcolors.BOLD}{bcolors.OKYELLOW}freezer drawer{bcolors.ENDC} to find a frozen body, but this was different.")
        spacer(1)
        print("It would seem that the body had an onset of necrosis, pretty badly.")
        spacer(1)
        print("'I wonder what caused this?'")
        spacer(1)
        morgue2()
    elif response == "no":
        spacer(1)
        print("Maybe it is too much to risk,")
        spacer(1)
        print("You decide to pass on the possible fresh human popsickle.")
        spacer(1)
        morgue2()
    else: 
        spacer(1)
        print ("I didn't understand that. Please try the command again. \n")
        morgue1()

def morgue2():
    response = input(f"Would you like to try your luck with the {bcolors.BOLD}{bcolors.OKYELLOW}locker{bcolors.ENDC} {bcolors.OKBLUE}{username}{bcolors.ENDC}?\nThere could be some really useful items inside. \nYes / No?\n")
    response = response.lower()
    if response == "yes":
        spacer(1)
        print(f"You open the {bcolors.BOLD}{bcolors.OKYELLOW}locker door{bcolors.ENDC} and find a couple of items.")
        spacer(1)
        print(f"There is some sort of {bcolors.BOLD}{bcolors.OKYELLOW}Robotic arm (r){bcolors.ENDC} and what appears to an ancient {bcolors.BOLD}{bcolors.OKYELLOW}Sceptre (s){bcolors.ENDC}")
        spacer(1)
        print("You can only carry one,")
        spacer(1)
        locker_choice()
    elif response == "no":
        spacer(1)
        print(f"I really think you should look in the {bcolors.BOLD}{bcolors.OKYELLOW}locker{bcolors.ENDC}.")
        spacer(1)
        morgue2()
    else: 
        spacer(1)
        print("I didn't understand that. Please try the command again. \n")
        morgue2()

def locker_choice():
    global strength_mod
    global dexterity_mod
    response = input(f"which do you choose?\n{bcolors.BOLD}{bcolors.OKYELLOW}Robotic arm (r){bcolors.ENDC} or {bcolors.BOLD}{bcolors.OKYELLOW}Sceptre (s){bcolors.ENDC}\n")
    response = response.lower()
    if response == "r":
        spacer(1)
        terminatorhand_art()
        spacer(1)
        print("Looks hefty, could be good for swinging?!\nI hope it has a laser weapon!")
        strength_mod += 4
        spacer(0.5)
        print(f"Your strength is now {bcolors.BOLD}{bcolors.OKRED}{strength}{bcolors.ENDC}!")
        spacer(1)
        terminator()
    elif response == "s":
        spacer(1)
        sceptre_art()
        spacer(1)
        print("I'm no doctor, but I bet this will cause some damage! You even feel more nimble")
        dexterity_mod += 4
        spacer(0.5)
        print(f"Your {bcolors.BOLD}{bcolors.OKRED}dexterity{bcolors.ENDC} is now {bcolors.BOLD}{bcolors.OKRED}{dexterity}{bcolors.ENDC}!")
        spacer(1)
        loki()
    else:
        spacer(1)
        print ("I didn't understand that. Please try the command again. \n")
        locker_choice()

def exit():
    print("You cautiously exit the room minding the fridge section on your way out.")
    spacer(1)

# ZOMBIE ATTACK - Plays against attack score, zom's is randomly generated

def zombie_scrubs():
    global attack_mod
    global attack_score
    global strength
    global dexterity
    global sanity
    global health

    print("The pile of bloody scrubs slowly begins to shuffle on the spot...")
    spacer(2)
    print("A half decayed, undead husk is dragging itself out from beneath the piles!")
    zom_attack = random.randint(8, 15)
    if attack_score > zom_attack:
        spacer(0.5)
        print("The zombie mass shuffles towards you...")
        spacer(0.5)
        print("But they're no match for your quick reactions. You easily dispose of them")
        sanity -= 1
        sanity_check()
        health -= 2
        health_check()
        inventory.append("zombie finger")
        print(f"The bugger tried to scratch you! Your health is now {bcolors.BOLD}{bcolors.OKRED}{health}{bcolors.ENDC} and you don't feel so sane anymore...")
        spacer(0.5)
        print("You swiped his at his finger and it broke right off, maybe it will be useful later.")
        spacer(0.5)
        zombiefinger_art()
        spacer(1)
        print("What now zombie killer? That door?")
        response = input("Yes  |  No  \n")
        response = response.lower()

        if response == "yes":
            morgue()
        elif response == "no":
            print("Fine! We'll head back.")
            surgery_choices()
        else:
            print("Sorry, I didn't quite get that? Probably your cowardly voice...")
            print("I'll assume you said head back!")
            surgery_choices()
           
    else:
        print("I don't think you can take that...")
        sanity -= 2
        sanity_check()
        spacer(0.5)
        print("What you saw has scarred you for life though...")
        surgery_choices()

# TERMINATOR PATH

def terminator():
    ("Coming out the morgue you're startled to a stop by the sight of a figure metres away.")
    spacer(2)
    print("They're hard to make out under the flickering fluorescent light but... you think they're a real person!")
    spacer(3)
    print("Thank the Gods, the last thing you need is to come uncomfortably close to another one of those monsters wearing human skin.")
    spacer(4)
    print("So you take cautious steps forward,")
    spacer(3)
    print("Only to freeze up as the figure takes large and steady strides towards you instead.")
    spacer(3)
    print("Getting closer and closer until finally they're close enough that you can see they have... a glowing red eye?")
    spacer(3)
    print(f"{bcolors.OKGREEN}Come with me if you want to live.{bcolors.ENDC}")
    spacer(1)
    print("Despite the promise of living, you are undeniably terrified of this gigantic... man?")
    spacer(2)
    print(f"{bcolors.OKGREEN}I'm a Terminator from the future and your life is important.{bcolors.ENDC}")
    spacer(2)
    print(f"{bcolors.OKGREEN}Firstly, these creatures must be put to an end,{bcolors.ENDC}")
    spacer(1)
    print(f"{bcolors.OKGREEN}I will go to the basement and kill the group in there.{bcolors.ENDC}")
    spacer(2)
    print(f"{bcolors.OKGREEN}The basement is too dangerous for you, grab the key to the chopper and go to the roof.{bcolors.ENDC}")
    spacer(1)
    print(f"{bcolors.OKGREEN}I will find you again, now go.{bcolors.ENDC}")
    spacer(1)
    terminator_run()

def terminator_run():
    spacer(2)
    response = input ("Will you listen to him and get to the chopper?\nYes or No\n")
    response = response.lower()

    if response == "yes":
        spacer(1)
        print ("You grab the helicopter key and go on ahead without The Terminator. Time to find an elevator.")
        spacer(1)
        basement()
    elif response == "no":
        spacer(1)
        print("You decide to stick by The Terminators side and follow him to eradicate the zombies in the basement.")
        spacer(2)
        print("This so called group is actually a horde, soon you're surrounded,")
        spacer(1)
        print("Bullets and blood are flying everywhere,")
        spacer(1)
        print("You make a valiant effort but soon enough a zombie latches onto your neck.")
        spacer(1)
        print("                             Survival tip - You won't be back!")
        gameover_screen_fail()
    else:
        spacer(1)
        print("Despite being a robot from the future even The Terminator can not understand the language you just spoke. Give it another try.")
        spacer(1)
        terminator_run()

# LOKI PATH

def loki():
    print("Coming out the morgue you're startled to a stop by the sight of a figure metres away.")
    spacer(2)
    print("They're hard to make out under the flickering fluorescent light but... you think they're a real person!")
    spacer(3)
    print("Thank the Gods, the last thing you need is to come uncomfortably close to another one of those monsters wearing human skin.")
    spacer(3)
    print("So you take cautious steps forward,")
    spacer(2)
    print("Only to freeze up as the figure takes large and steady strides towards you instead.")
    spacer(2)
    print("Getting closer and closer until finally they're close enough that you can see they're wearing a... cape!?")
    spacer(2)

    print(f"{bcolors.OKGREEN}You're saviour is heeeere!{bcolors.ENDC}")
    spacer(3)
    print("Beyond just how absurd this person looks, you can't deny it look suits them well.")
    spacer(2)
    print(f"{bcolors.OKGREEN}I am Loki, God of Mischief and I have a glorious plan!{bcolors.ENDC}")
    spacer(2)
    print(f"{bcolors.OKGREEN}So listen up mortal{bcolors.ENDC}")
    spacer(2)

    print(f"{bcolors.OKGREEN}I say we, and by we I mean YOU. Go investigate what's in the basement over there while I go check out the security room. {bcolors.ENDC}")
    spacer(2)
    print("You could listen to him, however you do see a helicoptor key hanging up on the wall... could be a good idea check the roof.")
    spacer(4)
    loki_run()

def loki_run():
    spacer(1)
    print("Do you trust Loki?")
    response = input("Yes | No \n")
    response = response.lower()
    if response == "yes":
        spacer(0.5)
        print ("You listen and go ahead without Loki to search the basement. You hear groaning behind the door.")
        spacer(1)
        print("Stupidly, you decide to go inside.")
        spacer(1)
        print("As soon as the door opens, you're attacked by a group of zombies and your buried under the pile.")
        spacer(1)
        print("Being devoured alive...")
        spacer(1)
        print("Survival tip: Never trust the GOD OF MISCHIEF!")
        spacer(3)
        gameover_screen()
    elif response == "no":
        spacer(0.5)
        print("You decide not to trust the God of Mischief and grab the helicoptor key, intent on getting to the roof.")
        spacer(1)
        basement()
    else:
        spacer(0.5)
        print("You must give the God a clear answer.")
        spacer(1)
        loki_run()

# ROOM SIX - Elevator Puzzle

def basement():
    basement_title_art()
    spacer
    print("You find yourself in a dark, dingy basement.")
    spacer(0.5)
    print("You can hear the sounds of zombies all around...")
    spacer(1)
    print("Quick! What's that in front of you?!")
    number_puzzle()

def number_puzzle():
    global sanity
    global strength_mod
    global dexterity_mod
    global charisma_mod

    print("In front of you is a lock to the elevator.")
    spacer(5)
    lockclosed_image()
    spacer(2)
    print("Attached to it is a clue on how to get through...")
    spacer(5)
    clear_screen()

    print("  | 6 | 8 | 2 |      |     | 6 | 4 | 5 |      |     | 2 | 0 | 6 |           ")
    print("   ONE number is     |     ONE number is      |     TWO numbers are         ")
    print("correct and properly |  correct, but placed   |   correct, but placed       ")
    print("       placed.       |        wrong.          |          wrong.             ")
    print("                                                                            ")
    print("             | 7 | 3 | 8 |     |   | 7 | 8 | 0 |                            ")
    print("          NOTHING is correct   |   ONE number is                            ")
    print("                               | correct, but placed                        ")
    print("                               |       wrong.                               ")
    print("                                                                            ")
    print("                                                                            ")
    print("                                                                            ")
    print("                      THREE DIGIT NUMBERS ONLY                              ")
    print("                      DRIVES YOU SLOWLY INSANE                              ")
    print("                             BE CAREFUL!                                    ")
    print("                                                                            ")

    spacer(3)
    print("You could probably solve that...")
    spacer(2)
    puzzle_choices()

def puzzle_choices():
    global sanity
    global health
    global inventory
    
    print("What do you want to do?")
    spacer(1)
    puzzle_choice = input("""
    Solve the Puzzle (A)
    Rip off the lock (B)
    Check out that Thumb Scanner (C)
    Pick the lock (D)
    """)
    puzzle_choice = puzzle_choice.lower()

    if puzzle_choice == "a":
        print("OK then hot shot, give it a go!")
        spacer(0.5)
        puzzle_answer = input(str("Key in a three digit number, or say BACK: \n"))
        puzzle_answer = puzzle_answer.lower()
        if puzzle_answer == "052":
            spacer(2)
            lock_animation()
            print("BLOODY HELL! That's the one, let's get out of here")
            rooftop()
        elif len(puzzle_answer) != 3:
            spacer(0.5)
            print("I SAID THREE DIGITS! This is driving me crazy.")
            sanity -= 1
            sanity_check()
            spacer(0.5)
            print(f"Your {bcolors.BOLD}{bcolors.OKRED}sanity{bcolors.ENDC} is now {bcolors.BOLD}{bcolors.OKRED}{sanity}{bcolors.ENDC}!")
            puzzle_choices()
        elif puzzle_answer == "back":
            spacer(0.5)
            print("OK then...")
            spacer(1)
            number_puzzle()
        else:
            spacer(0.5)
            print("Try again")
            spacer(1)
            puzzle_answer = input(str("Key in a three digit number: \n"))
            if puzzle_answer == "052":
                spacer(2)
                lock_animation()
                print("BLOODY HELL! That's the one, let's get out of here")
                rooftop()
            elif len(puzzle_choice) != 3:
                spacer(0.5)
                print("I SAID THREE DIGITS! This is driving me crazy.")
                sanity -= 1
                sanity_check()
                print(f"Your {bcolors.BOLD}{bcolors.OKRED}sanity{bcolors.ENDC} is now {bcolors.BOLD}{bcolors.OKRED}{sanity}{bcolors.ENDC}!")
                puzzle_choices()
            elif puzzle_answer == "back":
                spacer(0.5)
                print("OK then...")
                spacer(1)
                number_puzzle()
            else:
                spacer(0.5)
                print("You're not getting this!")
                sanity -= 2
                sanity_check()
                spacer(0.5)
                print(f"I hope you know how much this is effecting your {bcolors.BOLD}{bcolors.OKRED}sanity{bcolors.ENDC}!")
                puzzle_choices()
    elif puzzle_choice == "b" and "terminator hand" not in inventory:
        print(f"If you're sure, this will take a lot of {bcolors.BOLD}{bcolors.OKRED}strength{bcolors.ENDC} though")
        spacer(1)
        print("Rolling your strength check...")
        hard_skill(strength_mod)

        if skill_check == True:
            spacer(3)
            print("YOU'VE RIPPED IT RIGHT OFF THE HOLDER")
            spacer(1)
            print("Let's Go!")
            rooftop()
        else:
            spacer(3)
            print("Well you've messed that up.")
            spacer(0.5)
            print("You've even cut your hand")
            health -= 2
            health_check()
            sanity -= 1
            sanity_check()
            spacer(0.5)
            print(f"Your health is now {bcolors.BOLD}{bcolors.OKRED}{health}{bcolors.ENDC}HP! Your sanity is {bcolors.BOLD}{bcolors.OKRED}{sanity}{bcolors.ENDC}!")
            puzzle_choices()
    elif puzzle_choice == "b" and "terminator hand" in inventory:
        print(f"If you're sure, this will take a lot of {bcolors.BOLD}{bcolors.OKRED}strength{bcolors.ENDC} though")
        spacer(1)
        print("That Terminator hand you found should give you a bonus though!")
        spacer(1)
        print(f"Rolling your {bcolors.BOLD}{bcolors.OKRED}strength{bcolors.ENDC} check...")
        hard_skill(strength_mod)

        if skill_check == True:
            spacer(3)
            print("YOU'VE RIPPED IT RIGHT OFF THE HOLDER")
            spacer(1)
            print("Let's Go!")
            spacer(1)
            rooftop()
        else:
            spacer(3)
            print("Well you've messed that up.")
            spacer(0.5)
            print("You've even cut your hand")
            health -= 2
            health_check()
            sanity -= 1
            sanity_check()
            spacer(0.5)
            print(f"Your {bcolors.BOLD}{bcolors.HEADER}health{bcolors.ENDC} is now {bcolors.BOLD}{bcolors.OKRED}{health}{bcolors.ENDC}HP! Your {bcolors.BOLD}{bcolors.OKRED}sanity{bcolors.ENDC} is {bcolors.BOLD}{bcolors.OKRED}{sanity}{bcolors.ENDC}!")
            puzzle_choices()
    elif puzzle_choice == "c" and "zombie finger" in inventory:
        spacer(3)
        print("It looks like this needs the fingerprint of an employee...")
        spacer(0.5)
        print("Let's see if that finger you swiped earlier does anything...")
        spacer(1)
        zombiefinger_art()
        spacer(2.5)
        clear_screen()
        scanning_art()
        spacer(1)
        scanning_art()
        spacer(1)
        scanning_art()
        spacer(5)            
        clear_screen()
        success_art()
        spacer(1)
        print("It's unlocked! Let's go!")
        rooftop()
    elif puzzle_choice == "c" and "zombie_finger" not in inventory:
        spacer(3)
        print("It looks like this needs the fingerprint of an employee...")
        spacer(1)
        print("Shame you don't have anything like that...")
        spacer(0.5)
        puzzle_choices()
    
    elif puzzle_choice == "d" and "scalpel" in inventory:
        spacer(3)
        print(f"It will take a little {bcolors.BOLD}{bcolors.OKRED}dexterity{bcolors.ENDC}, but that {bcolors.BOLD}{bcolors.OKCYAN}scalpel{bcolors.ENDC} should help.")
        spacer(1)
        print("Rolling your dexterity check...")
        med_skill(dexterity_mod)
        if skill_check == True:
            spacer(0.5)
            print("Come on...")
            spacer(1)
            print("Nearly got it...")
            spacer(2)
            print("YOU DID IT! Let's go!")
            rooftop()
        else:
            spacer(2)
            print("Nice try, but you've messed it up.")
            spacer(0.5)
            health -= 2
            health_check()
            print(f"You've even managed to knick your finger, your {bcolors.BOLD}{bcolors.HEADER}health{bcolors.ENDC} is now {bcolors.BOLD}{bcolors.OKRED}{health}{bcolors.ENDC}HP!")
            sanity -= 1
            sanity_check()
            print(f"It's also driving you insane. Your {bcolors.BOLD}{bcolors.OKRED}sanity{bcolors.ENDC} is now {bcolors.BOLD}{bcolors.OKRED}{sanity}{bcolors.ENDC}!")
            puzzle_choices()
    elif puzzle_choice == "d" and "scalpel" not in inventory:
        spacer(3)
        print(f"It will take a little {bcolors.BOLD}{bcolors.OKRED}dexterity{bcolors.ENDC}.")
        spacer(1)
        print("Rolling your dexterity check...")
        med_skill(dexterity_mod)
        if skill_check == True:
            spacer(0.5)
            print("Come on...")
            spacer(1)
            print("Nearly got it...")
            spacer(2)
            print("YOU DID IT! Let's go!")
            rooftop()
        else:
            spacer(2)
            print("Nice try, but you've messed it up.")
            spacer(0.5)
            health -= 2
            health_check()
            print(f"You've even managed to knick your finger, your {bcolors.BOLD}{bcolors.HEADER}health{bcolors.ENDC} is now {bcolors.BOLD}{bcolors.OKRED}{health}{bcolors.ENDC}HP!")
            sanity -= 1
            sanity_check()
            print(f"It's also driving you insane. Your {bcolors.BOLD}{bcolors.OKRED}sanity{bcolors.ENDC} is now {bcolors.BOLD}{bcolors.OKRED}{sanity}{bcolors.ENDC}!")
            puzzle_choices()
    else:
        spacer(1)
        print("Now's not the time to waste time...")
        spacer(0.5)
        health -= 3
        health_check()
        sanity -=2
        sanity_check()
        print(f"Your {bcolors.BOLD}{bcolors.HEADER}health{bcolors.ENDC} is now {bcolors.BOLD}{bcolors.OKRED}{health}{bcolors.ENDC}HP with a {bcolors.BOLD}{bcolors.OKRED}sanity{bcolors.ENDC} of {bcolors.BOLD}{bcolors.OKRED}{sanity}{bcolors.ENDC}! Stop messing about!")
        spacer(0.5)
        puzzle_choices()

def rooftop():
    global health
    global sanity
    print("YOU WIN!")
    spacer(1)
    clear_screen()
    gamewin_art()
    spacer(2)
    print(f"You finished with {health}HP and {sanity} points")
    gamewin_screen()

intro()