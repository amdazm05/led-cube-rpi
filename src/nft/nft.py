from time import sleep
import cv2




class NFT:
   
    def __init__(self):
        print("NFT Initialiser")
    
    def display(self,path1,path2):
        img_2 = cv2.imread(path1)
        img_1 = cv2.imread(path2)
        cv2.namedWindow("graycsale image", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("graycsale image",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow('graycsale image',img_2)
        cv2.namedWindow("graycsale image_2", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("graycsale image_2",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow('graycsale image_2',img_1)
        cv2.moveWindow('graycsale image', 480,0)
        cv2.waitKey(0)  #Add an event here to flip images
        cv2.destroyAllWindows()
        cv2.namedWindow("graycsale image", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("graycsale image",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow('graycsale image',img_1)
        cv2.namedWindow("graycsale image_2", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("graycsale image_2",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow('graycsale image_2',img_2)
        cv2.moveWindow('graycsale image', 480,0)
        cv2.waitKey(0)   #Add an event here to flip images
        cv2.destroyAllWindows()  

