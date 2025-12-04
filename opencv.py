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

import cv2
import numpy as np 

picture = cv2.imread("resim6.jpg")
#kesit = picture[1000:2500,1000:2500]
aynalanan_resim = cv2.copyMakeBorder(picture,100,100,100,100,cv2.BORDER_REFLECT)

cv2.imshow("kahve ve kek",aynalanan_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
print(aynalanan_resim.shape)