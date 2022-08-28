### 가족 관계 데이터 세트(Korean Family Dataset)

> AI Hub "가족 관계가 알려진 얼굴 이미지" 데이터 세트의 전처리 및 가공 코드 모음

### 원본 데이터 세트 살펴 보기

* [가족 관계가 알려진 얼굴 이미지 데이터 세트 링크](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=528)

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

<pre>
/A(친가)
  /1.Family
  /2.Individuals
  /3.Age
/B(외가)
  /1.Family
  /2.Individuals
  /3.Age

* "3.Age" 폴더에 존재하는 이미지는 {가족 번호}_AGE_{지위}_{나이}_{나이 클래스} 형식을 따른다.
  * 지위: "GF", "GM", "F", "M", "S", "D", "S2", "S3", "S4", "D2", "D3" "D4"
    * GF: 할아버지, GM: 할머니, F: 아버지, M: 어머니, S: 아들, D: 딸
  * 나이: 0~80
  * 나이 클래스: "a1", "a2", "a3", ...
    * 0~6세(a), 7~12세(b), 13~19세(c), 20~30세(d), 31~45세(e), 46~55세(f), 56~66세(g), 67~80세(h)

</pre>
