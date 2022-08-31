import os
import cv2

# 이미지 크기 수정 결과가 담길 폴더 생성
result_folder = "./resized_images_resolution_256"
if not os.path.exists(result_folder):
    os.makedirs(result_folder)

directory = "./images"
for file in os.listdir(directory): # 이미지 파일을 하나씩 확인하며
    # 이미지를 읽어서 크기를 256 X 256으로 변환하기
    path = os.path.join(directory, file)
    img = cv2.imread(path)
    resized_img = cv2.resize(img, (256, 256))
    # 이미지 저장하기
    saved_path = os.path.join(result_folder, file)
    cv2.imwrite(saved_path, resized_img)
