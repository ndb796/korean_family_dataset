import os
import pandas as pd
import shutil


# 최종 전처리 결과가 담길 폴더 생성
result_folder = "./custom_dataset"
if not os.path.exists(result_folder):
    os.makedirs(result_folder)
# 이미지 폴더 생성
if not os.path.exists(os.path.join(result_folder, "images")):
    os.makedirs(os.path.join(result_folder, "images"))
# 레이블 정보가 담길 데이터프레임(dataframe)
df = pd.DataFrame({
    'family_id': [],
    'person_id': [],
    'age_class': [],
    'image_path': []
})

directories = [
    './family_dataset/1.Training/original',
    './family_dataset/2.Validation/original'
]

for directory in directories:
    for current in os.listdir(directory):
        path = os.path.join(directory, current)
        if path[-4:] != '.zip': # 압축 파일(.zip)이 아닌 경우
            # 친가(A), 외가(B) 폴더
            folder_a, folder_b = os.listdir(path)
            # 친가(A) 폴더에 존재하는 파일 수
            length_a = len(os.listdir(os.path.join(path, folder_a, "3.Age")))
            # 외가(B) 폴더에 존재하는 파일 수
            length_b = len(os.listdir(os.path.join(path, folder_b, "3.Age")))
            target = folder_a # 친가(A) 폴더인 경우
            if length_b > 0: # 외가(B) 폴더인 경우
                target = folder_b
            full_path = os.path.join(path, target, "3.Age")
            for file in os.listdir(full_path):
                # 모든 파일은 .jpg 혹은 .JPG 파일
                if file[-4:] != ".jpg" and file[-4:] != ".JPG":
                    print(f"[Error] It's not a '.jpg' file: [{file}]")
                    continue
                family_id, _, person_id, _, age_class = file.split('_')
                age_class = age_class.split('.')[0][0]
                # family_id = "F0101", person_id = "M", age_class = "f"
                print(family_id, person_id, age_class, file)
                df.loc[len(df.index)] = [family_id, person_id, age_class, file]
                shutil.copyfile(os.path.join(full_path, file),
                                os.path.join(result_folder, "images", file))

df.to_csv(os.path.join(result_folder, "custom_dataset.csv"))
