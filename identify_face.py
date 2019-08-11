import face_recognition
import os, glob
import cv2
import time


def IdentifyFace() :
    BASE_DIR = os.getcwd()
    VALID_FACES_DIR = os.path.join(BASE_DIR,"valid_faces")
    os.chdir(BASE_DIR)

    # We will take in input an image of the person sitting in the car capture one of the image of his 
    # and perform testing on it 
    if os.path.exists(os.path.join(BASE_DIR, "scan_user_id")) == False :
        os.mkdir(os.path.join(BASE_DIR, "scan_user_id"))
    os.chdir(os.path.join(BASE_DIR, "scan_user_id"))
    print("Please keep your face still")
    vidcap = cv2.VideoCapture(0)
    time.sleep(1.5)
    _, face_id_under_scan = vidcap.read()
    cv2.imwrite("faceIDunderScan.png", face_id_under_scan)
    vidcap.release()
    path2scanningFaceID = os.path.join(os.path.join(BASE_DIR,"scan_user_id"), "faceIDunderScan.png")
    # Current Face_ID to be scanned Stores Successfully


    # Now , the deafult directory is face_detection_startup
    # We will open the camera wait for like 4 seconds and take a picture , 
    # and detect find a suitable match for it if not found till last we will return a zero 
    #  if found we will break it immidiately and and return 1

    #below is the sequence to go through all the images of all the user id's
    true_id_detected = "Match Not Found"
    unknown_image = face_recognition.load_image_file(path2scanningFaceID)
    for user_id_names in os.listdir(VALID_FACES_DIR) :
        if user_id_names[0] != '.' :
            path = os.path.join(VALID_FACES_DIR, user_id_names)
            for face_id_directory in os.listdir(path) :
                if face_id_directory[0] != '.' :
                    path1 = os.path.join(path, face_id_directory)
                    flag = False
                    n_correct = 0
                    n_false = 0
                    # print(path1)
                    os.chdir(path1)
                    # print(os.path.join(path1,"face_id_pics"))
                    files = glob.glob("*.jpg")
                    files.sort(key=os.path.getmtime)
                    # print(files)
                    for face_id_pics in files :
                        if face_id_pics[0] != '.' :
                            # here comes each and every image with image path os.path.join(path1, face_id_pics)
                            known_image = face_recognition.load_image_file(os.path.join(path1, face_id_pics))
                            try :
                                biden_encoding = face_recognition.face_encodings(known_image)[0]
                                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                                # results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
                                if (float(face_recognition.face_distance([biden_encoding], unknown_encoding))) <= 0.53 :
                                    results = True
                                else :
                                    results = False
                                print(results)
                                if results == True :
                                    n_correct += 1
                                else :
                                    n_false +=1
                                if n_false >= 4 :
                                    break
                                if n_correct >= 6 :
                                    flag = True 
                                    true_id_detected = "Hello " + user_id_names
                                    os.remove(os.path.join(path1, files[0]))
                                    print(str(files[0]))
                                    cv2.cvtColor(face_id_under_scan, cv2.COLOR_BGR2RGB)
                                    cv2.imwrite(str(files[0]), face_id_under_scan)
                                    break
                            except :
                                pass
    os.remove(os.path.join(os.path.join(BASE_DIR, "scan_user_id"),"faceIDunderScan.png"))
    return true_id_detected
