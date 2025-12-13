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
# import cv2 as cv
# import os
# import time
# import sys


# video_name = "/home/leviberkowitz/python_yen/video folder/video.mp4"

# # Video içe aktar : capture cap
# cap = cv.VideoCapture(video_name)
# if not cap.isOpened():
#     print("video açılamadı ")
#     sys.exit()
# print("genişlik:",cap.get(3))
# print("yükseklik:",cap.get(4))


# while True:
#     ret,frame = cap.read()
#     if ret == True:
#         time.sleep(0.01)#uyarı kullanmazsak çok hızlı akar
#         cv.imshow("Video",frame)
#     else:
#         break

#     if cv.waitKey(1) & 0xFF == ord("q"): 
#         break
# cap.release()
# cv.destroyAllWindows()

#######KAMERA AÇMA VE VİDEO KAYDI########################################################
# import cv2 as cv

# #capture
# cap = cv.VideoCapture(0)

# wiidth = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# print("height:",height,"width:",wiidth)

# # Video kaydet
# writer = cv.VideoWriter("video_kaydı.mp4",cv.VideoWriter_fourcc(*"DIVX"),20,(wiidth,height))

# while True:
#     ret,frame = cap.read()
#     cv.imshow("Video",frame)

#     #save
#     writer.write(frame)

#     if cv.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# writer.release()
# cv.destroyAllWindows()

########RESİM BOYUTLANDIRMA#####################################################################
# import cv2 as cv

# image = cv.imread("Lenna.png")

# print("Lenna resmi boyutu:",image.shape)
# cv.imshow("original",image)
# #resized
# image_resized = cv.resize(image,(800,800))
# print(image_resized.shape)
# cv.imshow("Resized image",image_resized)

# #kırp
# imgcroppe = image[:200,:200]
# cv.imshow("kirpik resim",imgcroppe)


# cv.waitKey(0)

#######RESME ŞEKİL VE METİN EKLEME###################################################################
import cv2 as cv
import  numpy as np 

#resim oluştur 
img= np.zeros((512,512,3),np.uint8)#siyah resim

print(img.shape)
cv.imshow("siyah",img)

#çizgi
# resim,başlangıç noktası ,bitiş noktası ,renk ,kalınlık
cv.line(img,(100,250),(512,512),(0,255,0),3)
cv.imshow("resim",img)


# dikdörtgen
#resim, başlangıç, bitiş ,renk
cv.rectangle(img,(0,0),(255,255),(255,0,0))
cv.imshow("dikdortgen",img)

#çember
# resim ,merkez,uarıçağı,rengi
cv.circle(img,(300,300),78,(0,0,255),cv.FILLED)
cv.imshow("cember",img)


#metin
# resim,başlangıç noktası,font,kalınlığı,renk 
cv.putText(img,"resim",(300,300),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255 ))

cv.imshow("metin",img)
cv.waitKey(0)