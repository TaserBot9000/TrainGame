#make train line game
#name train line
#ask what stop should be named
#start with a stop, "<["name of stop"]>"
#ask for distance, one - is one kilometer

stopName = ""
distance = 0
yourLine = ""
a = True
b = True

print("Rules of the Game\n1)Start with one stop, give it a name.\n2)Each \"-\" is a kilometer\n3)Game start")

stopName = input("Name of first stop -> ")
while b == True:
    try:
        distance = int(input("How many kilometers to next stop -> "))
        break
    except:
        print("Please enter a number.")
yourLine+="<[" + stopName + "]>"
for i in range(distance):
    yourLine+="-"    
print("Current progress -> " + yourLine)

running = True

while running == True:
    stopName = input("Name of the next stop -> ")
    while b == True:
        try:
            distance = int(input("How many kilometers to next stop -> "))
            break
        except:
            print("Please enter a number.")
    yourLine+="<[" + stopName + "]>"
    for i in range(distance):
        yourLine+="-"    
    print("Current progress -> " + yourLine)
    while a == True:
        keepPlaying = input("Keep playing? (y/n) -> ").lower()
        if keepPlaying == "y":
            a = False
        elif keepPlaying == "n":
            break
        else:
            print("Please try again.")
    a = True
lastStation = input("Name of the last stop -> ")
nameOfLine = input("Please enter the name of your line -> ")
print(nameOfLine + " ==>> " + yourLine + "<[" + lastStation + "]>")            
            
