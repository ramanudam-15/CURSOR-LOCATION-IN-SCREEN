import cv2
def location(event,x,y,flags,param):
    if event==cv2.EVENT_FLAG_LBUTTON:
        print("x", x)
        print("y", y)
image=cv2.imread(r"C:\Users\user\Pictures\Saved Pictures\pp-2.jpg",0)
cv2.imshow("image",image)
cv2.setMouseCallback("image", location)
cv2.waitKey(0)
cv2.destroyAllWindows()    