import webbrowser

print(" *** YOU HAVE ENTERED THE PYTHON LAIR, NOW YOU MUST ANSWER SOME QUESTIONS *** ")
name = input("Who DARES Enters my Realm? ")
#imput name and capitalize the first letter. if you want to capitalize 2 names use title instead.
print("Ahhhhhhhhh", name.title() + ",")
#input age with different outcomes. < Or > "greater than or equal to" is the key phrase  for the  >= operator
while True:
    try:
        age = int(input("And what is your age? "))
        if age >=30:
            print()
            if age >=99:
                print()
                age = int(input("No...Really. How old are you? "))
                if age >=99:
                    print()
                    print("My God you are old. ")
            elif age <=99:
                print("Well..You are never to old to learn.")
        elif age <=31:
            if age >=5:
                print ()
                print("I remember when i was that age. ")
            elif age <=4:
                print("You can't trick me Human! ")
                age = int(input("What is your age and this time don't tell fibs? "))
                if age <=4:
                    print()
                    print("OK smarty, you're",age,"years old.")
        break
    except ValueError:
        print("Use only numbers")
# triple quotes allows to span over multiple lines
print('''Now what brings a puny programmer like you to the realm of Python?

1: I'm not sure?
2: I want to learn Python
3: My brain is exploding
''')

try:
    selection = int(input("Choose Wisely: "))
    web = webbrowser.open
    while selection not in range(1, 4):
        selection = int(input("Don't try and trick me Human, choose the 3 listed above: "))
    if selection == 1:
        print('''
        1: I wish to learn Python
        2: I'm just not sure!''')
        sel = int(input("What will it be? "))
        while sel not in range(1, 3):
            sel = print(web("https://www.youtube.com/watch?v=hSbtDuFJF6U"))
            break
        if sel == 1:
            print(web("www.youtube.com/watch?v=X5G_rB9ZMLc"))
        elif sel == 2:
            print (web("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
    elif selection == 2:
        print(web("https://www.tutorialspoint.com/python3/index.htm"))
    elif selection == 3:
        print(web("https://www.youtube.com/watch?v=A_MnyV-HH3U"))
except ValueError:
    print("Use only numbers")