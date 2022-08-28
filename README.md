### 가족 관계 데이터 세트(Korean Family Dataset)

> AI Hub "가족 관계가 알려진 얼굴 이미지" 데이터 세트의 전처리 및 가공 코드 모음

### 원본 데이터 세트 살펴 보기

* [가족 관계가 알려진 얼굴 이미지 데이터 세트 링크](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=528)
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
