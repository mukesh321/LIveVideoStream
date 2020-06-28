from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
import requests
import cv2
import numpy as np
import time
# Create your views here.

def index(request):
	return render(request,'chartapp/index.html')
def webcam(request):

	video=cv2.VideoCapture(0)

	while True:
		check, frame =video.read()

		gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	

		cv2.imshow("capturing", gray)

		key=cv2.waitKey(1)

		if key==27:
			break
	video.release()

	cv2.destoryAllWindows()

def mobilecam(request):
	url="http://192.168.0.31:8080/shot.jpg"

	while True:
		img_response=requests.get(url)
		img_arr=np.array(bytearray(img_response.content), dtype=np.uint8)
		img = cv2.imdecode(img_arr, -1)

		cv2.imshow("mobilecam", img)	

		if cv2.waitKey(1)==27:
			break
	cv2.destoryAllWindows()