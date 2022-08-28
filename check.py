import os
import zipfile


directories = [
    './family_dataset/1.Training/original',
    './family_dataset/2.Validation/original'
]

check = True # 친가(A) 혹은 외가(B) 한쪽에만 이미지가 있는지 여부
for directory in directories:
    for current in os.listdir(directory):
        path = os.path.join(directory, current)
        # path = "./family_dataset/1.Training/original\TS0284"
        if path[-4:] != '.zip': # 압축 파일(.zip)이 아닌 경우(폴더인 경우)
            # 친가(A), 외가(B) 폴더명
            folder_a, folder_b = os.listdir(path)
            # 친가(A) 폴더에 존재하는 파일 수 (예시: 25)
            length_a = len(os.listdir(os.path.join(path, folder_a, "3.Age")))
            # 외가(B) 폴더에 존재하는 파일 수 (예시: 0)
            length_b = len(os.listdir(os.path.join(path, folder_b, "3.Age")))
            if length_a > 0 and length_b > 0:
                check = False

if check: print("Dataset loaded.")
else: print("Conflict!")
