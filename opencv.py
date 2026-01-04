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
# import cv2 as cv
# import  numpy as np 

# #resim oluştur 
# img= np.zeros((512,512,3),np.uint8)#siyah resim

# print(img.shape)
# cv.imshow("siyah",img)

# #çizgi
# # resim,başlangıç noktası ,bitiş noktası ,renk ,kalınlık
# cv.line(img,(100,250),(512,512),(0,255,0),3)
# cv.imshow("resim",img)


# # dikdörtgen
# #resim, başlangıç, bitiş ,renk
# cv.rectangle(img,(0,0),(255,255),(255,0,0))
# cv.imshow("dikdortgen",img)

# #çember
# # resim ,merkez,uarıçağı,rengi
# cv.circle(img,(300,300),78,(0,0,255),cv.FILLED)
# cv.imshow("cember",img)


# #metin
# # resim,başlangıç noktası,font,kalınlığı,renk 
# cv.putText(img,"resim",(300,300),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255 ))

# cv.imshow("metin",img)
# cv.waitKey(0)

#######GÖRÜNTÜLERİN BİRLEŞTİRİLMESİ ##########################################

# import cv2 as cv
# import numpy as np 
# img = cv.imread("Lenna.png")
# cv.imshow("Lenna",img)

# #Yatay 
# hor = np.hstack((img,img))
# cv.imshow("Yatay",hor)
# #Dikey
# ver = np.vstack((img,img))
# cv.imshow("Dikey",ver)


# cv.waitKey(0)

####PERSPEKTİF AYARLAMA###########################################################
# import cv2 as cv
# import numpy as np 
# #resmi içeri aktar
# img = cv.imread("kart.png")
# cv.imshow("orijinal",img)
# width = 400
# height = 500
# pts1 = np.float32([[230,1],[1,472],[540,150],[338,617]])
# pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

# matrix = cv.getPerspectiveTransform(pts1,pts2)
# print(matrix)
# img_out_put = cv.warpPerspective(img,matrix,(width,height))
# cv.imshow("donusturulmus",img_out_put)
# cv.waitKey(0)

##################GÖRÜNTÜLERİ KARIŞTIRMAK##########################################################
# import cv2 as cv
# import matplotlib.pyplot as plt 
# import numpy as np 

 
# img1 = cv.imread("img1.jpg")
# img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)
# img2 = cv.imread("img2.jpg")
# img2 = cv.cvtColor(img2,cv.COLOR_BGR2RGB) 



# plt.figure()
# plt.imshow(img1)

# plt.figure()
# plt.imshow(img2)    
# plt.show()
# print(img1.shape)
# print(img2.shape)
# img1 = cv.resize(img1,(600,600))
# img2 = cv.resize(img2,(600,600))
# print(img1.shape)
# print(img2.shape)


# plt.figure()
# plt.imshow(img1)

# plt.figure()
# plt.imshow(img2)
# plt.show()

# # karıştırılmış resim = alpha*img1 + beta*img2
# blended_picture = cv.addWeighted(src1=img1,alpha=0.5,src2=img2,beta = 0.5,gamma=0)
# plt.figure()
# plt.imshow(blended_picture)
# plt.show()
#############3 GÖRÜNTÜ EŞİKLEME################################################
# import cv2 as cv
# import matplotlib.pyplot as plt 

# #resmi içeri aktar 
# img = cv.imread("img1.jpg") 
# img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# plt.figure() 
# plt.imshow(img, cmap="gray")
# plt.axis("off")

# #eşikleme
# _, thresh_img = cv.threshold(img,thresh=60,maxval=255,type=cv.THRESH_BINARY)
# plt.figure()
# plt.imshow(thresh_img,cmap="gray")
# plt.axis("off")

# thresh_img2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,8)
# plt.figure()
# plt.imshow(thresh_img2,cmap="gray")
# plt.axis("off")
# plt.show()

