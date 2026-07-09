homework = set()
p_ai = set()
while True:
    print ("1 , add number")
    print("2 , remine number")
    print(" 3 , show number")
    print("4 , show member")
    print("5 , show all member")
    print("6 , member in one club")
    print(" 7 , search a member")
    print("exit / close ")
    choose = int(input("enter your choice :"))
    if choose == "1 ":
        name = input("enter nmae")
        club = input("programming/ ai / cyber")
        elif club == "ai":
            ai.add(name)
        elif club == "cyber":
            cyber.add(name)
        if choose == " 2 ":
        name = input("enter nmae")
        club = input("programming/ ai / cyber")
    elif club == "ai":
        ai.add(name)
    elif club == "cyber":
        cyber.add(name)
    if choose == "3 ":
        name = input("enter nmae")
        club = input("programming/ ai / cyber")
    elif club == "ai":
        ai.add(name)
    elif club == "cyber":
        cyber.add(name)
