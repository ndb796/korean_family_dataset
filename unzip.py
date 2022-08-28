import os
import zipfile


directories = [
    './family_dataset/1.Training/labeled',
    './family_dataset/1.Training/original',
    './family_dataset/2.Validation/labeled',
    './family_dataset/2.Validation/original'
]
for directory in directories:
    for current in os.listdir(directory):
        # 전체 경로(.zip까지)
        path = os.path.join(directory, current)
        if path[-4:] == '.zip': # 압축 파일(.zip)인 경우
            compressed = zipfile.ZipFile(path)
            # 동일 폴더에 압축 해제
            compressed.extractall(path[:-4])
            compressed.close()
