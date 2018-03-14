#Commands: Look around, inspect, take, pick up, go west, east, north and south, climb, descend look left and right, go forward, backwards left and right
#Created by Joar and Johan, started 08 march 2018
#b6f2d495-1587-4b34-8b6f-ebe48199aa17
#Fiara text game
import time
import Va #Variables
#Defining all the classes:
#Listor funkar om man definerar dem utanför funktionen, variablar gör inte det.
c, r = 5, 3 #Number of tags, number of classes.
classes = [[0 for x in range(c)] for y in range(r)]
#classes[0] is one class, [1] another etc.
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
                clueless = 0
                look = "no"
                if "Kerosene Lamp" in Va.inventory:
                        print ("The dark room is lit up by the lamp you picked up.\n")
                else:
                        print ("The room is dark. You see a lamp in an adjacent room.\n")
                while True:
                        action = input("What will you do? \n")
                        action = action.lower()
                        if action == "look around":
                                #When you look around this happens
                                look = "yes"
                                print ("You look around. The eerie silence crushes your eardrums. \
You are standing in a stone room made of bricks.\n\n\
There is a sockdrawer in the corner. The light in the other room seems miles away. \n")
                        elif "light" in action or "room" in action or "lamp" in action:
                                return "light"
                        #elif action == "vi är bäst": dröm om at hoppa till vilket rum man vill
                            #inventory.append("Kerosene Lamp")#, "Mystic Stone", "The Princess Bride"
                            #return input("Enter room to teleport\n")
                        elif action == "ca":
                            return "courtyard"
                        elif "inventory" in action:
                            print ("Inventory:                                   [%d/10][Satchel]")
                            print (", ".join(Va.inventory))
                                #breaking the loop and you walk into the next room
                        elif "drawer" in action: #This includes "sockdrawer", since "sockdrawer" contains "drawer".
                                print ("You approach the mystical drawer. It gives of an aura of adventure.\n")
                                #Princess bride easter egg which will affect the story later
                                while True:
                                        action = input ("What will you do?\n")
                                        print ("YOure stucke!")#####
                                        action = action.lower()
                                        if "open" in action:
                                                if Va.drawer == "open":
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
                                                        Va.drawer = "open"
                                        elif "take" in action and "book" not in action:
                                                print ("You try to grasp something abstract, but it slipped through your fingers. Try taking something that's more real.\n")
                                        elif "take" in action and "book" in action:
                                                if drawer == "open":
                                                        if "The Princess Bride" in Va.inventory:
                                                                 print ("You cannot take a book that is not there.")
                                                        else:
                                                                print("The book is now in your satchel.") #to give a response to that action
                                                                Va.inventory.append("The Princess Bride")

                                                else:
                                                        print ("You try to grasp something abstract, but it slipped through your fingers. Try taking something that's more real.\n")
                                        elif "inspect" in action or "look" in action:
                                                if Va.drawer == "open":
                                                        print ("You take a closer look at the opened drawer. Seems like an ordinary sockdrawer, made of dark oak and passed down through generations. It reminds you of times past.\n")
                                                else:
                                                        print ("You take a closer look at the drawer. Seems like an ordinary sockdrawer, made of dark oak and passed down through generations. It reminds you of times past.\n")
                                        elif "back" in action or "leave" in action:
                                                print ("You take a step back, to the center of the room.\n")
                                                break
                                        else:
                                                print ("If you've lost intrest, why don't you take a step back, instead of trying to do something implausible with the drawer.") #Instead of this, have so if you misstype it prints "seems like you have lost intrest. perhaps you shouold take a step back."
                        elif "back" in action:
                                if Va.rooms[1] == "light":
                                        print ("You head back to the room you were in before.")
                                        return "light"
                        else:
                                if look == "no":
                                        print("Huh, that didn´t do anything")
                                        if clueless == 3:
                                                print("You suddenly feel the urge to look around. Express the urge!")
                                        elif clueless >= 4 and clueless <= 10:
                                                print("Express the urge")
                                        elif clueless >= 10:
                                                print("Normal human behavior is: looking around, inspecting different objects and walking in different directions")
                                                print ("Write something sensible.")
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
                        if action == "look around":
                                look = "yes"
                                if Va.taken == "no":
                                        print("This room has three glowing stones with the colours blue, red and white, \
lying on a flying pig. The pig looks happy, but is stuck in the air by an unknown force.\n")
                                        print ("There is a door opposite to the dark room. The door seems closed.")

                                elif Va.taken == "yes" and "Kerosene Lamp" not in Va.inventory:
                                        print ("You look around. The room is lit up by a kerosene lamp.")
                                        print ("The only things apart from that are two doors, one leading to the dark room and one leading to a pitch black hallway.")
                                elif Va.taken == "yes" and "Kerosene Lamp" in Va.inventory:
                                        print ("You look around. The room is lit up by the kerosene lamp you hold.")
                                        print ("The only things in the room are two doors, one leading to the dark room and one leading to a pitch black hallway.")
                        elif "inventory" in action:
                                print ("Inventory:                                   [%d/10][Satchel]" %(len(Va.inventory)))
                                print (", ".join(Va.inventory))
                        elif "dark room" in action:
                                print ("You go into the dark room.")
                                return "start"
                        elif "back" in action:
                                if Va.rooms[1] == "start":
                                        print ("You go back into the dark room.")
                                        return "start"
                        elif "pet" in action and "pig" in action:
                                print("The pig seems pleased and oinks happily.")
                        elif action == "inspect":
                                print ("You inspect the dust in the air.")
                        elif "pick" in action and "up" in action and "light" in action or "pick" in action and "up" in action and "lamp" in action:
                                if "Kerosene Lamp" not in Va.inventory:
                                        print("You pick up the light.")
                                        Va.inventory.append("Kerosene Lamp") #Adds Kerosene Lamp to inventory.
                                else:
                                        print ("You have already picked up the light.")
                        elif "take" in action and "lamp" in action or "take" in action and "light" in action:
                                if "Kerosene Lamp" not in Va.inventory:
                                        print("You pick up the light.")
                                        Va.inventory.append("Kerosene Lamp")
                                else:
                                        print ("You have already picked up the light.")
                        elif "inspect" in action and "stone" in action or "take" in action and "stone" in action or "pick" in action and "stone" in action:
                                if Va.taken== "yes":
                                        print ("The stones are no longer there to interact with.")
                                else:
                                        print("You touch the stones. \n\
The blue stone shows you a vision of stars and it feels like you are in a completely different world. \n\
The white stone makes you believe that you are the chosen and your faith is strong.\n\
The red stone makes you visualize your strenght and brute force. You feel strong.")
                                        while True:
                                                stone = input("\n\nPick up a stone of your chosing. \n") #Which stone you pick up.
                                                stone = stone.lower()
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
                                                        print("Pick a stone of your chosing")
                                        print("Just as you take the stone off the pig's back, the other stones vanish. You hear a clicking sound from the door.")
                                        Va.taken = "yes"
                        elif "take" in action: #If "take" in action and you have not typed "light" or "stones" too.
                                                print ("You try to grasp something abstract, but it slipped through your fingers. Try taking something that's more real.\n")
                        elif "enter" in action or "door" in action:
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
                look = "no"
                print("Just as you approach it, the door creaks open.")
                time.sleep(a)
                if "Kerosene Lamp" in Va.inventory:
                        print ("You take a step forwards to take a look, but suddenly the door slams shut! You're pushed into a hallway, \
illuminated only by your lamp. You can barely see the other end.")
                else:
                        print ("You take a step forwards to take a look, but suddenly the door slams shut! You're pushed into a pitch black hallway.")
                while True:
                        forwards = "no"
                        action = input("What will you do? \n")
                        action = action.lower()
                        if "look" in action or "inspect" in action:
                                look = "yes"
                                if "Kerosene Lamp" in Va.inventory:
                                    if forwards == "no":
                                        print ("You notice an open trapdoor two steps infront of you. The space below is filled with spikes and sharp poles.\n")
                                    else:
                                        print ("You notice an open trapdoor infront of the door from the Pig Room. The space below is filled with spikes and sharp poles.\n")
                                else:
                                        print ("You look around, but see nothing in the thick darkness.")#######
                        elif "inventory" in action:
                                print ("Inventory:                                   [%d/10][Satchel]" %(len(Va.inventory)))
                                print (", ".join(Va.inventory))
                        elif "forward" or "further" in action:
                                forwards = "yes"
                                if "Kerosene Lamp" in Va.inventory:
                                        if look == "yes":
                                                print("You step around the trapdoor, thanking your gods that you took the lamp when you had the chance.\
Making sure you don't activate any other traps, you make your way to the other end of the corridor.\n \
You are met with an intimidating door. You stare at it. Its icy face stares back.")
                                                time.sleep(c)
                                                if Va.clas == classes[0]:
                                                    print ("You let your hand wander into your satchel, touching the blue stone.")
                                                    time.sleep(b)
                                                    print ("-Mellon!")
                                                    time.sleep(b)
                                                    print ("The door gives way to your powerful cry, revealing a dark night sky. What is up with this strange aura? You stumble outside and the door closes behind you.")
                                                    return "courtyard"
                                                elif Va.clas == classes[2]:
                                                    print ("You let your hand wander into your satchel, touching the white stone.")
                                                    time.sleep(b)
                                                    print ("You close you eyes, whispering to the door: 'Open'.")
                                                    time.sleep(b)
                                                    print ("The door gives way to your soft prayer, revealing a dark night sky. What is up with this strange aura?  You stumble outside and the door closes behind you")
                                                    return "courtyard"
                                                elif Va.clas == classes[1]:
                                                    print ("You let your hand wander into your satchel, touching the red stone.")
                                                    time.sleep(b)
                                                    print ("In a fit of rage, you lash out, releasing a flurry of punches at the door.")
                                                    time.sleep(b)
                                                    print ("The now pulverized door gives way to your attack, revealing a dark night sky. What is up with this strange aura? You stumble outside and the door closes behind you")
                                                    return "courtyard"
                                        else:
                                                print("You step forwards, suddenly jumping to the side as you notice a trapdoor just where you would have walked. You thank your gods that you took the lamp and saw the trapdoor \
when you did. Taking great care not to activate any hidden traps, you make your way to the end of the hallway.\n \
You are met with an intimidating door. You stare at it. It's icy face stares back.")
                                                time.sleep(c)
                                                if Va.clas == classes[0]:#### smart
                                                    print ("You let your hand wander into your satchel, touching the blue stone.")
                                                    time.sleep(b)
                                                    print ("-Mellon!")
                                                    time.sleep(b)
                                                    print ("The door gives way to your powerful cry, revealing a dark night sky. What is up with this strange aura? You stumble outside and the door closes behind you")
                                                    return "courtyard"
                                                elif Va.clas == classes[2]:
                                                    print ("You let your hand wander into your satchel, touching the white stone.")
                                                    time.sleep(b)
                                                    print ("You close you eyes, whispering to the door: 'Open'.")
                                                    time.sleep(b)
                                                    print ("The door gives way to your soft prayer, revealing a dark night sky. What is up with this strange aura? You stumble outside and the door closes behind you")
                                                    return "courtyard"
                                                elif Va.clas == classes[1]:
                                                    print ("You let your hand wander into your satchel, touching the red stone.")
                                                    time.sleep(b)
                                                    print ("In a fit of rage, you lash out, releasing a flurry of punches at the door.")
                                                    time.sleep(b)
                                                    print ("The now pulverized door gives way to your attack, revealing a dark night sky. What is up with this strange aura? You stumble outside and the door closes behind you")
                                                    return "courtyard"
                                else:
                                        print("Two steps forwards. One moment, sudden anguish and in the next, nothing.\n")
                                        return "death"
                        elif "inspect" in action and "trap" in action:
                                print ("You lean over the trapdoor to get a better look. You see something valuable glittering in the depths.")
                        elif "decend" in action or "down" in action:
                                print ("Blinded by the prospect of valuables and treasure, you jump to your death.")
                                return "death"
                        else:
                            print("Huh, that didn´t do anything")
        elif room == "courtyard":
            print("The garden you enter looks like it has not seen daylight in many years.")
            while True:
                action = input("What shall you do? ")
                action = action.lower()
                if action == "look around":
                    print("The garden has a high metal fence sorrounding it. It is filled with decomposing dead trees and an absence of flowers is noticable. On the opposite side of the garden is a gate. \
\nThe house, or rather the manor, is made of black wood and looks like it once belonged to a lord, but has since been abandoned. All you see outside the garden is a thick fog...")
                elif "go to" and "gate" in action or "walk to" and "gate" in action:
                    print ("You walk to the gate and you still only see fog outside of the fence.")
                    while True:
                        yn = input("Want to open the gate? (y/n) ")
                        yn = yn.lower()
                        if "y" in yn:
                            return "fog"
                        elif "n" in yn:
                            break
                elif "inventory" in action:
                        print ("Inventory:                                   [%d/10][Satchel]" %(len(Va.inventory)))
                        print (", ".join(Va.inventory))
                elif "back" in action:
                        print ("You decide to go back into the house.")
                        return Va.rooms[1]
        elif room == "fog":
            print ("You pierce the fog. Slowly but surely, with every step you take, the fog dissapates. After an amount of steps uncountable to mere mortals, the fog is gone. \
You turn around, expecting to see the manor's looming body, but you can only see dust, lingering for a moment until even the dust is gone.")
            useless = input("A thunderous voice states: What is your wish to make happen?\n")
            print("The voice states: Im not a genie you silly bastard. You hear a earth-shattering . Suddenly everything goes dark.")
        elif room == "death":
                print ("Your journey has come to a tragic end.") #Man måste starta om spelet när man dör eller? Antingen det eller så finns det checkpoint
        else:
                print ("Oops, room did not have a value. Returning to the last room you were in...")
                time.sleep(3)
                return Va.rooms[1]
room = "start"
while room != "end":
        room = handle_room(room)
        Va.rooms.insert(0,room)
        Va.allrooms.append(room) #Lägg till rummet till en lista som har alla rum man har varit i
        if len(Va.rooms) > 2:
                Va.rooms.pop(2) #Ta bort objektet med index [2] från listan room.
input("\n\nPress the Enter key to exit.")
