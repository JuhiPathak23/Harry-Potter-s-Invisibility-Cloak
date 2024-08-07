import cv2
import numpy as np
print(cv2.__version__)
capture_video = cv2.VideoCapture(0)
count = 0
background = 0
for i in range(60):
    return_val, background = capture_video.read()
    if return_val == False:
        continue

background = np.flip(background, axis=1)  
cv2.namedWindow("INVISIBILITY CLOAK", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("INVISIBILITY CLOAK", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while capture_video.isOpened():
    return_val, img = capture_video.read()
    if not return_val:
        break

    count = count + 1
    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_neon_green = np.array([25, 50, 50]) 
    upper_neon_green = np.array([40, 255, 255])
    mask_green = cv2.inRange(hsv, lower_neon_green, upper_neon_green)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask_green = cv2.dilate(mask_green, np.ones((3, 3), np.uint8), iterations=1)
    mask_not_green = cv2.bitwise_not(mask_green)
    res1_green = cv2.bitwise_and(background, background, mask=mask_green)
    res2_green = cv2.bitwise_and(img, img, mask=mask_not_green)
    final_output_green = cv2.addWeighted(res1_green, 1, res2_green, 1, 0)

    cv2.imshow("INVISIBILITY CLOAK", final_output_green)
    k = cv2.waitKey(10)
    if k == 27:
        break

capture_video.release()
cv2.destroyAllWindows()