#######BULANIKLAŞTIRMA##################################################################
import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np 
import warnings
warnings.filterwarnings("ignore")

# # blurring (detayı azaltır ve gürültüyü engeller)
# img = cv.imread("nyc.jpg")
# img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# plt.figure()
# plt.imshow(img),plt.axis("off"),plt.title("orijinal")

# # Ortalama bulanıklaştırma yöntemi

# dst2 = cv.blur(img,ksize=(3,3))
# plt.figure(),plt.imshow(dst2),plt.axis("off"),plt.title("ortalama blur")

# # Gausian blur
# gb = cv.GaussianBlur(img,ksize=(3,3),sigmaX=7) 
# plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("gausian blur")

# #Medyan blur
# mb = cv.medianBlur(img,ksize=3)
# plt.figure(),plt.imshow(mb),plt.axis("off"),plt.title("median blur"),plt.show()


# def gaussian_noise(image):
#     row , col, ch = image.shape
#     mean = 0
#     var = 0.05
#     sigma = var**0.5
#     gauss = np.random.normal(mean,sigma,(row,col,ch))
#     gauss = gauss.reshape(row,col,ch)
#     noisy = image + gauss
#     return noisy

# #içe aktar normalize et
# img = cv.imread("nyc.jpg")
# img = cv.cvtColor(img,cv.COLOR_BGR2RGB)/255
# plt.figure()
# plt.imshow(img),plt.axis("off"),plt.title("orijinal"),plt.show()
# gaussian_noisy_image = gaussian_noise(img)
# plt.imshow(gaussian_noisy_image),plt.axis("off"),plt.title("gausiiian noise"),plt.show()
# # gauss blur
# gb2 = cv.GaussianBlur(gaussian_noisy_image,ksize=(3,3),sigmaX=7) 
# plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title("with gausian blur işlemi"),plt.show()

# def salt_pepper_noise(image):
#     row,col,ch = image.shape
#     s_vs_p = 0.5
#     amount = 0.004
#     noisy = np.copy(image)

#     # salt beyaz
#     num_salt = np.ceil(amount*image.size*s_vs_p)
#     coords = [np.random.randint(0,i-1,int(num_salt))for i in image.shape]
#     noisy[coords] = 1

#     #pepper siyah
#     num_pepper = np.ceil(amount*image.size*(1 - s_vs_p))
#     coords = [np.random.randint(0,i-1,int(num_pepper))for i in image.shape]
#     noisy[coords] = 0
#     return noisy

# sp_image = salt_pepper_noise(img)
# plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title("SP image"),plt.show()
# sp_uint8 = (sp_image * 255).astype(np.float32)
# mb2 = cv.medianBlur(sp_uint8, ksize=3) 
# plt.figure(),plt.imshow(mb2),plt.axis("off"),plt.title("SP image mbulur"),plt.show()    

######## MORFOLOJİK OPERASYONLAR########################################################
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("datai_team.jpg",0) 
plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off"),plt.title("original image")

#erozyon
kernel = np.ones((5,5),dtype = np.uint8)
result = cv.erode(img,kernel, iterations = 1)
plt.figure(),plt.imshow(result,cmap="gray"),plt.axis("off"),plt.title("erozyon")


# genişleme dialation
result2 = cv.dilate(img,kernel,iterations=1)
plt.figure(),plt.imshow(result2,cmap="gray"),plt.axis("off"),plt.title("genisletilmis"),plt.show()

# white noise
white_noise = np.random.randint(0,2, size = img.shape[:2])
white_noise = white_noise*255
plt.figure(),plt.imshow(white_noise,cmap="gray",),plt.axis("off"),plt.title("Beyaz gürültü"),plt.show()
noise_image = white_noise + img
plt.figure(),plt.imshow(noise_image,cmap="gray",),plt.axis("off"),plt.title("Beyaz gürültü "),plt.show()
