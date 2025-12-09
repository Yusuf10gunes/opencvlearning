#import cv2
#import numpy as np 


# İmread ile okunmak istenen resmi okuyoruz ve picture değişkenine atıyoruz 
#picture = cv2.imread("resim.jpg")

#kesit = picture[150:450,500:900]
#picture[0:300,0:400] = kesit
# İm show ilede o resmi ekrana basıyoruz
#cv2.imshow("Kesit",kesit)    
#cv2.imshow("kibritler",picture)
# Pencere açıldıktan sonra herhangi bir tuşa basana kadar pencereyi görünür kılar.
#cv2.waitKey(0)
# Shape ile o görselin uzunluğunu gnişliğini ve bgr değerini öğreniriz
#print(picture.shape)
#Pencereleri kapattığıız zaman arka taraftaki tüm opencvleri kapatır.
#cv2.destroyAllWindows()

############################################################################################################

# import cv2
# import numpy as np 

# picture = cv2.imread("resim6.jpg")
# #kesit = picture[1000:2500,1000:2500]
# aynalanan_resim = cv2.copyMakeBorder(picture,100,100,100,100,cv2.BORDER_REFLECT)sa

# cv2.imshow("kahve ve kek",aynalanan_resim)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(aynalanan_resim.shape)

#############################################################################################################

# import cv2
# import numpy as np 

# picture = cv2.imread("hababam.jpg")

# halitat = picture[297:607,527:720]
# kemals = picture[534:734,540:611]
# #kemals = picture[]
# #cv2.imshow("hababam sinifi",halitat)
# #cv2.imshow("hababam sinifi",kemals)
# #cv2.imshow("hababam sinifi",tarıka)


# cv2.imshow("hababam sinifi",picture)


# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(picture.shape)

# print("dikey= 601,536 ,yatay=274,563")

#########################################################################################################

# import cv2 as cv
# import sys 

# img = cv.imread(cv.samples.findFile("hababam.jpg"))

# if img is None:
#     sys.exit("resim bulunamadı")

# cv.imshow("hababam sınıfı",img)
# k = cv.waitKey(0)
# if k == ord("s"):
#     cv.imwrite("habbam.png",img)

#######################################################################################
# import numpy as np
# import cv2 as cv
# import sys


# #Burda videocapture nesnesi oluşturuyoruz.
# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Kamera açılamadı")
#     sys.exit()
# while True:
#     #Kameradan frame'in başarıyla alınıp alınmadığını kontrol ediyoruz.
#     ret, frame = cap.read()
    
#     # Framei almadıysak çıkış yapıyoruz döngüyü kırıyoruz.
#     if not ret:
#         print("Frame_e erişemedik Çıkış yapılıyor")
#         break
#     #Burda frame'i griye çeviriyoruz 
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # Framei imshow ile ekrana basıyoruz
#     cv.imshow('frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break

# # herşey olduktan sonra yakalanan frameleri serbest bırakıyoruz.
# cap.release()
# cv.destroyAllWindows()


#########################################################################################

# import numpy as np
# import cv2 as cv
 
# cap = cv.VideoCapture(0)
 
# # Define the codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
 
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     frame = cv.flip(frame, 0)
 
#     # write the flipped frame
#     out.write(frame)
 
#     cv.imshow('frame', frame)
#     if cv.waitKey(1) == ord('q'):
#         break
 
# # Release everything if job is finished
# cap.release()
# out.release()
# cv.destroyAllWindows()

#########################################################################
import numpy as np 
import cv2 as cv


cap = cv.VideoCapture(0)

ret,frame = cv.read()