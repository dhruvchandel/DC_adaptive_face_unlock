# Importing Libraries
import cv2
import os

def DirectoryMaker() :
    BASE_DIR = os.getcwd()
    VALID_FACES_DIR = os.path.join(BASE_DIR,"valid_faces")

    if os.path.exists(VALID_FACES_DIR) :
        pass 
    else :
        os.mkdir(VALID_FACES_DIR)

    Name = input("Enter Name Whose Face ID is Being Scanned : ")

    if os.path.exists(os.path.join(VALID_FACES_DIR,Name)) :
        print("Another Face ID With Same Name Exists")
    else :
        os.mkdir(os.path.join(VALID_FACES_DIR,Name))

    CURRENT_DIR = os.path.join(VALID_FACES_DIR,Name)   #Directory In which new face's features will be stored
    os.mkdir(os.path.join(CURRENT_DIR,"face_id_pics"))
    CURRENT_DIR_FACES = os.path.join(CURRENT_DIR,"face_id_pics") #directory in which face images will be stored
    return CURRENT_DIR_FACES, BASE_DIR


def NewFace():
    CURRENT_DIR_FACES, BASE_DIR = DirectoryMaker()
    vidcap = cv2.VideoCapture(0)
    n = 0 
    lim = 0 

    while True :
        new_face = ()

        _, frame = vidcap.read()

        #Detecting faces in the frames captured and storing their co-ordinates in 
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        new_face = face_cascade.detectMultiScale(grayscale_frame,1.1,5)
        print(new_face)
        

        #Drawing the Boundries Around the Face
        for(x,y,w,h) in new_face :
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

        #Extracting the Face Out of Whole image
        if len(new_face) != 0 :
            offset = 10
            x,y,w,h = new_face[0]
            # face_only = frame[y-offset:y+h+offset ,x-offset:x+w+offset+30]
            # face_only = cv2.resize(face_only,(100,100)) 
            if lim < 10 :
                os.chdir(CURRENT_DIR_FACES)
                cv2.imwrite("f"+str(lim)+".jpg", frame)
                lim = lim+1
                os.chdir(BASE_DIR)

        if len(new_face) != 0 : 
            n = n+1

        if n == 10 :
            print("Face Captured Successfully !!!")
            print("Press 'y' to exit ...")
        
        if _ == False :
            continue 

        cv2.imshow("New Face", frame)
        # if len(new_face) != 0 :
        #     cv2.imshow("Extracted_Face", face_only)   

        if cv2.waitKey(1) & 0xFF == ord('y'):
            vidcap.release()
            cv2.destroyAllWindows()
            break


