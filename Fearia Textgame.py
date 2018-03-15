#Commands: Look around, inspect, take, pick up, go west, east, north and south, climb, descend look left and right, go forward, backwards left and right
#Created by Joar and Johan, started 08 march 2018
#Fiara text game
import time
import Va #Variables
#Defining all the classes:
#Listor funkar om man definerar dem utanför funktionen, variablar gör inte det.
c, r = 5, 3 #Number of tags, number of classes.
classes = [[0 for x in range(c)] for y in range(r)]
classes[0][0] = "Mage" #Name of the class, placeholder
classes[0][1] = 10 #Attack damage/points, placeholder value.
classes[0][2] = 20 #Magic damage/points, placeholder value.
classes[0][3] = 25 #Armor, placeholder value.
classes[0][4] = 100 #Health, placeholder value.
classes[1][0] = "Warrior" #Name of the class, placeholder.
classes[1][1] = 25 #Attack damage/points, placeholder value.
classes[1][2] = 5 #Magic damage/points, placeholder value.
classes[1][3] = 50 #Armor, placeholder value.
classes[1][4] = 130 #Health, placeholder value.
classes[2][0] = "Priest" #Name of the class, placeholder.
classes[2][1] = 15 #Attack damage/points, placeholder value.
classes[2][2] = 20 #Magic damage/points, placeholder value.
classes[2][3] = 25 #Armor, placeholder value.
classes[2][4] = 150 #Health, placeholder value.
print("Text based Game Name, 2018 created by Joar and Johtli.\n")
def handle_room(room):
        #a, b, c are time variables. Set to 1, 2, 3 for real play.
        global a
        global b
        global c
        a = 0
        b = 0
        c = 0
        if room == "start":
                drawer = "closed"
                clueless = 0
                look = "no"
                if "Kerosene Lamp" in Va.inventory:
                        print ("The dark room is lit up by the lamp you picked up.\n")
                else:
                        print ("The room is dark. You see a lamp in an adjacent room.\n")
                while True:
                        action = input("What will you do? \n")
                        action = action.lower()
                        print ("")
                        if action == "look around":
                                #When you look around this happens
                                look = "yes"
                                print ("You look around. The eerie silence crushes your eardrums. \
You are standing in a stone room made of bricks.\n\
There is a sockdrawer in the corner. The light in the other room seems miles away. \n")
                        #elif action == "vi är bäst": dröm om at hoppa till vilket rum man vill
                            #inventory.append("Kerosene Lamp")#, "Mystic Stone", "The Princess Bride"
                            #return input("Enter room to teleport\n")
                        elif action == "ca":
                            return "courtyard"
                        elif "inventory" in action:
                            print ("Inventory:                                   [%d/10][Satchel]" %(len(Va.inventory)))
                            if len(Va.inventory) != 0:
                                print (", ".join(Va.inventory))
                            else:
                                print ("Your satchel is empty.")
                            print ("")
                                #breaking the loop and you walk into the next room
                        elif "turn on" in action and "light" in action:
                                print ("You look around to see if there is a light to turn on. There is none.")
                                print ("There is, however, a light in the other, adjacent, room.\n")
                        elif "light" in action or "adjacent" in action or "room" in action or "lamp" in action:
                                return "light"
                        elif "drawer" in action:
                                print ("You approach the mystical drawer. It gives of an aura of adventure.\n")
                                #Princess bride easter egg which will affect the story later
                                while True:
                                        action = input ("What will you do?\n")
                                        action = action.lower()
                                        print ("")
                                        if "open" in action:
                                                if drawer == "open":
                                                        if "The Princess Bride" in Va.inventory:
                                                                print ("The drawer is already open. It is empty.")
                                                        else:
                                                                print ("The drawer is already open. There is a book, 'The Princess Bride', inside.")
                                                else:
                                                        print ("You listen to the voices in your head and open the drawer. Inside you find a book, titled 'The Princess Bride'.\n")
                                                        time.sleep(b)
                                                        print ("Tantalized, you open it and read the first passage you see:")
                                                        print ("Fencing, fighting, torture, revenge, giants, monsters, chases, escapes, true love and miracles!\n")
                                                        print ("It seems oddly relevant to your situation.")
                                                        drawer = "open"
                                        elif "take" in action and "book" in action:
                                                if drawer == "open":
                                                        if "The Princess Bride" in Va.inventory:
                                                                 print ("You cannot take a book that is not there.")
                                                        else:
                                                                print("The book is now in your satchel.") #to give a response to that action
                                                                Va.inventory.append("The Princess Bride")

                                                else:
                                                        print ("You try to grasp something abstract, but it slipped through your fingers. Try taking something that's more real.\n")
                                        elif "take" in action and "book" not in action:
                                                print ("You try to grasp something abstract, but it slipped through your fingers. Try taking something that's more real.\n")
                                        elif "inventory" in action:
                                            print ("Inventory:                                   [%d/10][Satchel]" %(len(Va.inventory)))
                                            if len(Va.inventory) != 0:
                                                print (", ".join(Va.inventory))
                                            else:
                                                print ("Your satchel is empty.")
                                            print ("")
                                        elif "inspect" in action or "look" in action:
                                                if drawer == "open":
                                                        print ("You take a closer look at the opened drawer. Seems like an ordinary sockdrawer, made of dark oak and passed down through generations. It reminds you of times past.\n")
                                                else:
                                                        print ("You take a closer look at the drawer. Seems like an ordinary sockdrawer, made of dark oak and passed down through generations. It reminds you of times past.\n")
                                        elif "back" in action or "leave" in action:
                                                print ("You close the drawer and take a step back to the center of the room.\n")
                                                drawer = "closed"
                                                break
                                        else:
                                                print ("If you've lost intrest, why don't you take a step back, instead of trying to do something implausible with the drawer.") #Instead of this, have so if you misstype it prints "seems like you have lost intrest. perhaps you shouold take a step back."
                        elif "back" in action:
                                if Va.rooms[1] == "light":
                                        print ("You head back to the room you were in before.")
                                        return "light"
                                else:
                                    print ("You have only been in one room, you cannot go back yet.\n")
                        else:
                                if look == "no":
                                        print("Huh, that didn´t do anything")
                                        if clueless == 3:
                                                print("You suddenly feel the urge to look around. Express the urge!")
                                        elif clueless >= 4 and clueless <= 10:
                                                print("Express the urge")
                                        elif clueless >= 10:
                                                print("Normal human behavior is: looking around, inspecting different objects and walking in different directions.")
                                                print ("Write something sensible.\n")
                                        clueless += 1
                                else:
                                        if clueless < 3:
                                                print ("Huh, that didn't do anything.")
                                        else:
                                                print("Normal human behavior is: looking around, inspecting different objects and walking in different directions")
                                        clueless += 1
        elif room == "light":
                #Tog bort variabeln "light", onödig om man lägger till lampan till inventory.
                clueless = 0
                look = "no" #If you've looked around.
                if "Kerosene Lamp" in Va.inventory and Va.taken== "yes":
                        print ("You enter the room that holds the pig. There is nothing else in the room.")
                elif "Kerosene Lamp" in Va.inventory and Va.taken!= "yes":
                        print ("The room that was once lit up by the kerosene lamp is now only lit up by three glowing stones.")
                else:
                        print("Ten short steps and the light is in your reach. The light comes from a kerosene lamp.")
                while True:
                        action = input("What will you do? \n")
                        action = action.lower()
                        print ("")
                        if action == "look around":
                                look = "yes"
                                if Va.taken == "no":
                                        print("This room has three glowing stones with the colours blue, red and white, lying on a flying pig. The pig looks happy, but is stuck in the air by an unknown force.\n")
                                        print ("There is a door opposite to the dark room. The door seems closed.")

                                elif Va.taken == "yes" and "Kerosene Lamp" not in Va.inventory:
                                        print ("You look around. The room is lit up by a kerosene lamp.")
                                        print ("The only things apart from that are two doors, one leading to the dark room and one leading to the unknown. \nYou remember hearing a clicking sound.")
                                elif Va.taken == "yes" and "Kerosene Lamp" in Va.inventory:
                                        print ("You look around. The room is lit up by the kerosene lamp you hold.")
                                        print ("The only things in the room are two doors, one leading to the dark room and one leading to the unknown. \nYou remember hearing a clicking sound.")
                        elif "inventory" in action:
                                print ("Inventory:                                   [%d/10][Satchel]" %(len(Va.inventory)))
                                if len(Va.inventory) != 0:
                                    print (", ".join(Va.inventory))
                                else:
                                    print ("Your satchel is empty.")
                                print ("")
                        elif "dark room" in action or "back" in action:
                                print ("You go into the dark room.\n")
                                return "start"
                        elif "pet" in action and "pig" in action:
                                print("The pig seems pleased and oinks happily.\n")
                        elif action == "inspect":
                                print ("You inspect the dust in the air.\n")
                        elif "take" in action and "pig" in action:
                            print ("The pig is locked in place, you cannot take it with you. Even if you could move it, how would you fit it into your satchel?\n")
                        elif "pick" in action and "up" in action and "light" in action or "pick" in action and "up" in action and "lamp" in action:
                                if "Kerosene Lamp" not in Va.inventory:
                                        print("You pick up the light.")
                                        Va.inventory.append("Kerosene Lamp") #Adds Kerosene Lamp to inventory.
                                else:
                                        print ("You have already picked up the light.")
                        elif "take" in action and "lamp" in action or "take" in action and "light" in action or "take" in action and "kerosene" in action:
                                if "Kerosene Lamp" not in Va.inventory:
                                        print("You pick up the light.")
                                        Va.inventory.append("Kerosene Lamp")
                                else:
                                        print ("You have already picked up the light.")
                        elif "inspect" in action and "stone" in action or "take" in action and "stone" in action or "pick" in action and "stone" in action:
                                if Va.taken== "yes":
                                        print ("The stones are no longer there to interact with.")
                                else:
                                        print("\nYou touch the stones. \n\
The blue stone shows you a vision of stars. You feel like you are in a completely different world. \n\
The white stone tells you that you are chosen, special. Your faith is strong.\n\
The red stone makes you visualize your strenght and brute force. Strenght pulses in your veins.")
                                        while True:
                                                stone = input("\n\nPick up a stone of your chosing. \n") #Which stone you pick up.
                                                stone = stone.lower()
                                                print ("")
                                                if "blue" in stone:
                                                        print ("You take the blue stone and put it in your satchel.")
                                                        Va.clas = classes[0] #Your proffession (class) becomes classes[0].
                                                        Va.inventory.append("Mystic Stone")
                                                        break
                                                elif "white" in stone:
                                                        print ("You take the white stone and put it in your satchel.")
                                                        Va.clas = classes[2]
                                                        Va.inventory.append("Holy Stone")
                                                        break
                                                elif "red" in stone:
                                                        print ("You take the red stone and put it in your satchel.")
                                                        Va.clas = classes[1]
                                                        Va.inventory.append("Fierce Stone")
                                                        break
                                                else:
                                                        print("''%s' is not a stone."%(stone))
                                        print("Just as you take the stone off the pig's back, the other stones vanish. You hear a clicking sound from the door.")
                                        Va.taken = "yes"
                        elif "take" in action: #If "take" in action and you have not typed "light" or "stones" too.
                                                print ("You try to grasp something abstract, but it slipped through your fingers. Try taking something that's more real.\n")
                        elif "enter" in action or "door" in action or "unknown" in action:
                                if Va.taken == "yes":
                                        return "hallway"
                                else:
                                        print ("You approach the door, but it is locked. No matter how hard you hit it, it won't budge.\n")
                        else:
                          if look == "no":
                                print("Huh that didn´t work.") #to atleast give some response
                                clueless += 1
                                if clueless == 3:
                                        print("You suddenly feel the urge to look around. Express the urge!")
                                elif clueless >= 4 and clueless <= 10:
                                        print("Express the urge")
                                elif clueless >= 10:
                                        print("Normal human behavior is: looking around, inspecting different objects and walking in different directions")
                          else:
                                if clueless < 3:
                                        print ("Huh, that didn't work.")
                                else:
                                        print("Normal human behavior is: looking around, inspecting different objects and walking in different directions")
                                        clueless += 1

        elif room == "hallway":
                ####The door does not open if Va.rooms[1] == "courtyard", as it's possible you broke it and it gets repetetive!
                if "courtyard" in Va.allrooms:
                    if Va.clas == classes[1]: #If your class is Warrior
                        print ("You enter the manor, passing by the dust that once was a majestic door.\n")
                    else:
                        print ("You enter the manor.")
                else:
                    look = "no"
                    print("Just as you approach it, the door creaks open.")
                    time.sleep(a)
                    if "Kerosene Lamp" in Va.inventory:
                            print ("You take a step forwards to take a look, but suddenly the door slams shut! You're pushed into a hallway, \nilluminated only by your lamp. You can barely see the other end.")
                    else:
                            print ("You take a step forwards to take a look, but suddenly the door slams shut! You're pushed into a pitch black hallway.")
                while True:
                        forwards = "no"
                        action = input("What will you do? \n")
                        action = action.lower()
                        print ("")
                        if "look" in action or "inspect" in action and "trap" not in action:
                                look = "yes"
                                if Va.rooms[1] == "light":
                                    if "Kerosene Lamp" in Va.inventory:
                                        if forwards == "no":
                                            print ("You notice an open trapdoor two steps infront of you. The space below is filled with spikes and sharp poles.\n")
                                        else:
                                            print ("You notice an open trapdoor infront of the door to the Pig Room. The space below is filled with spikes and sharp poles.\n")
                                    else:
                                            print ("You look around, but see nothing in the thick darkness.")
                                else:
                                    print ("You notice an open trapdoor infront of the door to the Pig Room. The space below is filled with spikes and sharp poles.\n")
                        elif "inventory" in action:
                                print ("Inventory:                                   [%d/10][Satchel]" %(len(Va.inventory)))
                                if len(Va.inventory) != 0:
                                    print (", ".join(Va.inventory))
                                else:
                                    print ("Your satchel is empty.")
                                print ("")
                        elif "forward" in action or "further" in action or "courtyard" in action:#Man kunde inte skriva "elif "forward" or "further" in action:", det gjorde att alla block efter detta misslyckades.
                                forwards = "yes"
                                if "Kerosene Lamp" in Va.inventory:
                                    if "courtyard" not in Va.allrooms:
                                        if look == "yes":
                                                print("You step around the trapdoor, thanking your gods that you took the lamp when you had the chance.")
                                                print ("Making sure you don't activate any other traps, you make your way to the other end of the corridor.\n")
                                                print ("You are met with an intimidating door. You stare at it. Its icy face stares back.\n")
                                                time.sleep(c)
                                                if Va.clas == classes[0]:
                                                    print ("Deep in thought on how to proceed, you let your hand wander into your satchel, touching the blue stone.")
                                                    time.sleep(b)
                                                    print ("-Mellon!")
                                                    time.sleep(b)
                                                    print ("The door gives way to your powerful cry, revealing a dark night sky. \nWhat is up with this strange aura? You stumble outside and the door closes behind you.")
                                                    return "courtyard"
                                                elif Va.clas == classes[2]:
                                                    print ("Deep in thought on how to proceed, you let your hand wander into your satchel, touching the white stone.")
                                                    time.sleep(b)
                                                    print ("You close you eyes, whispering to the door: 'Open'.")
                                                    time.sleep(b)
                                                    print ("The door gives way to your soft prayer, revealing a dark night sky. \nWhat is up with this strange aura?  You stumble outside and the door closes behind you.")
                                                    return "courtyard"
                                                elif Va.clas == classes[1]:
                                                    print ("Deep in thought on how to proceed, you let your hand wander into your satchel, touching the red stone.")
                                                    time.sleep(b)
                                                    print ("In a fit of rage, you lash out, releasing a flurry of punches at the door.")
                                                    time.sleep(b)
                                                    print ("The now pulverized door gives way to your attack, revealing a dark night sky. \nWhat is up with this strange aura? You stumble outside and the door closes behind you.")
                                                    return "courtyard"
                                        else:
                                                print("You step forwards, suddenly jumping to the side as you notice a trapdoor just where you would have walked.")
                                                print ("You thank your gods that you took the lamp and saw the trapdoor when you did.\n")
                                                print ("Taking great care not to activate any hidden traps, you make your way to the end of the hallway.\n")
                                                print ("You are met with an intimidating door. You stare at it. It's icy face stares back.\n")
                                                time.sleep(c)
                                                if Va.clas == classes[0]:
                                                    print ("Deep in thought on how to proceed, you let your hand wander into your satchel, touching the blue stone.")
                                                    time.sleep(b)
                                                    print ("-Mellon!")
                                                    time.sleep(b)
                                                    print ("The door gives way to your powerful cry, revealing a dark night sky. \nWhat is up with this strange aura? You stumble outside and the door closes behind you.")
                                                    return "courtyard"
                                                elif Va.clas == classes[2]:
                                                    print ("Deep in thought on how to proceed, you let your hand wander into your satchel, touching the white stone.")
                                                    time.sleep(b)
                                                    print ("You close you eyes, whispering to the door: 'Open'.")
                                                    time.sleep(b)
                                                    print ("The door gives way to your soft prayer, revealing a dark night sky. \nWhat is up with this strange aura? You stumble outside and the door closes behind you.")
                                                    return "courtyard"
                                                elif Va.clas == classes[1]:
                                                    print ("Deep in thought on how to proceed, you let your hand wander into your satchel, touching the red stone.")
                                                    time.sleep(b)
                                                    print ("In a fit of rage, you lash out, releasing a flurry of punches at the door.")
                                                    time.sleep(b)
                                                    print ("The now pulverized door gives way to your attack, revealing a dark night sky. \nWhat is up with this strange aura? You stumble outside and the door closes behind you.")
                                                    return "courtyard"
                                    else:
                                        print ("You decide to go outside, to the courtyard. \n")
                                else:
                                        print("Two steps forwards. One moment, sudden anguish and in the next, nothing.\n")
                                        return "death"
                        elif "inspect" in action and "trap" in action: #Typing "inspect trapdoor" does not trigger this action...
                                print ("You lean over the trapdoor to get a better look. You see something valuable glittering in the depths.")
                        elif "decend" in action or "down" in action:
                                print ("Blinded by the prospect of valuables and treasure, you jump to your death.")
                                return "death"
                        elif "back" in action:
                            if Va.rooms[1] == "light":
                                print ("You try to open the door to the Pig Room, but it won't budge. Seems like entering was a one way trip.\n")
                            else:
                                print ("You decide to go back outside.\n")
                                return "courtyard"
                        else:
                            print("Huh, that didn´t do anything")
        elif room == "courtyard":
            body = "unlooted"
            print("The garden you enter looks like it has not seen daylight in decades.\n")
            while True:
                action = input("What will you do?\n") #Om vi vill ändra på frågan lite då och då tycker jag att vi antingen ändrar den radikalt eller ändrar den smått när något händer.
                #Nu när man blir kidnappad är ett perfekt tillfälle.
                action = action.lower()
                print ("")
                if action == "look around":
                    print("The garden has a high metal fence surrounding it. It is filled with decomposing dead trees and the absence of flowers stands out. On the opposite side of the garden is a gate.\n")
                    print ("The house, or rather the manor, is made of black wood and looks like it once belonged to a lord, but has since been abandoned. All you see outside the garden is a thick fog...\n")
                    print ("You see a man's decapitated body, lying on the floor next to his own severed head. A head, which at this time, has no name.")
                    print ("'I know his name.' escapes your lips.\n")
                elif "go to" and "gate" in action or "walk to" and "gate" in action or "go" in action and "outside" in action or "leave" in action:
                    if body == "looted":
                        print ("You walk to the gate and you still only see fog outside of the fence.")
                        while True:
                            yn = input("Want to open the gate? [Y/N]\n")
                            yn = yn.lower()
                            print ("")
                            if "y" in yn:
                                return "fog"
                            elif "n" in yn:
                                break
                    else:
                        print ("Perhaps you should look at the body first.")
                elif "body" in action:
                    body = "looted"
                    print ("You loot the body.")
                elif "inventory" in action:
                        print ("Inventory:                                   [%d/10][Satchel]" %(len(Va.inventory)))
                        if len(Va.inventory) != 0:
                            print (", ".join(Va.inventory))
                        else:
                            print ("Your satchel is empty.")
                        print ("")
                elif "back" in action:
                    if body == "looted":
                        print ("You try to open the door to the manor, but it's locked.")
                    else:
                        print ("You decide to go back into the house.")
                        return Va.rooms[1]
                else:
                    print ("Huh, that didn't do anything.") ## Add clueless?
        elif room == "fog":
            print ("You pierce the fog. Slowly but surely, with every step you take, the fog dissapates.")
            print ("After an amount of steps uncountable to mere mortals, the fog is gone.\n")
            print ("You turn around, expecting to see the manor's looming body, but you can only see dust, lingering for a moment until even the dust is gone.\n\nYou hear a faint, hammering sound.\n")
            useless = input("A thunderous voice booms: What is your wish?\n")
            print ("")
            useless = list(useless)
            useless.insert(1,useless[0].upper())
            useless.pop(0)
            useless = "".join(useless)
            #Make the first letter of useless into a upper case letter.
            print("The voice replies: '%s'? I'm not a genie! \nThe sound grows lowder."%(useless))
            time.sleep(b)
            print ("Suddenly everything goes dark.")
            time.sleep(b)
        elif room == "death":
                print ("Your journey has come to a tragic end.") #Man måste starta om spelet när man dör eller? Antingen det eller så finns det checkpoints
        else:
                print ("Oops, room did not have a name. Returning to the last room you were in...")
                time.sleep(3) #Should always be 3 and not c, since you don't want your computer to crash.
                return Va.rooms[1]
room = "start"
while room != "end":
        room = handle_room(room)
        Va.rooms.insert(0,room)
        Va.allrooms.append(room) #Lägg till rummet till en lista som har alla rum man har varit i
        if len(Va.rooms) > 2:
                Va.rooms.pop(2) #Ta bort objektet med index [2] från listan room.
input("\n\nPress the Enter key to exit.")
