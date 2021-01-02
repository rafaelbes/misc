import cv2, sys, numpy as np
import sys, os, time
import pytesseract as ocr

for i in range(2):
	time.sleep(2)
	os.system("import -window 67108870 teste2.png")

	original = cv2.imread('teste.png')
	k = 2
	img = cv2.resize(original, None, fx=k, fy=k)
	gr = img[k*324:k*688,k*476:k*536]
	h, w = gr.shape[0], gr.shape[1]

	t = ocr.image_to_string(gr, lang='eng', config='digits')

#cv2.imshow('window1', gr)
#cv2.imwrite('t.png', gr)
#cv2.waitKey(0)
