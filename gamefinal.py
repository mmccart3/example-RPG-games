from random import choice, shuffle, randint
from time import sleep
from colorama import Fore, Back, Style
from os import system, name
from sys import stdout

dave = {
    "coins": 0,
    "tankard": "A hefty steel cup",
    "broadsword": "Actually just a wide dagger"
}

flags = {
    "Room0_Items_Obtainable": 0,
    "room0_coins_get": 0,
    "trap": False
}

def list_stuff(stuff):
    for it in stuff:
        print(f"you can see a {it}")
def list_inv(stuff):
    for it in stuff:
        if it == "coins":
            print(f"you have {dave.get("coins")} {it} in your inventory ")
        else:
            print(f"you have a '{it}' in your inventory. It's {stuff.get(it)}")


#---------------------------------------------------------------------

def Intro ():
    print
    print ("His eyes closed, he feels a chill breeze brush across his face")
    sleep(2)
    print("how unusual I dont normally sleep with the window ajar""he thought to himself")
    sleep(2)
    print("He rolls to the side feeling a different sort of cold, it was hard and damp, certainly not the comfort of his bed.")
    sleep(1)
    print("Opening his eyes he finally notices")
    sleep(2)
    print("Indeed, twas not his bed, nor his abode. it appeared to be a dimly lit cavern of sorts")
    sleep(2)
    print("Looking around himself he finds only a large empty tankard and a coinpurse bereft of contents...")
    sleep(2)
    print("AAAH! he remembers!"
          "the 15 hour gamble and drinkathon down at the local tavern the night before..at least he hopes it was the night before. Ordering his first pint was the last thing he could remember, even his name was Escaping him")
    input("what was your name again?")
    print ("No, no that wasnt it...")
    input("It was?...")
    print("No that still doesnt sound right..")
    sleep(2)
    print ("...")
    sleep (1)
    print("Sod it,'Dave' will do")

#-----------------------------------------------------------------------------


# dave = {
#     "coins": 0,
#     "TANKARD": "A hefty steel cup"
# }
# ==================================================Intro Room=====================================================
def Room_0():
    
    def Options():
        # print(flags)
        # print(dave)
        Player_input = input("Options:|Look|Use|Take|Talk|:").strip().upper()
        if Player_input=="LOOK":
            Look()
        elif Player_input=="USE":
            Use()
        elif Player_input=="TAKE":
            Take()
        elif Player_input=="TALK":
            print("with no one else around Dave has a riveting conversation with himself")
            Options()
        else:
            print("Invalid action")
            return(Options())

    def room_description():
        print("Looking around the room, Dave spots a large hole in the centre of the ceiling, likely the entrance he utilised. From it there appears to be a rope dangling just above head height and looped through a pully with a bucket attatched at the very top")
        
        print ("It's a mirracle Dave fell down here without getting hurt, but then where there's no sense there is no feeling, as they say")
        sleep(1)
        print ("On further observation there seems to be a pile of rubble in the south eastern corner of this dank place and Dave being the magpie like fellow he is quickly spots the shimmer of coin jutting from underneath some of the mislayed bricks")
        Options()
    def Look():
         Look = input("look at what?:").strip().upper()
         if Look == "ROOM":
             room_description()
         else:
             print ("Gawk at that all you like, it's not going to get you anywhere")
             return(Options())
    def Use():
        list_inv(dave)
        print("You can also try the 'rubble' or the 'rope' if you feel brave I guess")
        Use = input("Use what?").strip().upper()
        if Use == ("ROPE"):
            if flags.get("rope_break")!= None:
                print("You can't reach the part that it snapped off Dave, come on now.")
                Options()
            else:
                # print(flags.get("Room0_Items_Obtainable"))
                flags.update({"Room0_Items_Obtainable": 1})
                # print(flags.get("Room0_Items_Obtainable"))
                print("Tightly grasping the rope, Dave endeavors to hoist himself whence he came. Unfortunately years of wear and tear along with the additional weight of Dave and his obtuse gut, were too much for the rope. It snaps, dropping Dave on his behind, itself on the floor and its' associated bucket narrowly misses Dave's head as it crashes to the ground, causing it's flimsy wire handle to fall off")
                flags.update({"rope_break": True})
                Options()
        elif Use == ("RUBBLE"):
            if flags.get("room0_coins_get") == 0:
                print(f"Dave begins to dig through the rock and rubble, revealing a short tunnel that seems to lead to another room, not forgetting to greedily pocket the Coins he uncovered in the process, he proceeds on through")
                dave.update({"coins":dave.get("coins")+3})
                flags.update({"room0_coins_get": 1})
                room_02()
            else:
                print("Dave goes back through the tunnel")
                room_02()
        else:
            print("And how are you going to 'Use' that exactly?..no don't bother telling me, try something else")
            return(Options())
    def Take():
        Take = input ("Take what?").strip().upper()
        for items in dave:
         print(items)
         if Take == items:
          print("You already have that")
          return Options()
        if Take == ("BUCKET") and (flags.get("Room0_Items_Obtainable")==1):
            dave.update({"BUCKET":"Wooden bucket from the well"})
            print ("Bucket added to Inventory")
            Options()
        elif Take == ("BUCKET") and (flags.get("Room0_Items_Obtainable")==0):
            print ("that's far too high to reach right now")
            return (Options())
        elif Take ==("ROPE")and (flags.get("Room0_Items_Obtainable")==1):
            dave.update({"rope":"a frayed length of rope from the well"})
            print ("Rope added to Inventory")
            Options()
        elif Take == ("ROPE") and (flags.get("Room0_Items_Obtainable")==0):
            print ("It seems to be fixed in place")
            return (Options())
        elif Take == ("HANDLE")and (flags.get("Room0_Items_Obtainable")==1):
            dave.update({"HANDLE":"A thick length of wire once attatched a bucket"})
            print ("Wire Handle added to Inventory")
            Options()
        elif Take == ("HANDLE") and (flags.get("Room0_Items_Obtainable")==0):
            print ("and how exactly do you plan to reach that?")
            return (Options())
        else:
            print ("I don't know what bright idea you think you have trying this Dave, but this isn't it")
            return(Options())
    room_description()
    Options()
    # =====================================Room 0 ===========================================================
# ==================================================Intro Room=====================================================
def room_02():
    look_list= {
            "'drain' in the middle of the floor": "Looks like there's something at the bottom of it",
            "'wooden door' on the northern wall": "This door is locked, you swear you can hear something brushing behind it",
            "'metal door' on the right": "Another locked door, this one has horns",
            "'wooden box' by the wooden door": "it's full of hooks and not the musical kind",
            "recently dug 'tunnel' on the west wall": "Your great escape Dave, no point going back"
        }
    take_list = {

    }



    if dave.get("barrel_key") != None:
        look_list.update({"drain in the middle of the floor": "it's the drain you fished the key out of"})
    if dave.get("larder_unlock")!= None:
        look_list.update({"wooden door on the northern wall": "The door to the larder, you can still hear the broom working away"})
    if dave.get("goat_unlock")!= None:
        look_list.update({"'metal door' on the right": "The door you had to charm a broom to get through"})


    def list_stuff(stuff):
        for it in stuff:
            print(f"you can see a {it}")
    def list_inv(stuff):
        for it in stuff:
            if it == "coins":
                print(f"you have {dave.get("coins")} {it} in your inventory ")
            else:
                print(f"you have a '{it}' in your inventory. It's {stuff.get(it)}")

    def options():
        print("You're in a dank room with a drain in the middle")
        leprechaun()
        player_input = input(f"Options look|use|take|talk|tunnel|{'wooden door|' * bool(flags.get("larder_unlock"))}{'metal door' * bool(flags.get("goat_unlock"))} ").strip().lower()  
        if player_input=="look":
            look(look_list)
            options()
        elif player_input=="use":
            use(dave)
            options()
        elif player_input=="take":
            take(take_list)
            options()
        elif player_input=="talk":
            talk()
            options()
        elif player_input == "wooden door":
            if flags.get("larder_unlock"):
                larder_intro()
            else: 
                print("The doors locked Dave")

        elif player_input == "metal door":
            if flags.get("goat_unlock"):
                maze_room()
            else: 
                print("The doors locked Dave")
        elif player_input == "tunnel":
            Room_0()
        else:
            print("Invalid action")
            options()

    def look(stuff):
        print("You can see")
        list_stuff(stuff)
        player_input = input("So what are we looking at Dave? ").strip().lower()
        match player_input:
            case "drain":
                print(stuff.get("'drain' in the middle of the floor"))
            case "wooden door":
                print(stuff.get("'wooden door' on the northern wall"))
            case "metal door":
                print(stuff.get("'metal door' on the right"))
            case "tunnel":
                print(stuff.get("recently dug 'tunnel' on the west wall"))
            case "wooden box":
                if dave.get("hook")!= None:
                    print("The box you where you stole the hook from it's family")
                else:
                    print(stuff.get("'wooden box' by the wooden door"))
                    look_list.update({"'hook'": "Perfect for fishing." })
                    take_list.update({"'hook'": "Perfect for fishing." })
            case "back":
                options()
            case _:
                print("remember to enter anything between the ' ' marks dave or 'back' to go back")

    def take(take_list):#
        if len(take_list) == 0:
            print("Theres nothing to take, Dave")
            options()
        list_stuff(take_list)
        player_input = input("So what are we taking Dave? ").strip().lower()
        match player_input:
            case "hook":
                if dave.get("hook")!= None:
                    print("You already seperated one hook, best not do it again")
                else:
                    print("You take the hook")
                    dave.update({"hook": "Kinda dangerous being in your pants" })
            case "back":
                options()
            case _:
                print("remember to enter anything between the ' ' marks dave or 'back' to go back")

    def use(dave):
        print(dave)
        list_inv(dave)
        player_input = input("So what are we using Dave? ").strip().lower()
        print(f"player input {player_input}")
        match player_input:
            case "rope":
                if dave.get("rope"):
                    sec_input = input("Using a rope by itself on the drain wont work, what should we use with it Dave? ")
                    if sec_input == "hook":
                        if dave.get("hook") == None:
                            print("You don't have a hook")
                            use(dave)
                        else:
                            print("After a good minute, you get a bite and reel in the key, However your rope is rendered useless in the process")
                            dave.update({"barrel key": "An ordinary key. The end has a barrel carved on it"})
                            print("Key pocketed")
                            options()
                else:
                    print("You don't have the rope anymore")
                    use(dave)
            case "hook":
                if dave.get("hook") == None:
                    print("You don't have a hook")
                    use(dave)
                sec_input = ("Using a hook by itself on the drain wont work, what should we use with it Dave? ")
                if sec_input == "'rope'":
                    print("After a good minute, you get a bite and reel in the key, However your rope is rendered useless in the process")
                    dave.update({"barrel key": "An ordinary key. The end has a barrel carved on it"})
                    print("Key pocketed")
                    dave.pop("rope")
                    options()
            case "barrel key":
                print("You try the key on both doors, the wooden one unlocks first while the metal door refuses your tribute.")
                flags.update({"larder_unlock": True})
            case "horned key":
                print("You unlock the intimidating looking door")
                flags.update({"goat_unlock": True})
            case "back":
                options()
            case _:
                print("that wont work Dave")
    def talk():
        print("There's nothing to talk to in here Dave!")
        options()

    def leprechaun():
            # leprechaun = ["Coins for a random clue", "Coins for help with a puzzle", "Coins for a special item" ]
            # option_1 = print("Find and press the buttom on the wall to receive bonus coins") # By pressing the button, removes an item from player.
            # option_2 = print("Solve the riddle to double your coins for the next puzzle") # Get zero coins for the next puzzle.
            # option_3 = print("solve three bonus ridddles for an extra life") # Steals 5 coins from the player.
            # option_4 = print("How about a trade, coins for clues")

        small_guy = randint(1, 4)
        # print(small_guy)
        if small_guy == 3 and flags.get("trap") == False:
                # random_leprechaun = choice(leprechaun)
            print(f"Daves leg catches a snare hoisting him upside down in the room")
            print("After only a few minutes of hanging, a haughty small man smaller than a gnome comes skipping by.")
            print(f"Option one! Solve the riddle to double your coins for the next puzzle")
            print(f"Option two! solve three bonus ridddles for an extra life")
            print(f"Option three! How about a trade, coins for clues")
            player_input= input("So Dave, which option is it going to be? one, two or three?").strip().lower()
            match player_input:
                case "one":
                    print("The small man hits you with a barrage of words you don't understand, as you attempt an answer he cuts you loose, after helping himself to a coin")
                    dave.update({"coins": dave.get("coins") -1})
                    flags.update({"leprechaun": True})
                case "two":
                    print("Luckily, You're able to answer all his riddles, oathbound, he frees you.")
                    flags.update({"leprechaun": True})
                case "three": 
                     print("The man helps himself to coin coins, cutting you loose as he idly comments I heard the broom likes the alphabet")
                     flags.update({"leprechaun": True})
                case _:
                    print("Something broke")        
        else:
            return

    options()

