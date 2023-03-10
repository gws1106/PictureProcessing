import cv2

#영상 소스 열기
src1 = cv2.imread('c:/images/picture99.jpg')

#영상처리 알고리즘
dst1 = cv2.cvtColor(src1, cv2.COLOR_RGB2GRAY)





#영상 디스플레이
cv2.imshow('src1', src1)
cv2.imshow('dst1', dst1)


#영상종료 및 마무리
cv2.waitkey(0)             #아무키 누르면 종료
cv2.destroyAllWindows()    #메모리 해제
