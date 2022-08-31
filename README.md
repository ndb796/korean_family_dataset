### 가족 관계 데이터 세트(Korean Family Dataset)

> AI Hub "가족 관계가 알려진 얼굴 이미지" 데이터 세트의 전처리 및 가공 코드 모음

### 원본 데이터 세트 살펴 보기

* [AI Hub "가족 관계가 알려진 얼굴 이미지 데이터 세트"](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=528)
* [데이터 세트 내에 존재하는 모든 압축 파일을 해제하는 코드](/unzip.py)

<pre>
/family_dataset
  /1.Training
    /labeled
      TL0001.zip
      TL0002.zip
      ...
      TL0299.zip
    /original
      TS0001.zip
      TS0002.zip
      ...
      TS0299.zip
  /2.Validation
    /labeled
      VL0801.zip
      VL0802.zip
      ...
      VL0900.zip
    /original
      VS0801.zip
      VS0802.zip
      ...
      VS0900.zip
</pre>

* 이때 각 original 폴더에 포함된 압축 파일은 다음과 같이 구성된다.
* 각 폴더는 A(친가) 혹은 B(외가) 폴더만 존재한다.
  * [검증 코드](/check.py)

<pre>
# 예시 폴더 구성
/VS0801
  /A(친가)
    /1.Family
    /2.Individuals
    /3.Age
  /B(외가)
    /1.Family
    /2.Individuals
    /3.Age
</pre>

* "3.Age" 폴더에 존재하는 이미지는 <b>{가족 번호}\_AGE\_{지위}\_{나이}\_{클래스}</b> 형식을 따른다.
  * 지위: "GF", "GM", "F", "M", "S", "D", "S2", "S3", "S4", "D2", "D3", "D4"
    * GF: 할아버지
    * GM: 할머니
    * F: 아버지
    * M: 어머니
    * S: 아들
    * D: 딸
  * 나이: 0~80
    * 단, 이는 데이터 세트 구축 당시의 나이 정보라서 촬영 당시 나이는 "클래스"를 확인해야 한다.
  * 클래스: "a1", "a2", "a3", ...
    * (a): 0-6세
    * (b): 7-12세
    * (c): 13-19세
    * (d): 20-30세
    * (e): 31-45세
    * (f): 46-55세
    * (g): 56-66세
    * (h): 67-80세

### 데이터 전처리

* 모든 "3.Age" 폴더만 확인하여 전체 데이터 세트를 전처리한다.
  * [소스 코드](/preprocess.py)
* 결과로 나오는 images 폴더는 13,068개의 이미지로 구성된다.
<pre>
/images
  F0001_AGE_D_18_a1.jpg
  F0001_AGE_D_18_a2.jpg
  ...
  F0900_AGE_M_57_f1.jpg
  F0900_AGE_M_57_f2.jpg
</pre>
* custom_dataset.csv는 13,068개의 이미지에 대한 메타 정보를 가진다.
  * 속성(attribute) 목록: 'family_id', 'person_id', 'age_class', 'image_path'

### 이미지 크기 줄이기

* 전처리된 이미지 중에는 해상도가 큰 이미지가 많다.
* 모든 이미지를 128 X 128로 바꾼 버전과 256 X 256로 바꾼 버전을 만들 수 있다.
* [소스 코드](/image_resizer.py)

### 고정된 평가 데이터 세트 만들기

* 평가를 위하여 10,000개의 (얼굴 이미지, 얼굴 이미지) 쌍을 만들 수 있다.
  * 5,000 쌍은 가족(positive), 5,000 쌍은 비가족(negative)로 구성할 수 있다.
* [소스 코드](/generate_fixed_evaluation_dataset.py)
<pre>
/fixed_val_dataset
  /positive
    /0
    /1
    ...
    /4999
  /negative
    /0
    /1
    ...
    /4999
</pre>

### 최종적으로 전처리된 데이터 세트들

* [custom_korean_family_dataset_resolution_128.zip](https://postechackr-my.sharepoint.com/:u:/g/personal/dongbinna_postech_ac_kr/EbMhBPnmIb5MutZvGicPKggBWKm5hLs0iwKfGW7_TwQIKg)
* [custom_korean_family_dataset_resolution_256.zip](https://postechackr-my.sharepoint.com/:u:/g/personal/dongbinna_postech_ac_kr/Eb1hztk047VFk2j9bI7JKmEBtkWpABZ8vfX5_m0cdSjQHw)