# =====================================Drain Room================================================
# =====================================Larder====================================================

def larder_intro():
    def list_sacks(sacks):
        for x in sacks:
            print(f"a {sacks.get(x)}")
    def shelf_arrange(player_shelf, shelf2):
        print(shelf2)
        solution = ["smelly", "small", "light", "heavy"]
        if len(player_shelf) == 4 and player_shelf != solution: 
            print("The broom disaproves of the order you've organised and sweeps everything back to the floor")
        elif len(player_shelf) == 4 and player_shelf == solution:
            print("Moved by your piety towards order, The broom bestows upon you a boon or some sorts. A metal  key and a shiny coin!")
            print("Coin pocketed")
            dave.update({"coins": dave.get("coins") +1})
            dave.update({"horned key": "I could make a funny joke here but I wont"})
            flags.update({"larder_solved": True})
            larder_intro()
        else:
            print(player_shelf)
            print(len(player_shelf))
            while len(player_shelf) != 4:
                list_sacks(shelf2)
                shelf_choice = input("Which bag are you putting on the shelf ").lower()
                if shelf_choice == "heavy" or  shelf_choice == "wheat":
                    player_shelf.append("heavy")
                    shelf2.pop("heavy")
                    shelf_arrange(player_shelf, shelf2)
                elif shelf_choice == "light" or shelf_choice == "onions":
                    player_shelf.append("light")
                    shelf2.pop("light")
                    shelf_arrange(player_shelf, shelf2)
                elif shelf_choice == "small" or  shelf_choice == "pork" or shelf_choice == "pork scratchings":
                    player_shelf.append("small")
                    shelf2.pop("small")
                    shelf_arrange(player_shelf, shelf2)
                elif shelf_choice == "smelly" or shelf_choice == "apple":
                    player_shelf.append("smelly")
                    shelf2.pop("smelly")
                    shelf_arrange(player_shelf, shelf2)
                else:
                    print("Pick it by the contents or adjective, dave")
                    print("reset")
                    shelf_arrange(player_shelf, shelf2)


    larder_sacks = {
        "heavy": "heavy sack", 
        "light": "light sack",
        "small": "small bag",
        "smelly": "smelly pouch"
    }
    look_list = {
        "bag of 'oats'": "How Nutty, you should take some",
        "bag of 'coffee'": "The saviour of many last minute projects",
        "animate 'broom'": "It's humming a copyrighted tune",
        "'wooden door'": "The door you came through"

    }

    take_list = {

    }
    if(flags.get("broken_broom")) == True:
       print("You step into a rather disorganised larder with with the remains of a broom scattered about") 
    else:
        print("You step into a rather disorganised larder with a broom sweeping about")
    def options():
        print("You're in a dusty Larder, there's a broom sweeping about")
        player_input = input(f"Options look|use|take|talk|wooden door")
        if player_input=="look":
            look(look_list)
            options()
        elif player_input=="use":
            use(dave)
            options()
        elif player_input=="take":
            take(take_list)
            options()
        elif player_input=="talk":
            talk(larder_sacks)
            options()
        elif player_input == "wooden door":
            room_02()
        else:
            print("Invalid action Dave")
            options()

    def list_stuff(stuff):
        for it in stuff:
            print(f"you can see a {it}")
    def list_inv(stuff):
        for it in stuff:
            if it == "coins":
                print(f"you have {dave.get("coins")} {it} in your inventory ")
            else:
                print(f"you have a '{it}' in your inventory. It's {stuff.get(it)}")

    def look(stuff):
        print("You can see")
        list_stuff(stuff)
        player_input = input("So what are we looking at Dave? ").strip().lower()
        match player_input:
            case "oats":
                if dave.get("oats")!= None:
                    print("A half full sack of oats")
                else:
                    print(stuff.get("bag of 'oats'"))
                    take_list.update({"bag of 'oats'": "Very Oaty"})
            case "wooden door":
                print(stuff.get("'wooden door' on the northern wall"))
            case "coffee":
                if dave.get("coffee")!= None:
                    print("The bag of beans your belligerently burgled")
                else:
                    print(stuff.get("bag of 'coffee'"))
                    take_list.update({"coffee bag": "You hope this is legal"}) 
            case "broom":
                print(stuff.get("animate 'broom'"))
            case "back":
                options()
            case _:
                print("remember to enter anything between the ' ' marks dave or 'back' to go back")

    def take(take_list):#
        if len(take_list) == 0:
            print("Theres nothing to take, Dave")
            options()
        print("You can take")
        list_stuff(take_list)
        player_input = input("So what are we taking Dave? ").strip().lower()
        match player_input:
            case "oats":
                if dave.get("oats")!= None:
                    print("You already have some oats Dave")
                else:
                    print("You pocket some oats")
                    dave.update({"oats": "A handful of oats line your pockets" })
            case "oats":
                if dave.get("coffee")!= None:
                    print("You took the coffee Dave, leave some for the rest of us")
                else:
                    print("You pocket the brain fuel")
                    dave.update({"coffee": "You hope this is legal." })
            case "back":
                options()
            case _:
                print("remember to enter anything between the ' ' marks dave or 'back' to go back")

    def use(dave):
        print(dave)
        list_inv(dave)
        player_input = input("So what are we using Dave? ").strip().lower()
        print(f"player input {player_input}")
        match player_input:
            case "broadsword":
                if flags.get("larder_solved") == True:
                    print("It looks too happy to put down now")
                else:
                    print("Tired of this brooms mockery of life you take your sword and reutrn it to firewood")
                    print("On closer inspection of the lumber you find a metal key with horns carved on the end")
                    dave.update({"horned key": "I could make a funny joke here but I wont"})
                    flags.update({"broken_broom": True})
            case _:
                print("that wont work here Dave")

    def talk(larder_sacks):
        if(flags.get("larder_solved"))!= None:
            print("The broom is on break and does not wish to chat")
            options()
        elif(flags.get("broken_broom")) != None:
            print("You can't really talk to kindling, can you dave?")
            options()
        print("Thankfully you took a night class in inanimate object and speak a bit of broom")
        print("It seems to be asking you to help organise a shelf promising a reward in the end")
        player_input = input("Well Dave, are we helping the broom? Im sure we could cut right to the end if we think hard enough, yes or no should we help this broom?")
        if player_input == "yes":
            larder_puzzle(larder_sacks)
        elif player_input == "no":
            print("You leave the broom to it's musings")
            options()
        else: 
            print("yes or no Dave")
    
    # print("The broom wants them in a particular order Dave.")
    # larder_puzzle(larder_sacks)
    
    def larder_puzzle(larder_sacks):
        print("The broom shuffles leads you to four items on the floor it wants organised in order")
        list_sacks(larder_sacks)
        shelf2 = larder_sacks.copy()
        player_shelf = []
        player_input =  input(("Shall we 'arrange' the bags or have a quick 'search' first?: or just 'leave'? ")).lower()
        while True:
            match player_input:
                case "search":
                    larder_sacks.update({"heavy": "heavy sack of wheat"})
                    larder_sacks.update({"light": "light sack of onions"})
                    larder_sacks.update({"small": "small bag of pork scratchings"})
                    larder_sacks.update({"smelly": "smelly pouch of overripe apple"})
                    print("Searching the sacks reveals their mysteries to you Dave")
                    list_sacks(shelf2)
                    print(larder_sacks)
                    larder_puzzle(larder_sacks)
                    break
                case "arrange":
                    shelf_arrange(player_shelf, shelf2)
                    larder_puzzle(larder_sacks)
                case "leave": 
                    larder_intro()
                case _:
                    print("That doesn't make sense dave")
                    larder_puzzle(larder_sacks)






        # def larder_solved():
        #     while True:
        #         print("Not much here yet, just a dilligent brush")
        #         input("Options |Look|Take|Use|")
        #         input("Placeholder room, if you see this ctrl c out the terminal")


            # def shelf_edit(player_shelf, shelf_choice,shelf2):
            #     player_shelf.append(shelf_choice)
            #     shelf2.pop(shelf_choice)
        

    options()
# ================================================Larder==================================================================
# ================================================Maze===================================================================

def maze_room():
    print("Dave passes the metal door and comes upon a porticullus, the Wall has some sort of demon etched into the side")
    print("""            
                                                        
                                         &              
              &&                       &&&              
              & &                      & &              
              &  &                    && &              
              && &&                   &  &              
              &&  &                  &&  &              
              &   &                  &   &              
              &   &                  &   &              
              &   &                  &   &              
             &&   &   &&&&&    &&&& &&   &              
             &    &&&              &&    &              
              &    &&   &&&&&&&&  &&    &&              
              &&     &&         &&     &&&              
             &  &     &&       &      &   &             
            &  &&&&     &           &&  &&&&&&          
           &&&   &&&              &  &        &&        
        &&&      &&                   &     &&          
        &&&    &&&                    &&&&& &&          
           &&&   &&&&&            &&&&       &&         
          &       && &            & &&&       &         
         &&       & &&            &&& &       &&        
         &        &     &     &      &&        &        
         &        &&    &     &     &&         &        
         &          &&  &     &   &&          &&        
         &&          &   &   &   &&           &         
           &&         &  &      &&           &          
           &&&&       &&        &&          &           
           &&    &&&&&&& &   &  &          &&           
            &   &    &&&&&& &&&&&&         &&           
            &  &     &  &  &&  &  &        &            
            & &      &  &      &  &&       &            
            &&&      &  &      &   &       &            
            &&       &   &     &   &&     &&            
              &      &    &   &&    &     &             
              &     &&    & && &   &&     &             
              &     &&&   &    &  & &     &             
              &&   &  &  &&    &  & &     &             
               &   &  && &&    &  & &    &&             
               &  &&  && &     &  &&&    &              
              &&&&&   &&&&       & &&    &              
              &    &               &     &              
              &    &               &    &&              
              &&& &&               &&   &               
                                    &  &                
                                   &&&&&&               
                                   &    &               
                                   &&   &               
                                    &&&                 
                                                        
                                                        
                                                        
                                                        
          """)
    print("Those who enter the maze may find great riches or be lost forever")
    print("We are also legally obligated to offer you the chance to skip the maze")
    print("On the opposite wall is a dark passage and a sign offering greater riches than the smelly old maze")
    player_input =  input("Well Dave? are we going to 'enter', 'skip' 'back' or are we going down that 'passage' out?")
    match player_input:
        case "enter":
            maze_start()
        case "skip": 
            maze_beaten()
        case "back":
            print("room2 goes here")
        case "passage":
            tot()
        case _:
            print("Cmon Dave, enter, skip, back or passage")
            maze_room()


