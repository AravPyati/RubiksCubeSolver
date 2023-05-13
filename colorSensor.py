import numpy as np
import cv2
import kociemba

cap = cv2.VideoCapture(0)

cubecolor = (0,0,0)
thickness = 2


while True:
   _, frame = cap.read()
   hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   cv2.line(frame, (200,125), (200,375), cubecolor, thickness)
   cv2.line(frame, (200,125), (450,125), cubecolor, thickness)
   cv2.line(frame, (200,375), (450,375), cubecolor, thickness)
   cv2.line(frame, (200,125), (200,375), cubecolor, thickness)
   cv2.line(frame, (450,125), (450,375), cubecolor, thickness)
   
   cv2.line(frame, (283,125), (283,375), cubecolor, thickness)
   cv2.line(frame, (367,125), (367,375), cubecolor, thickness)
   cv2.line(frame, (200,208), (450,208), cubecolor, thickness)
   cv2.line(frame, (200,292), (450,292), cubecolor, thickness)


   img1 = frame[125:208, 200:283]
   
   cv2.imshow("cube1", img1) 

   img2 = frame[208:292, 283:367]
   
   cv2.imshow("cube2", img2)
   img3 = frame[292:375, 367:450]
   
   cv2.imshow("cube3", img3)
   
   
   img4 = frame[125:208, 283:367]
   
   cv2.imshow("cube4", img4)

   img5 = frame[125:208, 367:450]
   
   cv2.imshow("cube5", img5)

   img6 = frame[208:292, 367:450]
   
   cv2.imshow("cube6", img6)

   
    



    #White

   low_white = np.array([0,0,168])
   high_white = np.array([172,111,255])
   maskWhite = cv2.inRange(hsv_frame, low_white, high_white)

    #Green
    
   low_green = np.array([20,100,100])
   high_green = np.array([80,255,255])
   maskGreen = cv2.inRange(hsv_frame, low_green, high_green)

    #Blue

   low_blue = np.array([94,80,2])
   high_blue = np.array([126,255,255])
   maskBlue = cv2.inRange(hsv_frame, low_blue, high_blue)

    #Orange

   low_orange = np.array([0,164,0])
   high_orange = np.array([25,255,255])
   maskOrange = cv2.inRange(hsv_frame, low_orange, high_orange)

    #Red

   low_red = np.array([161,155,84])
   high_red = np.array([179,255,255])
   
    #Yellow

   low_yellow = np.array([22,93,0])
   high_yellow = np.array([45,255,255])
   maskYellow = cv2.inRange(hsv_frame, low_yellow, high_yellow)
   #resultYellow = cv2.bitwise_and(yellow,yellow)


   pixelX = 0
   pixelY = 0

   maskedRed = cv2.inRange([pixelX,pixelY], low_red, high_red)
   maskedWhite = cv2.inRange([pixelX,pixelY], low_white, high_white)
   maskedOrange = cv2.inRange([pixelX,pixelY], low_orange, high_orange)
   maskedGreen = cv2.inRange([pixelX,pixelY], low_green, high_green)
   maskedBlue = cv2.inRange([pixelX,pixelY], low_blue, high_blue)
   maskedYellow = cv2.inRange([pixelX,pixelY], low_yellow, high_yellow)


   whitecount = 0
   yellowcount = 0
   bluecount = 0
   greencount = 0
   redcount = 0
   orangecount = 0
   

   for x in range(200,450):
        for y in range(125,375):
            pixelX = x
            pixelY = y

            if(maskedOrange):
                orange+=1
            if(maskedGreen):
                green+=1
            if(maskedBlue):
                blue+=1
            if(maskedYellow):
                yellow+=1
            if(maskedWhite):
                white+=1
            if(maskedRed):
                red+=1

   colors = {'green':green, 'blue':blue, 'white':white,'yellow':yellow,'orange':orange,'red':red}
   highest = max(colors, key=players.get)
   print(highest)

   #cv2.imshow("red mask", maskRed)
   #cv2.imshow("white mask", maskWhite)
   #cv2.imshow("orange mask", maskOrange)
   #cv2.imshow("blue mask", maskBlue)
   #cv2.imshow("green mask", maskGreen)
   #cv2.imshow("yellow mask", maskYellow)

    


   #print(ping)
  # imgBlur = cv2.GaussianBlur(frame, (7,7), 1 )
   #imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

   #imgStack = stackImages(0.8,[cap,imgBlur,imgGray])
   cv2.imshow("Frame", frame)
   key = cv2.waitKey(1)
   #print(ping)
   if key == 27:
        break
        print(ping)


result = kociemba.solve('FBRUURRFDLFDDRDLRRFLFLFFBBFLLUDDBUDBRRUFLUBRDBUDLBUUBL')
print(result)
#print("************************************************************************")
#print("************************************************************************")
#print("********************************WHITE****************************************")
#imgU = cv2.imread(r"C:\Users\17324\Desktop\color_recognition\white.jpg", 0)
#print(imgU)
#print("*********************************RED***************************************")
#imgR = cv2.imread(r"C:\Users\17324\Desktop\color_recognition\red.jpg", 0)
#print(imgR)
#print("********************************ORANGE*************************************")
#imgL = cv2.imread(r"C:\Users\17324\Desktop\color_recognition\orange.jpg", 0)
#print(imgL)
#print("********************************YELLOW****************************************")
#imgD = cv2.imread(r"C:\Users\17324\Desktop\color_recognition\yellow.jpg", 0)
#print(imgD)
#print("********************************GREEN**************************************")
#imgF = cv2.imread(r"C:\Users\17324\Desktop\color_recognition\green.jpg", 0)
#print(imgF)
#print("*********************************BLUE****************************************")
#imgB = cv2.imread(r"C:\Users\17324\Desktop\color_recognition\blue.jpg", 0)
#print(imgB) 
#print("******************************SCRAMBLED***************************************")
#imgS = cv2.imread(r"C:\Users\17324\Desktop\color_recognition\scrambled2.jpg", 0)
#print(imgS)
#print("************************************************************************")

