# print(os.name)

# current_dir = os.getcwd()
# print("Current directory:", current_dir)

# folder_name = "new_folder"
# new_folder_name = "new_folder2"

# # Klasör yoksa oluştur
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
#     print("Klasör oluşturuldu:", folder_name)

# # Yeniden adlandır
# if os.path.exists(folder_name):
#     os.rename(folder_name, new_folder_name)
#     print("Klasör yeniden adlandırıldı:", new_folder_name)
# else:
#     print("Klasör bulunamadı!")

# # Yeni klasöre geç
# os.chdir(os.path.join(current_dir, new_folder_name))
# print("Yeni dizine geçildi:", os.getcwd())

# files = os.listdir()
# for f in files:
#     if f.endswith(".py"):
#         print(f) 

# print(os.path.exists("opencvlearn.py"))

############################################################################################################
# import cv2 as cv

# img = cv.imread("hababam.jpg",0)

# cv.imshow("haababm sınıfı",img)

# k = cv.waitKey(0) & 0xFF

# if k == 27:
#     cv.destroyAllWindows()
# elif k == ord('s'):
#     cv.imwrite("hababam.png",img)
#     cv.destroyAllWindows()

###############################################################################################################
import cv2 as cv
import os
import time
import sys


video_name = "/home/leviberkowitz/python_yen/video folder/video.mp4"

# Video içe aktar : capture cap
cap = cv.VideoCapture(video_name)
if not cap.isOpened():
    print("video açılamadı ")
    sys.exit()
print("genişlik:",cap.get(3))
print("yükseklik:",cap.get(4))


while True:
    ret,frame = cap.read()
    if ret == True:
        time.sleep(0.01)#uyarı kullanmazsak çok hızlı akar
        cv.imshow("Video",frame)
    else:
        break

    if cv.waitKey(1) & 0xFF == ord("q"): 
        break
cap.release()
cv.destroyAllWindows()