def maze_start():
    dave.setdefault("pos", 3)
    dave.setdefault("direction", "north")
    

    def direction_check(facing, going):
        cardinals = ["north", "east", "south", "west"]
        match going:
            case "left":
                return cardinals[cardinals.index(facing)-1]
            case "right":
                if facing == "west":
                    return cardinals[0]
                else:
                    return cardinals[cardinals.index(facing)+1]
            case "back":
                match facing:
                    case "north":
                        facing = "south"
                    case "south":
                        facing = "north"
                    case "west":
                        facing = "east"
                    case "east": 
                        facing = "west"
        return facing
    def move_text(text):
        print(f"you move {text}")
    def wall_bump():
        print("You bump into a wall")
    def room_check(pos, facing):
        # print(pos)
        # print(f"Daves position is {pos} and is facing {facing}")
        if pos == 3:
            maze_entrance(pos, facing)
        elif pos == 13:
            lever_room(pos, facing)
        elif pos == 11 or pos == 12 or pos == 14 or pos == 20 or pos == 25 or pos == 42 or pos == 46 or pos == 54:
            hallway(pos, facing)
        elif pos == 10 or pos == 50:
            corner_room_ll(pos, facing)
        elif pos == 30 or pos == 35:
            corner_room_lu(pos, facing)
        elif pos == 15 or pos == 31 or pos == 36 or pos == 44:
            corner_room_ru(pos, facing)
        elif pos == 51 or pos == 64:
            corner_room_rr(pos, facing)
        elif pos == 41:
            fork_l(pos, facing)
        elif pos == 43:
            fork_m(pos, facing)
        elif pos == 56 or pos == 33 or pos == 60:
            coin_room(pos, facing)
        elif pos == 63:
            maze_exit(pos, facing)
        else: print(f"The new pos is: {pos}")



    def maze_entrance(pos, facing):
        if facing == "north":
            sleep(1)
            print("You stand at the entrance to the maze, the way back has been blocked and the walls hug your sides.")
        elif facing == "south":
            sleep(1)
            print("You stand at the entrance to the maze, the door is still locked. ")
        else:
            print("Somethng broke")
        sleep(1)
        player_move = input("Plese enter forward, back, left or right Dave " ).strip().lower()
        
        if player_move == "forward" and facing == "north":
            # lever room
            print("You proceed into the next room")
            sleep(1)
            pos += 10
            room_check(pos, facing)
        elif player_move == "forward" and facing == "south":
            # Door
            facing = direction_check(facing, player_move)
            print("You collide with a locked door.")
            sleep(1)
            room_check(pos, facing)
        elif player_move == "back" and facing == "north":
            print("You turn and stare at the a maze ing door.")
            sleep(1)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)
        elif player_move == "back" and facing == "south":
            print("You turn around and proceed into the next room")
            sleep(1)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)
        elif player_move == "left" or player_move == "right":
            print("You bump into a wall")
            sleep(1)
            room_check(pos, facing)
        else:
            print("Let's try this again Dave")
            room_check(pos, facing)
    def lever_room(pos, facing):


        if facing == "north":
            sleep(1)
            print("The path leads both left and right with a mighty lever infront of you")
        elif facing == "west":
            sleep(1)
            print("The lever is to your right and the entrace to your left")
        elif facing == "east":
            sleep(1)
            print("The lever is to your left and the entrace to your right")
        else:
            print("something broke")
            sleep(1)
        player_move = input("Plese enter forward, back, left or right Dave, you can also use the lever " ).strip().lower()


        if player_move == "use":
            if dave.get("lever") == True:
                sleep(1)
                print("You've already pulled the lever")
                room_check(pos, facing)
            else:
                sleep(1)
                print("You hear something heavy move")
                dave.setdefault("lever", True)
                room_check(pos, facing)


        elif (player_move == "forward" and facing == "north") or (player_move == "right" and facing == "west" ) or (player_move == "right" and facing == "east"): 
            sleep(1)
            print("you bump into the lever..ow")
            room_check(pos, facing)

        elif (player_move == "left" and facing == "north") or (player_move == "forward" and facing == "west") or (player_move == "back" and facing == "east"):
            sleep(1)
            print(f"you procced {player_move} into the next room")
            pos -= 1
            facing = direction_check(facing, player_move)
            room_check(pos, facing)

        elif(player_move == "back" and facing == "north") or (player_move == "left" and facing == "west") or (player_move == "right" and facing == "east"):
            pos -= 10
            sleep(1)
            print(f"you procced {player_move} towards the entrance")
            facing = direction_check(facing, player_move)
            room_check(pos, facing)


        elif(facing == "north" and player_move == "right") or (facing =="east" and player_move == "forward") or (facing == "west" and player_move):
            pos += 1
            sleep(1)
            print(f"you procced {player_move} into the next room")
            facing = direction_check(facing, player_move)
            room_check(pos, facing)



        
        else: 
            sleep(1)
            print("input a proper direction, dave")
            room_check(pos, facing)
    def hallway(pos, facing):
        sleep(1)
        print("The stone walls still loom on either side, kinda scary eh dave?")
        sleep(1)
        player_move = input("Plese enter forward, back, left or right Dave " ).strip().lower()
        if(facing == "west" and player_move =="forward") or (facing == "east" and player_move == "back"):
            pos -= 1
            facing = direction_check(facing, player_move)
            sleep(1)
            move_text(player_move)
            room_check(pos, facing)
        elif (facing == "west" and player_move =="back") or (facing == "east" and player_move == "forward"):
            pos += 1
            facing = direction_check(facing, player_move)
            sleep(1)
            move_text(player_move)
            room_check(pos, facing)
        elif player_move == "right" or player_move == "left":
            sleep(1)
            print("you bounce off the wall")
            room_check(pos, facing)
        elif (facing == "north" and player_move == "forward") or (facing == "south" and player_move == "back"):
            pos += 10
            facing = direction_check(facing, player_move)
            sleep(1)
            move_text(player_move)
            room_check(pos, facing)
        elif (facing == "north" and player_move == "back") or (facing == "south" and player_move == "forward"):
            pos -= 10
            facing = direction_check(facing, player_move)
            sleep(1)
            move_text(player_move)
            room_check(pos, facing)
        else: 
            sleep(1)
            print("input a proper direction, dave")
            room_check(pos, facing)       
    def corner_room_ll(pos, facing):
        if(facing == "west"):
            sleep(1)
            print("The wall to your left and the one infront blocks your way")
        elif(facing == "south"):
            sleep(1)
            print("The wall to your right and front blocks your way")

        player_move = input("Plese enter forward, back, left or right Dave " ).strip().lower()

        if (facing == "west" and player_move == "right") or (facing == "south" and player_move == "back"):
            pos += 10
            facing = direction_check(facing, player_move)
            sleep(1)
            move_text(player_move)
            room_check(pos, facing)

        elif(facing== "south" and player_move == "left" ) or (facing== "west" and player_move =="back" ):
            pos += 1
            facing = direction_check(facing, player_move)
            sleep(1)
            move_text(player_move)
            room_check(pos, facing)
        
        elif(facing == "west" and (player_move == "forward" or player_move == "left")) or (facing == "south" and (player_move == "right" or player_move == "forward")):
            sleep(1)
            print("you bump into a wall")
            room_check(pos, facing)


        else: 
            print("input a proper direction, dave")
            room_check(pos, facing) 
    def corner_room_lu(pos, facing):
        if facing == "north":
            sleep(1)
            print("The wall ahead and to your left blocks the way")
        elif facing == "west":
            sleep(1)
            print("The wall ahead and to your right blocks the way")

        player_move = input("Plese enter forward, back, left or right Dave " ).strip().lower()
        if (facing == "north" and player_move == "right" or (facing == "west" and player_move == "back")):
            pos += 1
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)

        elif(facing == "north" and player_move == "back") or (facing == "west" and player_move == "left"):
            pos -= 10
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)
        elif(facing == "north" and (player_move == "forward" or player_move == "left") or (facing== "west" and (player_move == "foward" or player_move == "right"))):
            sleep(1)
            wall_bump()
            room_check(pos, facing)

        else: 
            sleep(1)
            print("input a proper direction, dave")
            room_check(pos, facing)
    def corner_room_ru(pos, facing):
        if facing == "east":
            sleep(1)
            print("The walls to your right and front block the way")
        elif facing == "south":
            sleep(1)
            print("The walls to your front and left blow the way")
        else:
            sleep(1)
            print("Something broke")

        sleep(1)
        player_move = input("Plese enter forward, back, left or right Dave " ).strip().lower()

        if(facing == "east" and player_move == "left") or (facing == "south" and player_move == "back"):
            pos += 10
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)
        elif(facing == "east" and player_move == "back") or (facing == "south" and player_move == "right"):
            pos -= 1
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)
        elif(facing == "south" and (player_move == "forward" or player_move == "left")) or (facing == "east" and (player_move == "forward" or player_move == "right")):
            sleep(1)
            wall_bump()
            room_check(pos, facing)
        else: 
            sleep(1)
            print("input a proper direction, dave")
            room_check(pos, facing)  
    def corner_room_rr(pos, facing):
        if facing == "north":
            sleep(1)
            print("The wall ahead and to your right blocks the way")
        elif facing == "east":
            sleep(1)
            print("The wall ahead and to your left blocks the way")

        player_move = input("Plese enter forward, back, left or right Dave " ).strip().lower()

        if(facing == "north" and player_move == "left") or (facing == "east" and player_move == "back"):
            pos -= 1
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            print(f"room51 facing {facing}")
            room_check(pos, facing)
        elif (facing == "north" and player_move == "back") or (facing == "east" and player_move=="right"):
            pos -= 10
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)
        elif (facing == "north" and (player_move == "forward" or player_move =="right")) or (facing=="east" and (player_move == "forward" or player_move == "left" )):
            sleep(1)
            wall_bump()
            room_check(pos, facing)
        else: 
            print("input a proper direction, dave")
            room_check(pos, facing) 
    def fork_l(pos, facing):
        if facing == "north":
            sleep(1)
            print("You come to a spoon, no a fork in the maze, there is a wall to your left")
        elif facing == "west":
            sleep(1)
            print("You come to a spoon, no a fork in the maze, there is a wall ahead")
        elif facing == "south":
            sleep(1)
            print("You come to a spoon, no a fork in the maze, there is a wall to your right")

        player_move = input("Plese enter forward, back, left or right Dave " ).strip().lower()
        if(facing == "north" and player_move == "forward") or (facing == "west" and player_move == "right") or (facing == "south" and player_move == "back"):
            pos += 10
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)
        elif(facing == "north" and player_move == "back") or (facing == "west" and player_move == "left") or (facing == "south" and player_move == "forward"):
            pos -= 10
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)
        elif(facing == "north" and player_move == "right") or (facing == "west" and player_move == "back") or (facing == "south" and player_move == "left"):
            pos += 1
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)
        else: 
            sleep(1)
            print("input a proper direction, dave")
            room_check(pos, facing)
    def fork_m(pos, facing):
        if facing == "north":
            sleep(1)
            print("You step into the maze crossroads, a wall is infront of you")
        elif facing == "west":
            sleep(1)
            print("You step into the maze crossroads, you see a wall to your right")
        elif facing == "east":
            sleep(1)
            print("You step into the maze crossroads, you see a wall to your left")
        
        player_move = input("Plese enter forward, back, left or right Dave " ).strip().lower()

        if(facing == "north" and player_move == "left") or (facing == "east" and player_move == "back") or (facing == "west" and player_move== "forward"):
            pos -=1
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)

        elif(facing == "north" and player_move == "right") or (facing == "east" and player_move == "forward") or (facing == "west" and player_move== "back"):
            pos +=1
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)
        elif(facing == "north" and player_move == "back") or (facing == "east" and player_move == "right") or (facing == "west" and player_move== "left"):
            pos -= 10
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)

        elif(facing == "north" and player_move == "forward") or (facing == "east" and player_move == "left") or (facing == "west" and player_move== "right"):
            sleep(1)
            wall_bump()
            room_check()
        else: 
            print("input a proper direction, dave")
            room_check(pos, facing)
    def coin_room(pos, facing):
        if dave.get(pos) == True:
            sleep(1)
            print("You're back at the dead end, now coinless")
        else:
            sleep(1)
            print("You come to dead end, but look at the floor Dave a shiny coin to pocket")
            dave.setdefault(pos, True)
            print("Coin Pocketed")

        player_move = input("Plese enter forward, back, left or right Dave " ).strip().strip().lower()
        if facing == "north" and player_move == "back":
            pos -= 10
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)
        elif facing == "south" and player_move == "back":
            pos += 10
            sleep(1)
            move_text(player_move)
            facing = direction_check(facing, player_move)
            room_check(pos, facing)
        elif player_move == "forward" or player_move == "left" or player_move == "right":
            sleep(1)
            wall_bump()
            room_check(pos, facing)
        else: 
            print("input a proper direction, dave")
            room_check(pos, facing)

        
    def maze_exit(pos, facing):
        if dave.get("lever") != None:
            print("You have made it to the end of the maze! congratulations")
            maze_beaten()
        else:
            print("You come to the locked door upon the exist, doesn't seem like theres anypoint hanging here dave, might as well go back")
            pos -= 1
            facing = "east"
            room_check(pos, facing)
    room_check(dave.get("pos"), dave.get("direction"))
    # player_move = input("Plese enter forwards, back, left or right Dave " ).strip().strip().lower()

        # else: 
        #     print("input a proper direction, dave")
        #     room_check(pos, facing)

