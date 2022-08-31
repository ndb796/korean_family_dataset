import pandas as pd
import random
import os
from shutil import copyfile


"""
> [Function] Parse the metadata.
* family_list = ["F0001", "F0002", ...]
* family_to_person_map["F0001"] = ["D", "GM", "M"]
* person_to_image_map["F0001_D"] = [
    "F0001_AGE_D_18_a1.jpg",
    "F0001_AGE_D_18_a2.jpg",
    ...
]
"""
def parsing(metadata):
    family_set = set()
    family_to_person_map = dict()
    person_to_image_map = dict()
    # iterate all rows in the metadata file
    for idx, row in metadata.iterrows():
        family_id = row["family_id"]
        person_id = row["person_id"]
        key = family_id + "_" + person_id
        image_path = row["image_path"]
        if family_id not in family_set:
            family_set.add(family_id)
            family_to_person_map[family_id] = []
        if person_id not in family_to_person_map[family_id]:
            family_to_person_map[family_id].append(str(person_id))    
            person_to_image_map[key] = []
        person_to_image_map[key].append(image_path) # save all image paths
    family_list = list(family_set)
    return family_list, family_to_person_map, person_to_image_map


metadata_path = "./custom_korean_family_dataset_resolution_256/custom_val_dataset.csv"
metadata = pd.read_csv(metadata_path)
image_directory = "./custom_korean_family_dataset_resolution_256/val_images"
family_list, family_to_person_map, person_to_image_map = parsing(metadata)

# 최종 데이터 세트가 담길 폴더 생성
positive_folder = "./fixed_val_dataset/positive"
if not os.path.exists(positive_folder):
    os.makedirs(positive_folder)
negative_folder = "./fixed_val_dataset/negative"
if not os.path.exists(negative_folder):
    os.makedirs(negative_folder)

"""
* 최종적으로 다음과 같은 형태로 저장된다.
/fixed_val_dataset
  /positive
    /0
    /1
    ...
  /negative
    /0
    /1
    ...
"""

total_pairs = 10000
for idx in range(total_pairs):
    # positive samples (family)
    if idx % 2 == 0:
        # select a single family
        family_id = random.choice(family_list)
        # select 2 different people in a single family
        p1, p2 = random.sample(family_to_person_map[family_id], 2) 
        key1 = family_id + "_" + p1
        key2 = family_id + "_" + p2
        result_folder = positive_folder
    # negative samples (not family)
    else:
        # select 2 different family
        f1, f2 = random.sample(family_list, 2)
        # select a person in each family
        p1 = random.choice(family_to_person_map[f1])
        p2 = random.choice(family_to_person_map[f2])
        key1 = f1 + "_" + p1
        key2 = f2 + "_" + p2
        result_folder = negative_folder

    path1 = random.choice(person_to_image_map[key1])
    path2 = random.choice(person_to_image_map[key2])

    if not os.path.exists(os.path.join(result_folder, str(idx // 2))):
        os.makedirs(os.path.join(result_folder, str(idx // 2)))
    copyfile(
        os.path.join(image_directory, path1),
        os.path.join(result_folder, str(idx // 2), path1)
    )
    copyfile(
        os.path.join(image_directory, path2),
        os.path.join(result_folder, str(idx // 2), path2)
    )
