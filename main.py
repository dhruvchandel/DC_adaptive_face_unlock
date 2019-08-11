import new_Face
import identify_face
import del_pycache

condition = True

def ShowMenu() :
    print("\t\tMenu")
    print("1. Add a new Face")
    print("2. Scan Your Face")
    print("3. Exit")


while condition == True :
    ShowMenu()
    choice = int(input("Enter Your Choice"))
    try :
        if choice == 3 :
            condition = False
        if choice == 1 :
            new_Face.NewFace()
        if choice == 2 :
            print(identify_face.IdentifyFace())
    except :
        print("Hey Lets Re-run the program; Seems like some error occured !!!!")
    del_pycache.__pycache__deleter()
