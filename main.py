import cv2
import numpy as np

left_img = cv2.imread('img/left.png')
right_img = cv2.imread('img/right.png')

added_img = cv2.addWeighted(left_img, 0.9, right_img, 0.9, -6)
cv2.imwrite('result/added.png', added_img)

zero = np.zeros(left_img.shape[:2], dtype=np.uint8)
red_left_img = cv2.merge((zero, zero, cv2.split(left_img)[2]))
blue_right_img = cv2.merge((cv2.split(right_img)[0], zero, zero))
color_added_img = cv2.addWeighted(red_left_img, 0.9, blue_right_img, 0.9, -6)
cv2.imwrite('result/color_added.png', color_added_img)
