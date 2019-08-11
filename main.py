import new_Face
import identify_face

condition = True

def ShowMenu() :
    print("\t\tMenu")
    print("1. Add a new Face")
    print("2. Scan Your Face")
    print("3. Exit")


while condition == True :
    ShowMenu()
    choice = int(input("Enter Your Choice"))
    if choice == 3 :
        condition = False
    if choice == 1 :
        new_Face.NewFace()
    if choice == 2 :
        print(identify_face.IdentifyFace())