def maze_beaten():
    maze_coins =[]
    for items in dave:
        if items == 60 or items == 33 or items == 56:
            maze_coins.append(items)
    dave.update({"coins": dave.get("coins") + len(maze_coins)})
    for coins in maze_coins:
        if dave.get(coins) == True:
            dave.pop(coins)
    print("Congratulations you beat the maze")
    print("Congratulations you beat the maze")
    print("Dave then proceeds into the next room")
    Room_6()
# ===============================================Maze====================================================================
# ==============================================    Tim=================================================================
def endscroll():
    print ("THE END")
    print ("Brought to you by")
    sleep(1)
    print ("Andrew Ormrod-Hague")
    sleep(1)
    print ("Carson Lawson")
    sleep(1)
    print ("Hasan Elahi")
    sleep(1)
    print ("Inonge Namushi")
    sleep(1)
    print ("Joshua Jones")
    sleep(1)
    print ("Thank you for playing Tab!")
    quit()

def Room_6():
    
    def Options():
        Player_input = input("Options:|Look|Use|Take|Talk|Interact: ").strip().upper()
        if Player_input=="LOOK":
            Look()
            Options()
        elif Player_input=="USE":
            Use()
            Options()
        elif Player_input=="TAKE":
            Take()
            Options()
        elif Player_input=="TALK":
            Talk()
            Options()
        elif Player_input=="INTERACT":
            Interact()
            Options()
        else:
            print("Invalid action")
            return(Options())

    def room_description():
        print("Before Dave is a room filled with casks of ale, across from the doorway exists a steep staircase from the cellar, oh yeah and a cyclops standing between dave and the hatch idly smoking a cigertte out of a small window to the outside")
        
        print ("Dave gets a distinct feeling that the cyclops isnt going to let him through without some kind of sidequest")
        sleep(1)
        print ("What?")
        print ("""                                                                                   
                             ██                                                    
                          ██ █ ███████████                                         
                        ███████          ███                                       
                    ████                   ██                                      
                 ███            █████       ████                                   
               ███         ████                 ██                                 
              ██                                ██                                 
              ██                               ███                                 
             ██                   ████████████████             ████                   #
             █              ██████████     ██    █           ██    ██              
            ██      ██  ████  █████████   ██      █         ███    ██                ##
          ████        ██   ███████████████        ███      ██ █     ██                 #
       ███   █                  █████              ██     ██  ██     ██████           ##
      ██ ██                                         █     ██   ██    ██   ██         # ##
       ██  ██                            ███        ██    ██    █    ██   ███ ███    ##
       ███     ██                ██                   ██  ██    █████████████████   ##
         ██     ██                                    ██   █  ██       __        ██#
           ████   ███                      █████████████   █   ████████  █████████ 
          ██  ██    ██            █████████            ██ ██     ████    ███    █  
         ██   ██     █       █████                     ██ ██    ██      ████   ██  
        ██     ██           ██                        ██  █    ██      ██ ██  ██   
     ███       ██          █              ████████     █  █    █       █████████   
    ██          ██     █              ████           ███████          ██      ██   
  ██             ██    ███████        █              ██    █         ███      █    
                   ███                              ██      █       ██      ███    
                     ████                         ███      ██    ███     ███       
                         ███#=_____________=#██████        ██             █        
                         """)
    def cyclops():
            print("typical case of an underpaid employee this cyclops looks tired and coinless likely from spending his coin on cigerettes to stay sane from the working grind.")
            print ("""                                                                                   
                             ██                                                    
                          ██ █ ███████████                                         
                        ███████          ███                                       
                    ████                   ██                                      
                 ███            █████       ████                                   
               ███         ████                 ██                                 
              ██                                ██                                 
              ██                               ███                                 
             ██                   ████████████████             ████                   #
             █              ██████████     ██    █           ██    ██              
            ██      ██  ████  █████████   ██      █         ███    ██                ##
          ████        ██   ███████████████        ███      ██ █     ██                 #
       ███   █                  █████              ██     ██  ██     ██████           ##
      ██ ██                                         █     ██   ██    ██   ██         # ##
       ██  ██                            ███        ██    ██    █    ██   ███ ███    ##
       ███     ██                ██                   ██  ██    █████████████████   ##
         ██     ██                                    ██   █  ██       __        ██#
           ████   ███                      █████████████   █   ████████  █████████ 
          ██  ██    ██            █████████            ██ ██     ████    ███    █  
         ██   ██     █       █████                     ██ ██    ██      ████   ██  
        ██     ██           ██                        ██  █    ██      ██ ██  ██   
     ███       ██          █              ████████     █  █    █       █████████   
    ██          ██     █              ████           ███████          ██      ██   
  ██             ██    ███████        █              ██    █         ███      █    
                   ███                              ██      █       ██      ███    
                     ████                         ███      ██    ███     ███       
                         ███#=_____________=#██████        ██             █        
                         """)
    def Look():
         Look = input("look at what?:").strip().upper()
         if Look == "ROOM":
             room_description()
         elif Look == "CYCLOPS":
             cyclops()
    def Use():
        list_inv(dave)
        Use = input("Use what?").strip().upper()
        if Use == ("ROPE"):
            print("dave throws the length of rope at the cyclops, not much happens")
            return(Room_6())
        else:
            print("And how are you going to 'Use' that exactly?..no don't bother telling me, try something else")
            return(Options())
    def Interact():
        print("Well we're in the endgame Dave, are we going to 'brawl' or 'bribe' ol One eye?")
        Use = input("What do you want to do?").strip().upper()
        if Use == ("BRAWL"):
            Confirm = input("You sure you want to do that dave?").strip().upper()
            if Confirm == ("YES"):
              print("As dave approach the cyclops squares up, planting both fists into your chest as dave gets close enough to reach, that really hurt... and daves dead")
              endscroll()
            else:
              print("Yeah it wasnt the best idea in the first place anyway")
              return(Options())
        elif Use == ("BRIBE") and (dave.get("coins") >=7 ):
            print("Eh fine you can go up")
            print ("""                                                                                   
                             ██                                                    
                          ██ █ ███████████                                         
                        ███████          ███                                       
                    ████                   ██                                      
                 ███            █████       ████                                   
               ███         ████                 ██                                 
              ██                                ██                                 
              ██                               ███                                 
             ██                   ████████████████             ████                   #
             █              ██████████     ██    █           ██    ██              
            ██      ██  ████  █████████   ██      █         ███    ██                ##
          ████        ██   ███████████████        ███      ██ █     ██                 #
       ███   █                  █████              ██     ██  ██     ██████           ##
      ██ ██                                         █     ██   ██    ██   ██         # ##
       ██  ██                            ███        ██    ██    █    ██   ███ ███    ##
       ███     ██                ██                   ██  ██    █████████████████   ##
         ██     ██                                    ██   █  ██       __        ██#
           ████   ███                      █████████████   █   ████████  █████████ 
          ██  ██    ██            █████████            ██ ██     ████    ███    █  
         ██   ██     █       █████                     ██ ██    ██      ████   ██  
        ██     ██           ██                        ██  █    ██      ██ ██  ██   
     ███       ██          █              ████████     █  █    █       █████████   
    ██          ██     █              ████           ███████          ██      ██   
  ██             ██    ███████        █              ██    █         ███      █    
                   ███                              ██      █       ██      ███    
                     ████                         ███      ██    ███     ███       
                         ███#=_____________=#██████        ██             █        
                         """)
            (dave.update({"coins":dave.get("coins")-7}))
            sleep(5)
            endscroll()
        else:
            print("And how are you going to 'Use' that exactly?..no don't bother telling me, try something else")
            return(Options())
    def Take():
        Take = input ("Take what?").strip().upper()
        if Take == ("CYCLOPS"):
            print ("Dave dont try to pick up the cyclops, there are too many reasons to not do that")
        else:
            print ("I don't know what bright idea you think you have trying this Dave, but this isn't it")
            return(Options())
    def Talk():
        Talk = input ("Talk to who?").strip().upper()
        if Talk == ("CYCLOPS"):
            print ("oi! what the hell are you doing down here! if the boss sees you he will be rightfully pissed if I let some bloke down here")
            print ("""                                                                                   
                             ██                                                    
                          ██ █ ███████████                                         
                        ███████          ███                                       
                    ████                   ██                                      
                 ███            █████       ████                                   
               ███         ████                 ██                                 
              ██                                ██                                 
              ██                               ███                                 
             ██                   ████████████████             ████                   #
             █              ██████████     ██    █           ██    ██              
            ██      ██  ████  █████████   ██      █         ███    ██                ##
          ████        ██   ███████████████        ███      ██ █     ██                 #
       ███   █                  █████              ██     ██  ██     ██████           ##
      ██ ██                                         █     ██   ██    ██   ██         # ##
       ██  ██                            ███        ██    ██    █    ██   ███ ███    ##
       ███     ██                ██                   ██  ██    █████████████████   ##
         ██     ██                                    ██   █  ██       __        ██#
           ████   ███                      █████████████   █   ████████  █████████ 
          ██  ██    ██            █████████            ██ ██     ████    ███    █  
         ██   ██     █       █████                     ██ ██    ██      ████   ██  
        ██     ██           ██                        ██  █    ██      ██ ██  ██   
     ███       ██          █              ████████     █  █    █       █████████   
    ██          ██     █              ████           ███████          ██      ██   
  ██             ██    ███████        █              ██    █         ███      █    
                   ███                              ██      █       ██      ███    
                     ████                         ███      ██    ███     ███       
                         ███#=_____________=#██████        ██             █        
                         """)
        else:
            print ("Talk to... Who exactly? Dave i think you should try something else because I doubt talking to yourself will help")
            return(Options())
    room_description()
    Options()
# =============================================Tim======================================================================
# ============================================TOT=======================================================================
def tot():
    easy_answers = [ ["TAB",  "DAVE",  "GNOME"], ["STOCKINGS", "NOTHING", "SWORD"],  ["DRAGON", "BUTTERFLY", "LOAF OF BREAD"] ]

    normal_answers  = [["WEST", "EAST", "SOUTH"], ["OAK", "DAISY", "ROSE"] ,["A CHOICE", "COOKIE", "HAT"]] 

    hard_answers = [[13 , 11 ,27] , [848, 1 , 648] , [624, 620, 640]]   


    final_test_answers = [["GOOSE", "GOAT", "GRANNY"], ["SKELLY", "LARRY", "LENNY"], ["BROOM", "MOP", "LADLE"], ["TAPESTRY", "PAINTING", "WALTER"]] 

    corner_obj = ["CRATE", "BARREL", "SACK", "CHAIR"] 

    table_obj = ["DAGGER", "WINE BOTTLE", "CANDELABRA" , "JEWEL", "SCROLL"] 

    wall_obj = ["WARDROBE", "CABINET", "CLOCK", "TAPESTRY", "STATUE"]

    floor_obj = ["A RUG", "A VASE", "A CHEST"]

    num_cats = [5, 9, 7] 

    random_corner_obj = choice(corner_obj)
    random_table_obj  = choice(table_obj)
    random_wall_obj  = choice(wall_obj)
    random_floor_obj  = choice(floor_obj)

    random_num_cats = choice(num_cats)

    #---- GLOBAL ----#
    answer = ""
    coins = dave.get("coins")
    valuable_item = ""
    #--- INVENTORY? ---#

    inventory = ["TANKARD", "GOLDEN EGG", "HERB", "STAFF"]

    #--- EFFECTS ----#
    abbot_speed = 0.05


    def abbot_text(text, abbot_speed=0.05, color=Fore.RED, background=Back.BLACK):
        for char in text:
            print(f"{background}{color}{char}", end='', flush=True)
            sleep(abbot_speed)
        print(Style.RESET_ALL)  
                                    
                                        
    def abbot_text_good(text, abbot_speed=0.05, color=Fore.WHITE, background=Back.LIGHTBLUE_EX): 
        for char in text:
            print(f"{background}{color}{char}", end='', flush=True)
            sleep(abbot_speed)
        print(Style.RESET_ALL)     
        
    def erase():  
        
        if name == 'nt': 
            system('cls')
        elif name == 'posix': 
            system('clear')
        
    def path(): 
        
        turn_back = ""
        take_risk = ""


        sleep(1)    
        print("...Are you sure this is a good idea....I think we should turn back!") 
        turn_back_input = False
        while turn_back_input == False:
            print("Turn back? Y/N")
            turn_back = input("") 
            turn_back = turn_back.upper()
            if turn_back == "Y":
                sleep(1)
                print("GOOD! What idiot would go down this creepy path! ") 
                sleep(1)
                print("Dave leaves. He actually made a good decision for once.")
                maze_room()
            elif turn_back == "N":
                sleep(1)
                print("Well I tried to warn you, but clearly I can't fix stupid!")  
                turn_back_input = "N"        
            else:
                sleep(1)
                print("What was that?")
            
                    
        sleep(2)        
        print("Dave slowly walks down the narrow path, the air is thick with damp and scratching can be heard from the old stone walls.")  
        sleep(2)
        print("A BAST SWIPES DOWN FROM THE CEILING!")
        sleep(2)
        print("This isn't a good sign, I'd rather be trapped back there.")
        sleep(2)
        print("The narrow path abruptly stops to reveal a huge dark hall with a colossal mirror at the end.") 
        print("Dave walks towards the mirror, someone stirs out from the dark corner of the mirror.")
        print("The figure acknowledges him and comes closer. Dave stops in his tracks. The figure becomes clearer.")          
        sleep(4)
        print("The figure is wearing a deep purple hooded cloak, covering their face only their mouth is visible. They begin to speak.")
        sleep(3)
        print("FIGURE: 'Many years...' They whisper. 'Many years have passes since one had walked this path...'")  
        sleep(2)
        print("Hard to believe someone else could be a dumb and you...")
        sleep(2)
        print("FIGURE: 'So you Seek  the ULTIMATE CHALLENGE?!'")
        print("The figure wheezes")
        print("Before you is the 'Mirror of reflection' that will take you to the dreaded...")
        print("'TRIAL OF TOMFOOLERY!'")
        sleep(4)
        print("The figure pauses, as if waiting for a fanfare...really with a name like that?!...probably a challenge that suits you though.")
        sleep(3)
        print("FIGURE: 'Should you choose to proceed, you will forfeit your past...you must beat the guardian, or you DIIIEEEEE! *Cough *Cough...'")
        print("The figure hunches over slightly. 'Apologies, I'm not in my 2,000s any more.'")
        sleep(4)
        print("Could have fooled me!")
        sleep(2)
        print("FIGURE: 'I will bestow upon you 3 coins, each will give you a chance to answer a question again...if you run out you DIIIEEEEE! *Wheeezee'")
        sleep(3)
        print("FIGURE: 'What say you?' ")
        print("The figure grins with frightful anticipation.")
        sleep(3)
        print("Well it's up to you if we die. Then again..I'd be free right? I say we do it!")
        sleep(1)
        
        
        take_risk_input = False
        while take_risk_input == False:
            print("Risk it all? Y/N")
            take_risk = input("")
            take_risk = take_risk.upper()
            if take_risk == "Y":
                take_risk_input = True
                sleep(2)
                print("FIGURE: 'Marvelous!' The figure flashes rows of sharp teeth 'Then go. Through the mirror before you and seal your fate.")
                print("There is no turning back beyond the glass' ")
                sleep(3) 
                coins += 3
                print("Dave gets 3 coins") #------DAVE HAS 3 COINS TOTAL. 
                sleep(2)
                print("The figure points a boney finger at the mirror, Dave walks towards it, his reflection staring back at him. ")
                sleep(2)
                print("Dave walks into the mirror and begins..THE TRIAL OF TOMFOOLERY! *Cough *Cough") 
                sleep(2)
                abbot_text("???: 'So...you have chosen your fate. I hope you have a good memory...DAVE...if that is your name...MWAH HA-HA-HA!'", abbot_speed)  #----- ABBOT
                sleep(2)
                print("...are you sure we can't turn back!")
                sleep(2)            
            elif take_risk == "N":
                print("Well I don't really want to know what could be in that mirror, might have been my last chance though.")
                sleep(1)
                print("Dave slowly backs away. Ruining my chance to be free.")
                maze_room()
            else:
                sleep(1)
                print("What was that?")
                                        
    path() 



    #----- BEGIN TRIAL OF TOMFOOLERY *WHEEEEZZZEEE ---- #
    def easy_room():
                                        
        global answer
        global coins
        
        
        def lose_room_1(): 
            print("")       
            sleep(2)              
            print("LENNY: 'You've used all your coin, now you sleep. I am sorry friend, tears for you I weep.'")
            sleep(2)
            print("I welcome death.")    
            sleep()
            Intro()
            
        
        #----------- INTRODUCTION TO THE BARD
        print("")
        sleep(2)
        print("As Dave walks forwards through the blackness, a room starts to form in front of him. He gingerly walks towards it until he finds himself inside.")
        sleep(2)
        print(f"The room looks old and abandoned. There is nothing in the room but for a", random_corner_obj,".")
        sleep(2)
        print("A man suddenly starts to fade into the middle of the room. As he becomes more...solid. Dave can see he is holding a lute") 
        print("The man has a long white beard, tangled in his lute. He strums the lute as he becomes fully visible.")
        sleep(3)  
        print("Man: 'Ho-Ho My friend, The name is LENNY. Tales I sing, and I know many!'")
        sleep(2)
        print("I want out!")
        sleep(1)  
        print("LENNY: 'Answer my lays and I'll let you pass, if you utter wrong it will be your last! heh-heh' ")
        sleep(2)
        print("He's clearly not a composer...how hard could it be?")
        
        
        
        #--------QUESTIONS
        
        sleep(2)
        print("Lenny strums the lute. One of the strings snap, but he doesn't seem to notice....hopefully the rest will give up soon.")
        sleep(2)
        
        while True:                                     
            if coins >= 1:    
                print("")   
                print("QUESTION 1") 
                print("") 
                print("LENNY:'A title, a title, a name for a quest. A title, a title, oh what's name of this text?' ")
                shuffle(easy_answers[0])
                print(", ".join(easy_answers[0]))
                sleep(1)   
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == "TAB":
                    sleep(1)
                    print("LENNY: 'HO-HO, HE-HE, that's right!, Diddly-Dee!' ") 
                    break 
                elif answer == "GNOME": 
                    sleep(1)
                    print("LENNY: 'There are not coins in the land for a clue. Gnome isn't right, once again he's tricked you.' ")
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_1()  
                elif answer == "DAVE": 
                    sleep(1)
                    print("LENNY: 'Barely a title, least not for a quest. A lass you are wrong, DAVE isn't the answer to my song' ") 
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_1()  
                else:            
                    sleep(1)    
                    print("LENNY: 'I didn't hear you then, can you sing that again?'")   
            
        sleep(3)
        print("")
        print("")
        while True:                                     
            if coins >= 1: 
                print("QUESTION 2:")
                print("")
                print("LENNY: 'I rest by your side, I slay your foes. To journey these treacherous plains, with me you will go.")
                shuffle(easy_answers[1])
                print(", ".join(easy_answers[1]))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == "SWORD":
                    sleep(1)
                    print("LENNY: 'HO-HO, HE-HE, that's right!, Diddly-Dee!' ")
                    break
                elif answer == "NOTHING":
                    sleep(1)         
                    print("LENNY: 'Brave, yet foolish, you would surly meet your end. You are gravely wrong my friend.' ")  
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")  
                    if coins == 0: 
                        lose_room_1()     
                elif answer == "STOCKINGS":     
                    sleep(1)    
                    print("LENNY: '...no'")    
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_1()  
                else:            
                    sleep(1)    
                    print("LENNY: 'I didn't hear you then, can you sing that again?'")      
                                            
        sleep(3)
        print("")
        print("")  
        while True:                                     
            if coins >= 1:  
                print("QUESTION 3:") 
                print("")                                 
                print("LENNY: 'Fire and brimstone, rock and smoke, I guard the castle's treasure, those who enter will burn and croak!' ")
                shuffle(easy_answers[2])
                print(", ".join(easy_answers[2]))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == "DRAGON":
                    sleep(1)
                    print("LENNY: 'HO-HO, HE-HE, that's right!, Diddly-Dee!' ")
                    break
                elif answer == "BUTTERFLY":  
                    sleep(1)       
                    print("LENNY: 'Wrong very wrong, you are mistaken. A coin I'm afraid, must be forsaken.' ")    
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_1()  
                elif answer == "LOAF OF BREAD": 
                    sleep(1)        
                    print("LENNY: 'You tried your best, that matters most. But that is wrong and you are toast.' ")  
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")  
                    if coins == 0: 
                        lose_room_1()  
                else:            
                    sleep(1)    
                    print("LENNY: 'I didn't hear you then, can you sing that again?'")   
        
                
        
                                    
        print("")                               
        sleep(3)                               
        print("LENNY: 'You've done well, my young apprentice. None have captured my lyrical sentence.'")
        sleep(2)
        print("I wonder why...")
        sleep(2)
        print("A gift for you, my greatest treasure. My finest works with it I tethered.")
        sleep(1)
        print("Days were lost, none remembered. A simple flower so small and weak.")
        sleep(1)
        print("yet many a yarn it grands me to speak.")
        sleep(2)
        print(f"Dave got a HERB and a coin")
        sleep(1)
        coins += 1
        print("You Got 1 coin. You have", coins , "left.")
        sleep(2)
        print("That..makes a lot of sense...")
        sleep(2)
        print("LENNY: 'Now Go Yonder, Go forth, continue your test. Should you succeed, I'll sing of your quest. '")
        sleep(2)
        print("Please don't.")
        sleep(1)
        print("Lenny strums his lute, and Dave starts to feel sleepy...")
        sleep(2)
        print("")
        print("Dave blacks-out")
        sleep(2)
        print("")
        abbot_text("'So you defeated the first monk...no matter...you will not get passed the second....'", abbot_speed)
        print("")
        sleep(2)
        print(Style.RESET_ALL)
        
                                        
    easy_room()
    

    
    
    erase()




    def normal_room(): 
        global answer
        global coins
        
        def lose_room_2(): 
            print("")       
            sleep(2)              
            print("VIVIAN: 'You should have turned back...I'm sorry DAVE.'") 
            sleep(2)
            print("This is fine.")  
            sleep()
            Intro() 
        
        sleep(2)
        print("Dave awakens. He feels heavy.")
        sleep(1)
        print("Our memory was erased!")
        sleep(2)
        print("Something...or someone doesn't want us to continue!")
        sleep(2)
        print("The last thing DAVE can remember is agreeing to do a perilous trial. Dave hears something hiss at him.")
        sleep(1)
        print("")
        
    
        #----------- INTRODUCTION TO THE SORCERESS
        sleep(2)
        print("Woman: 'Oh my little pumpkin, did the bad man scare you?'")
        sleep(2)
        print("A colourfully dressed woman picks up the cat, and glares at DAVE. She places the cat down next to a large bubbling cauldron.")
        sleep(2)
        print("Dave takes a look around. The room is covered with tall bookcases, with more books scattered around the floor.")
        print("Shelves on the wall in front are crammed with glowing bottles, most importantly the room is full of cats!")
        sleep(3)
        print(f"Dave counts", random_num_cats ,"cats in the room.")
        sleep(2)  
        print("Woman: 'I suppose you want to get through this trial.'The woman sounds unphased by Dave. She stands between the cauldron and Dave.")
        print("Woman: *Humpf 'My dears can tell a fool when they see one, they don't think your up for it. I'll let you pass for their sake, if you prove your not as incompetent and you look.'")
        sleep(3)
        print("Woman: My name is Vivian, should you live to remember...shall we begin?")
        sleep(1)
        print("You have", coins , "left.")
        
        
        
        #------ QUESTIONS -------#
        sleep(2)
        print("")
        print("")
        while True:                                     
            if coins >= 1:  
                print("QUESTION 1:")
                print("")
                print("VIVIAN:'If I am facing SOUTH, then I turn to face left, turn left again, then turn right, then I turn around ...which way am I facing?' ")
                shuffle(normal_answers[0])
                print(", ".join(normal_answers[0]))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == "WEST":
                    sleep(1)
                    print("VIVIAN: 'Oh, looks like you can understand directions...or have you done this before?' ")  
                    break
                elif answer == "EAST": 
                    sleep(1)
                    print("VIVIAN: 'That's wrong. I wonder how you even found this path.' ")
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_2() 
                elif answer == "SOUTH": 
                    sleep(1)
                    print("VIVIAN: 'Back to where you started?...No..That's not right.' ") 
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_2() 
                else:            
                    sleep(1)    
                    print("VIVIAN: 'Could you repeat that?'")   
            
        sleep(3)
        print("")
        print("")
        while True:                                     
            if coins >= 1:  
                print("QUESTION 2:")
                print("")
                print("VIVIAN: 'Finally...Which one of these is not like the others?' ")                             
                shuffle(normal_answers[1])
                print(", ".join(normal_answers[1]))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == "OAK":  
                    sleep(1)
                    print("VIVIAN: '...Extortionary...That's Right! It's a tree.' ")
                    break
                elif answer == "DAISY": 
                    sleep(1)        
                    print("VIVIAN: 'That's not right.' ") 
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_2()   
                elif answer == "ROSE": 
                    sleep(1)        
                    print("VIVIAN: 'Not that one.' ")
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_2()   
                else:            
                    sleep(1)    
                    print("VIVIAN: 'Could you repeat that?'") 
        
        sleep(3)
        print("")
        print("")
        while True:                                     
            if coins >= 1:
                print("QUESTION 3:")
                print("")  
                print("VIVIAN: 'What is it that given one, you'll have either two or none?'")
                shuffle(normal_answers[2])
                print(", ".join(normal_answers[2]))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == "A CHOICE":
                    sleep(1)
                    print("VIVIAN: 'Yes! too bad you chose to do this.' ")
                    break
                elif answer == "COOKIE":  
                    sleep(1)       
                    print("VIVIAN: 'I'd have two or MORE myself...not right.' ")
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_2()      
                elif answer == "HAT": 
                    sleep(1)       
                    print("VIVIAN: 'Does that sense to you...didn't think so. Wrong answer.'")  
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_2()  
                else:            
                    sleep(1)    
                    print("VIVIAN: 'Could you repeat that?'") 
                        
                        
                                                    
        print("")                               
        sleep(2) 
        print("VIVIAN: 'My my...you passed my test.' Vivian walks around the cauldron, it between her and DAVE.")
        sleep(2)
        print("She reaches her hand into the cauldron and pulls out a long staff.")
        sleep(2)
        print("My gift to you, a tool of other worldly power. It was my arm, in a previous life... May it help you go on.")
        print("Dave got a STAFF and a coin")
        sleep(2)
        print("We don't even know how to use magic....she basically just gave us a stick.")
        sleep(2)
        print("VIVIAN: 'I'll send you to your next challenger, your biggest test still awaits.'")
        sleep(2)
        print("Vivian begins to speak a chant. Vivian: 'You spin me right round...' all the cats mew in unison. Dave starts to feel dizzy... ")
        sleep(2)
        print("")
        print("Dave blacks-out")
        sleep(2)
        print("")
        abbot_text("'...Another defeat. I'll admit, you seem determined. Pity, the third will see to that!'", abbot_speed) 
        print("")
        sleep(2)
        print(Style.RESET_ALL)

        
    normal_room()     
    
                
    erase()             
            
                    
    def hard_room():
        
        global answer
        global coins
        
        def lose_room_3(): 
            print("")       
            sleep(2)              
            print("WALTER: 'As expected. I can't say I though anything more, now do please disappear. '")
            sleep(2)
            print("Sigh..we were so close.") 
            sleep()
            Intro() 
    
        
        sleep(2)
        print("Dave awakens. He feels heavy.")
        sleep(1)
        print("Our memory was erased again!")
        sleep(2)
        print("Why does he keep doing that...is there a reason?")
        sleep(2)
        print("The last thing DAVE can remember is agreeing to do a perilous trial.")
        
        #----------- INTRODUCTION TO THE MERCHANT
        
        print(f"Dave looks around the room...it's full of opulence. There is a large table with a" , random_table_obj , "on it. One of the walls has a", random_wall_obj ,"against it, and in the middle of the room there is a", random_floor_obj)
        sleep(2)
        print("Dave walks around the room...There are no exits. Maybe we have to solve something to get out of here?")
        sleep(2)
        print("Dave starts pacing and rummaging around")
        sleep(1)
        print("VOICE: AHEM!")
        sleep(2)
        print("Who said that?")
        sleep(2)
        print("VOICE: Over here...on the wall.")
        sleep(2)
        print("Dave looks around the walls...there is a large portrait of a man. Dave stares at it and is startled back when the eyes dart back and forth, until they rest on him.")
        print("""                                                                                                   
                                                                                                    
                                                                                                    
        ███████████████████████████████████████████████████████████████████████████  ██          ██    
        █              █                                                             █            █    
        █              █                                                             █            ██   
        █              █                                                             █            █    
        █        █████████████████████████████████████████████████████      ████████████          █    
        █      ██                                                                        ██       █    
    ██   ████                                                                         ██       █    
    ██      █                                                                         ██ ███   █    
    ██      █░                             ██████████                                  █       █    
    ██      ██                         ██             ███                             ██       █    
    ██       █                      ██                    ███          █               █       █    
    ██       █            ██                                 ███      ███              █       █    
    ██      ██          ██ █    █                                ████   █              █       █    
    ██      ██         █    ██               ███   ██ ██ ██             █              █       █    
    ██      ██         █                    █              ██           █              █       █    
    ██      █         ██                  ██                 ██        ██              █       █    
    ██      █          █                 ██                     ██    █               ██       █    
    ██      █          ██              ██                    ███  ███                  █       █    
    ██      █            ██          ██                    ██        ██               ██       █    
    ██      █              ████  ███████    ██            █     ████   █              ██       █    
        █      █           ██ █       █          ██          █     ████    █             ██       █    
        █      █         ██   █      ██  ███      █      █  █        █     █             █       ██    
        █      █         █           █   ███      █        ███            ██             █        █    
        █      █         █           ██           █          ██          ██              ██       █    
        █      █          █    █      █           █            █████  ███                █        █    
        █      █           ██   █      ██       ██             █                         █        █    
        █      █            ██████       ███████    ███        █   ██  █                 █        █    
        █      █                 ██              █     ███████       █ █                 █       ██    
        █      █                  ██           █               ██   █ █                  █       ██    
        █      █                 █  ██        █    ██   ███████      ██                  █       ██    
        █      █                █              ███  ████           ██  █                 █       ██    
        █      █                ██                              ██      █ █████████      █       ██    
        █      █               █              ███          █████        ██          █    █       ██    
        █      █               ██               ██████████     ██        █      █    █   █       ██    
        █      █           ███  ████            █       █       █        █      █     █  █       █     
        ██     █        ███             ██      █       █       █       ██     ██     ██ █       █     
        ██     ██    ███                █  ██████        ██ ██████     ██      █       █ █       █     
        ██     ██   █                  █        █        █         ████  █    █        ███       █     
        █      █  █                   ██       █      ██                █    █         ██       █     
        █      █ ██                     ██      ██████      █         ██    █          ██       █     
        █      █ █                        ███       ██    ████    ███      ██          ██       █     
        █      █ █                           ███    █   ██   ██████        █            █       █     
        █      █ █                              ██   ▓█▓           █      ░█            █       █     
        █      █ █                                 ██   ███         █     ██            ██      █     
        █     ██ █                        █          ███   ██        █     █            ██      █     
        █     ██ █                        █                   ██      █    █            ██      █     
        █     ██ █                        █                     ██    ██   █            ██      █     
        █     ██ █                        ██                      ██   ██  █  ███▒      ██      █     
        █ ██████ ██                       ██                        ██  ██ █ █    █     █       █     
        ███   ██  █                        █                          ██ ███ █   █      █████████     
        █     ██  █                        █                     █  ██  ████   █        █       █     
        █      █   █                       ██                    █   █    ██            █       █     
        █      ██  █   █████                █                     ██       ██           ██      █     
        █            █          ███ █ ▓█████████████████████████████████████████████████        █     
        █            █                                                           █              ██    
        █            █                                                           █              ██    
        ███         █                                                           █              ██    
                            ███████████████████████████████████████████████████████████████████      
                                                                                                    
                                                                                                    """)
        print("PORTRAIT: 'What are you doing in here. PEASANT! These are MY wares!.....Why am I a painting? Well I'm dead you buffoon. Mine like those other other ruffians sprits remain here until, SOMEONE triumphs.'")
        sleep(4)
        print("The portraits eyes are all th that moves...it's highly disturbing.")
        sleep(2)
        print("PORTRAIT: 'Rather than become a haggard hermit, like that gate keeper. I chose to preserve my brilliance in the finest form.")
        sleep(2)
        print("Let's go back to the bard...")
        sleep(2)
        print("PORTRAIT: 'My name is WALTER. I was a wealthy merchant...as you can see. I don't have time to play games with the likes of you!'")
        sleep(2)
        print("WALTER: '.....I have no choice on the matter however, it was part of the deal...VERY WELL. If you can answer my questions. I'll let you go die.'")
        sleep(2)
        print("WALTER: 'Get and answer wrong, I'll let you retry. But I'll take my twice the payment!...Shall we?'")
        sleep(2)
        
        print("WALTER: 'Your time starts now, poor person.'")
        sleep(2)
        print("Did he really need to add that...we are poor though. ")
        print("You have", coins , "left.")
    
        sleep(2)
        print("")
        print("")
        while True:                                     
            if coins >= 1:
                print("QUESTION 1:")
                print("")                                        
                print("WALTER:'If I have 30 gold coins and I spend 17, how many are left?' ")
                shuffle(hard_answers[0])
                print(', '.join(map(str,hard_answers[0])))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == 13:
                    sleep(1)
                    print("WALTER: 'Quite Right' ") 
                    break
                elif answer == 11: 
                    sleep(1)
                    print("WALTER: 'Wrong!' ")
                    sleep(1)
                    coins -= 2
                    sleep(1)
                    print("You lose 2 coins. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_3()  
                elif answer == 27: 
                    sleep(1)
                    print("WALTER: 'VERY Wrong!' ") 
                    sleep(1)
                    coins -= 2
                    sleep(1)
                    print("You lose 2 coins. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_3()  
                else:            
                    sleep(1)    
                    print("WALTER: 'That was illegible, answer again properly.'") 
    
        sleep(2)
        print("")
        print("")
        while True:                                     
            if coins >= 1:
                print("QUESTION 2:")
                print("")   
                print("WALTER: 'If 1 chandler costs 212 gold and I need 4, how much gold will they be?'")
                shuffle(hard_answers[1])
                print(', '.join(map(str,hard_answers[1])))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == 848:
                    sleep(1)
                    print("WALTER: 'That's correct...interesting' ")
                    break
                elif answer == 1:       
                    sleep(1)
                    print("WALTER: 'How?!' ")    
                    sleep(1)
                    coins -= 2
                    sleep(1)
                    print("You lose 2 coins. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_3() 
                elif answer == 648:   
                    sleep(1)     
                    print("WALTER: 'no, no. Wrong!'") 
                    sleep(1)
                    coins -= 2
                    sleep(1)
                    print("You lose 2 coins. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_3()   
                else:            
                    sleep(1)    
                    print("WALTER: 'That was illegible, answer again properly.'") 
                                    
        sleep(2)
        print("")
        print("")
        while True:                                     
            if coins >= 1:
                print("QUESTION 3:")
                print("")                                    
                print("WALTER: 'If I sell my rare gem valued at 520 coin for 20% more, how much would it cost?' ")
                shuffle(hard_answers[2])
                print(', '.join(map(str,hard_answers[2])))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == 624:
                    sleep(1)
                    print("WALTER: '..I am...speechless..' ")
                    break
                elif answer == 620: 
                    sleep(1)        
                    print("WALTER: 'Not right.' ")    
                    sleep(1)
                    coins -= 2
                    sleep(1)
                    print("You lose 2 coins. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_3() 
                elif answer == 640:     
                    sleep(1)    
                    print("WALTER: 'Too bad, that's Wrong.' ")   
                    sleep(1)
                    coins -= 2
                    sleep(1)
                    print("You lose 2 coins. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_3()  
                else:            
                    sleep(1)    
                    print("WALTER: 'That was illegible, answer again properly.'")              
            



                        
        print("")                               
        sleep(2) 
        print("WALTER: '..Remarkable. Simply divine I must say. No one has ever bested ME!  '")
        sleep(2)
        print("WALTER: 'Obviously I can't quite move, but I have something for you.' A golden oval object appears in the painting. 'Go on reach for it.' ")
        sleep(2)
        print("Dave reaches for the object in the painting, his hand morphing into it as though it was a part of the oil. He grabs the oval and pulls back his hand...it's an egg.")
        sleep(2)
        print("WALTER: 'Yes, I acquired a golden egg. The rarest of all my wares, my opus. I realise I'm not who I was, as you have shown me. I was poor once, a farm hand. The goose my only friend. Treasure it as I have dear boy, the memories are enough for me now...  '")
        sleep(3)
        print("Dave got a", "GOLDEN EGG", "and a coin") #--------- DAVE NEEDS THE "HERB" AND "+1 COIN" IN INVENTORY
        sleep(2)
        print("Perhaps he's not such a bad guy....")
        sleep(1)
        print("WALTER: 'Off you go to die, I'll look after the egg once more when you do. Good luck Dave.'")
        sleep(2)
        print("Nevermind.")
        sleep(2)
        print("The room begins to shake terribly...")
        sleep(2)
        print("")
        print("Dave blacks-out")
        print("")
        sleep(2)
        abbot_speed = 0.01
        abbot_text("'NO! NO!  NO! This isn't right. FINE. SO BE IT. HAVE AT YOU!'", abbot_speed) #----- ABBOT
        sleep(2)
        print(Style.RESET_ALL)

    hard_room()
        
        
    erase()

    def abbot():

        global answer
        global abbot_speed 
        global Tankard
        global coins
        global valuable_item
        
        coins = 3
        
        def lose_room_4(): 
            print("")
            abbot_text("ABBOT: 'You should never have come here. I will take now what is mine.'", abbot_speed) 
            print("")
            sleep(2)
            print("")
            print("Nice knowing you Dave...or not...")   
            sleep()
            Intro()
            

        
        sleep(2)
        print("Dave awakens. He feels heavy.")
        sleep(1)
        print("Our memory was erased!")
        sleep(2)
        print("This is it...What have you gotten us into?!")
        sleep(2)
        print("The last thing DAVE can remember is agreeing to do a perilous trial...")
        sleep(2)
        print("Something big takes steps towards him. Dave sees nothing but mist and great pillars endlessly reaching up into a non-existent sky. The steps tremor the ground. Dave gets up quickly.")
        sleep(3)
        abbot_text("???: 'You...You should not have made it here!...I refuse to believe your before me..but it is so.'" , abbot_speed)
        sleep(2)
        print("Dave is met by a colossal creature, it's body a splice of different beasts. It lowers it's massive head close to DAVE probably 100 times the size of him alone.")
        sleep(2)
        abbot_speed = 0.05
        abbot_text("???: 'I am the ABBOT. Your the final test. I will ask you 9 questions, to see if you have overcome your weakness...1 coin another chance...this game ends here!'" , abbot_speed)
        sleep(2)
        print("Whatever happens here Dave, I still hate you.")
        sleep(1)
        print("You have", coins , "left.")
        
        #------ QUESTIONS ------ # 
        sleep(3)
        print("")
        print("")
        while True:                                     
            if coins >= 1:
                print("QUESTION 1:")
                print("")  
                abbot_text("ABBOT: 'What creature blocked your path?'" , abbot_speed)
                shuffle(final_test_answers[0])
                print(", ".join(final_test_answers[0]))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == "GOAT":
                    sleep(1)
                    abbot_text("ABBOT: 'Yes. I'm still not sure why.' " , abbot_speed)
                    break
                elif answer == "GOOSE":       
                    sleep(1)  
                    abbot_text("ABBOT: 'No, but you would have had a hard time.' " , abbot_speed) 
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_4()        
                elif answer == "GRANNY":   
                    sleep(1)      
                    abbot_text("ABBOT: 'Really? A GRANNY, are you mocking me,  NO!' " , abbot_speed) 
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_4() 
                else:            
                    sleep(1)    
                    abbot_text("ABBOT: 'Type that again.'", abbot_speed)  
                    sleep(1)
            
            
        sleep(3)
        print("")
        print("")
        while True:                                     
            if coins >= 1:
                print("QUESTION 2:")
                print("")  
                abbot_text("ABBOT: 'What is the bard's name?'", abbot_speed)
                shuffle(final_test_answers[1])
                print(", ".join(final_test_answers[1]))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == "LENNY":
                    sleep(1)
                    abbot_text("ABBOT: 'Yes...I'm way back here for a reason.' " , abbot_speed)
                    break
                elif answer == "SKELLY":        
                    sleep(1) 
                    abbot_text("ABBOT: 'No. That isn't his name.' " , abbot_speed)  
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_4()     
                elif answer == "LARRY":         
                    sleep(1)
                    abbot_text("ABBOT: 'No. ' " , abbot_speed)
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_4()     
            else:            
                sleep(1)    
                abbot_text("ABBOT: 'Type that again.'", abbot_speed)  
                sleep(1)
            
        sleep(3)
        print("")
        print("")
        while True:                                     
            if coins >= 1:
                print("QUESTION 3:")
                print("")  
                abbot_text("ABBOT: 'What object wanted you to clean?'", abbot_speed)
                shuffle(final_test_answers[2])
                print(", ".join(final_test_answers[2]))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == "BROOM":
                    sleep(1)
                    abbot_text("ABBOT: 'Yes. Someone had to do it' " , abbot_speed)
                    break
                elif answer == "MOP":      
                    sleep(1)   
                    abbot_text("ABBOT: 'Wrong Object.' " , abbot_speed)    
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0:
                        lose_room_4()   
                elif answer == "LADLE":   
                    sleep(1)    
                    abbot_text("ABBOT: 'Do you even know what one is? NO!' " , abbot_speed)  
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_4()     
                else:            
                    sleep(1)    
                    abbot_text("ABBOT: 'Type that again.'", abbot_speed)  
                    sleep(1)     
        
            
        sleep(3)
        print("")
        print("")
        while True:                                     
            if coins >= 1:
                print("QUESTION 4:")
                print("")
                abbot_text("ABBOT: 'Who was on the wall?'", abbot_speed)
                shuffle(final_test_answers[3])
                print(", ".join(final_test_answers[3]))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == "WALTER":
                    sleep(1)
                    abbot_text("ABBOT: 'Yes. He's alright when you get to know him...and have money.' " , abbot_speed)
                    break
                elif answer == "TAPESTRY":   
                    sleep(1)      
                    abbot_text("ABBOT: 'Did the tapestry have those creepy eyes? NO.' " , abbot_speed)  
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0:
                        lose_room_4()     
                elif answer == "PAINTING":      
                    sleep(1)  
                    abbot_text("ABBOT: 'No. You should read more carefully...' " , abbot_speed)   
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_4()     
                else:            
                    sleep(1)    
                    abbot_text("ABBOT: 'Type that again.'", abbot_speed)  
                    sleep(1) 
            
            
        print("")    
        print("")
        sleep(2) 
        abbot_text("ABBOT: 'NOOO! YOU CANNOT WIN!'", abbot_speed)
        print("The abbot stops his beastly feet, the pillars waver under the force.")
        sleep(3)
        abbot_text("ABBOT: 'Let's see if you still remember!'", abbot_speed)
        print("")
        print("")
        
        sleep(2)
        print("")
        print("")
        while True:                                     
            if coins >= 1:
                print("QUESTION 5:")
                print("")
                abbot_text("ABBOT: 'What was in the corner of the bard's room?'", abbot_speed)
                shuffle(corner_obj)
                print(", ".join(corner_obj))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == random_corner_obj:
                    sleep(1)
                    abbot_text("ABBOT: 'Yes. He hasn't really noticed the lack of furniture...' " , abbot_speed)
                    break
                elif answer != random_corner_obj:  
                    sleep(1)       
                    abbot_text("ABBOT: 'No. There was only 1 thing in there, how could you forget that?' " , abbot_speed)  
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_4()     
                else:            
                    sleep(1)    
                    abbot_text("ABBOT: 'Type that again.'", abbot_speed)  
                    sleep(1) 
                

            
        sleep(3)
        print("")
        print("")
        while True:                                     
            if coins >= 1:
                print("QUESTION 6:")
                print("")
                abbot_text("ABBOT: 'How many cats were in Vivian's room?'", abbot_speed)
                shuffle(num_cats)
                print(', '.join(map(str,num_cats)))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == random_num_cats:
                    sleep(1)
                    abbot_text("ABBOT: 'Yes. As a....whatever part cat I am, I enjoy the company.' " , abbot_speed)
                    break
                elif answer != random_num_cats:   
                    sleep(1)     
                    abbot_text("ABBOT: 'No. Didn't you count...oh right I erased that! HA-HA-HA' " , abbot_speed)    
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_4()     
                else:            
                    sleep(1)    
                    abbot_text("ABBOT: 'Type that again.'", abbot_speed)  
                    sleep(1)  
                


        print("")
        print("")  
        sleep(2)
        abbot_text("ABBOT: 'RAWWWARRR!!!'", abbot_speed)
        print("The Abbot roars in annoyance.")
        sleep(2)
        print("")
        print("")    
            
            
        sleep(2)
        print("")
        print("")
        while True:                                     
            if coins >= 1:
                print("QUESTION 7:")
                print("")
                abbot_text("ABBOT: 'What was on Walter's table?'", abbot_speed)
                shuffle(table_obj)
                print(", ".join(table_obj))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == random_table_obj:
                    sleep(1)
                    abbot_text("ABBOT: 'Gurrr...correct.' " , abbot_speed)
                    break
                elif answer != random_table_obj:      
                    sleep(1)   
                    abbot_text("ABBOT: 'No. Not right!' " , abbot_speed) 
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_4()     
                else:            
                    sleep(1)    
                    abbot_text("ABBOT: 'Type that again.'", abbot_speed)  
                    sleep(1)        
    
            
            
        sleep(3)
        print("")
        print("")
        while True:                                     
            if coins >= 1:
                print("QUESTION 8:")
                print("")
                abbot_speed = 0.01
                abbot_text("ABBOT: 'Well, What was against Walter's wall?!'", abbot_speed)
                shuffle(wall_obj)
                print(", ".join(wall_obj))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer == random_wall_obj:
                    sleep(1)
                    abbot_text("ABBOT: 'How..did you remember that!..correct.' " , abbot_speed)
                    break
                elif answer != random_wall_obj: 
                    sleep(1)       
                    abbot_text("ABBOT: 'Wrong. I won't let you win! " , abbot_speed) 
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_4()     
                else:            
                    sleep(1)    
                    abbot_text("ABBOT: 'Type that again.'", abbot_speed)  
                    sleep(1)        
    
                    
                    
        sleep(3)
        print("")
        print("")
        while True:                                     
            if coins >= 1:
                print("QUESTION 9:")
                print("")               
                abbot_speed = 0.01
                abbot_text("ABBOT: 'W-What was on his floor?!!'", abbot_speed)
                shuffle(floor_obj )
                print(", ".join(floor_obj))
                sleep(1)
                answer = input("answer:"  )
                answer = answer.upper()
                if answer ==  random_floor_obj:
                    sleep(1)
                    abbot_text("ABBOT: '....correct.' " , abbot_speed)
                    break
                elif answer !=  random_floor_obj: 
                    sleep(1)        
                    abbot_text("ABBOT: 'NO! HA-HA, you almost made it.' " , abbot_speed)  
                    sleep(1)
                    coins -= 1
                    sleep(1)
                    print("You lose 1 coin. You have", coins , "left.")
                    if coins == 0: 
                        lose_room_4()     
                else:            
                    sleep(1)    
                    abbot_text("ABBOT: 'Type that again.'", abbot_speed)  
                    sleep(1)               
            
        
        print("")                            
        sleep(3)
        print("The Abbot stands still for a moment. Then speaks.")
        abbot_speed = 0.05
        abbot_text("ABBOT: 'Thousands of years....so many years. You have conquered your weakness....your memories. But I ask of you one more.'", abbot_speed )
        sleep(2)
        print("")
        abbot_text("ABBOT: 'You must trade 1 item for the treasure I keep, an item of great value. May it be the correct one, and you will be chosen...I'll allow you to use your coins, let's hope you have some left...'" ,abbot_speed)
        sleep(3)
        
        while True:  
            print("") 
            print("....What shall we trade?")
            print("") 
            
            
            sleep(1)
            print(", ".join(inventory))
            valuable_item = input( "" )
            valuable_item = valuable_item .upper()         
            print("") 
            
            if valuable_item == "TANKARD":                                                   
                sleep(1)
                print("It's all we have close to us...")
                sleep(2)
                print("")
                abbot_speed = 0.1
                abbot_text("ABBOT: 'You really are...The one....'",abbot_speed)
                sleep(1)
                print("Dave's tankard dissipates before his eyes")
                sleep(3)
                print("Something glistens high above, it slowly floats down, lighting up the room, revealing it's bright marble and plants. The Abbot no longer shrouded in a terrible darkness, looks almost ethereal.")
                abbot_text_good("ABBOT: I give you the HOLY TANKARD. Only the one who was truly the one to wield it was to complete this trial...it was you.")
                sleep(4)
                print("Dave receives 'THE HOLY TANKARD' it looks just like our old one...only it's glowing and can float on it's own...HANDY!")
                sleep(2)
                abbot_text_good("ABBOT: 'With it's power you will restore good upon these lands, any ale poured inside will never finish, will always have the perfect amount foam, and taste of the most succulent nectar!'",abbot_speed)
                sleep(3)
                print("...now hold on, isn't this a bit counter productive...")
                abbot_text_good("ABBOT: 'All will gather, friend and foe. Sing Shanties, cry cheers and bask in it's glow'",abbot_speed)
                sleep(2)
                print("..oh now he's rhyming too..we should have died...or at least I should.")
                sleep(2)
                abbot_text_good("ABBOT: 'I release the monks and send you back to your world. You have done well, Dave.' The Abbot bellows a deafening roar",abbot_speed)
                sleep(3)
                print("The world crumbles once again.....")
                print("") 
                print("")    
                break
            elif valuable_item == "GOLDEN EGG" or valuable_item == "HERB" or valuable_item == "STAFF":         
                abbot_text("ABBOT: 'No, Dave that isn't the item...' ")  
                sleep(1)
                coins -= 1
                sleep(1)
                print("You lose 1 coin. You have", coins , "left.")
                if coins == 0: 
                    lose_room_4() 
            else:            
                sleep(1)    
                abbot_text("ABBOT: 'Type that again.'", abbot_speed)  
                sleep(1) 
                
    abbot()
        
        
        
        
    def epic_end():
        
        sleep(4)
        print("Dave wakes up outside a tavern. In his hand a glowing tankard..., the sun is shining, he feels jubilant.")
        sleep(2)
        print("Well we did it. Whatever that was...Guess we should go save the world!")
        sleep(2)
        print("Dave get's up, and heads inside the tavern.")
        sleep(2)
        print(".....oh for--")
        sleep(1)
        print("-ULTIMATE END!")
        # --- Epilogue
    epic_end()


   
    
    
# ============================================TOT=======================================================================
print ("""     
                /==================================\.
                ||  .--------'                .   ||
                || (_)   /                   /    ||
                ||      /        .-.        /-.   ||
                ||     /        (  |       /   )  ||
                ||  .-/._        `-'-'   .'`--'`- ||
                || (_/  `-                        ||
                \==================================/

                                                              
                                                              
                                          ███████               
                                ███████████ ██  ███             
                       ██████████             ██   ██           
               ████████                         ██  ██          
            ████@███                     ████    ██  ██         
           ███    @██            ██████           ██  ██        
          ███     @@██   ██████                    █   ██       
          ██       ##██                             █   █       
          ██        #██                             ██  █       
          ██         #██                             █  █       
          ██         #██            █████████        █  █       
          ██         ##       ████                 ██████        
          ██         ##██                           ██ ██        
           ██     ..###██                           ██  ███      
           ██    ######██  ██████               ██████   ██     
            ██ ########██  ██ ███       ████████      ██  ██    
            ███########██  ██   ████████            █████████   
        █████████#####███  ████   ██       █████████      ██    
    ███████████████████████   ██    ███████          █████      
   ███████@@███████████████    ███           ███████            
   ████████████████@@@@@████      ███##███████                   
              ███████████                                  
                ███████                                       
                                                              """)

sleep(5)
Intro()
sleep(3)
Room_0()