# opencv

## project1
- 사진(`sample.jpg`) grayscale로 열어서 이미지의 평균 밝기보다 어두운 픽셀들을 0으로 바꿔서 `output.jpg`로 저장
- 주어진 사진 파일(`sample.jpg`)에 대해서 이미지의 평균 밝기를 기준으로 하여 명암비를 조절한 결과를 `constrast.jpg`로 저장
- 웹캠을 사용하여 grayscale로 동영상을 저장하되, 카메라로 들어오는 현재 프레임이 직전 프레임보다 이미지 전체의 평균 밝기가 30 넘게 바뀔 경우,
그 시점부터 다음 3초간 반전시켜서 `output.avi`로 저장

## project2
### 사각형 내의 원의 수 세기
<details>
<summary> 결과</summary>
<div>

|||
|:---:|:---:|
| <img width="200" alt="image" src="https://user-images.githubusercontent.com/65652094/214291316-8dd1ed8d-8203-482a-a94b-9899db9a65ee.png"> | <img width="200" alt="image" src="https://user-images.githubusercontent.com/65652094/214291375-d7ff3732-9810-4203-87a9-a4be7ca8cbf9.png"> |
<img width="200" alt="image" src="https://user-images.githubusercontent.com/65652094/214291402-eeb21a51-0dad-4aa9-9346-c721fca5e45a.png"> | <img width="200" alt="image" src="https://user-images.githubusercontent.com/65652094/214291425-f71f98d3-bc1f-431f-a007-4fcfdf8d4f87.png"> |

<img width="300" alt="image" src="https://user-images.githubusercontent.com/65652094/214291450-f0a43de6-99ac-4c38-81f4-32565e06ea1e.png">
</div>
</details>

- 한 이미지 내의 하나의 사각형이 있고 그 안에 n개의 원이 있을 때, 원의 숫자를 console에 출력하기

### 사각형 내의 원의 수 세기
<details>
<summary> 결과</summary>
<div>

||
|:---:|
| <img width="500" alt="image" src="https://user-images.githubusercontent.com/65652094/214292599-da179d3d-8d18-4e93-b591-aedfbbd76670.png"> |
<img width="300" alt="image" src="https://user-images.githubusercontent.com/65652094/214292637-d1489531-8157-4a3f-99a3-99b7ca5b7e75.png"> |

</div>
</details>

- 한 이미지 내에 여러 개의 사각형이 존재
- 각 사각형 안에 각각 n개의 원이 있을 때, 각 사각형별로 내부에 있는 원의 숫자를 오름차순으로 console에 출력하기

### 주사위 읽기 (1)
<details>
<summary> 결과</summary>
<div>

||
|:---:|
| <img width="300" alt="image" src="https://user-images.githubusercontent.com/65652094/214294657-f222d0a0-c52c-4df5-892f-3be0378b4fc7.png"> |
| <img width="300" alt="image" src="https://user-images.githubusercontent.com/65652094/214294678-09c19b84-1c13-47d5-9ed0-fe4c41926111.png"> |

</div>
</details>

- 책상 위에 놓인 임의의 주사위의 눈을 읽기
- 한 이미지 내에 여러 개의 주사위 존재
- 주사위의 눈을 오름차순으로 console에 출력하기

### 주사위 읽기 (2)
<details>
<summary> 결과</summary>
<div>

||
|:---:|
| <img width="500" alt="image" src="https://user-images.githubusercontent.com/65652094/214295367-8a704652-f24f-4b80-a297-6ce1f8aa6104.png"> |
| <img width="300" alt="image" src="https://user-images.githubusercontent.com/65652094/214295405-0b3309fb-00e7-4b89-b0c2-48faf9dbdd0f.png"> |

</div>
</details>

- 책상 위에 놓인 임의의 주사위의 눈 읽기
- 한 이미지 내에 여러 개의 주사위 존재
- 주사위의 눈을 오름차순으로 console에 출력하기


### 주사위 읽기 (3)
<details>
<summary> 결과</summary>
<div>

||||
|:---:|:---:|:---:|
| <img width="200" alt="image" src="https://user-images.githubusercontent.com/65652094/214295787-26363d1d-77b3-4d3a-9b1a-e8b4513d16c4.png" > | <img width="200" alt="image" src="https://user-images.githubusercontent.com/65652094/214295810-0d13c33e-ffc8-4642-830f-f348464c1377.png" > | <img width="200" alt="image" src="https://user-images.githubusercontent.com/65652094/214295826-fb25f5a6-b7a6-40eb-aa2d-543fee01710d.png" >
| <img width="200" alt="image" src="https://user-images.githubusercontent.com/65652094/214295836-784c1281-f841-4c22-8ee4-0ba1cb114746.png" > | <img width="200" alt="image" src="https://user-images.githubusercontent.com/65652094/214295850-354708f8-d5be-4281-bf54-e7eb93958934.png" > | <img width="200" alt="image" src="https://user-images.githubusercontent.com/65652094/214295862-7eea3bb7-87eb-471a-8c8e-13012a68bccb.png" >
| <img width="200" alt="image" src="https://user-images.githubusercontent.com/65652094/214295908-f9f0c55d-d7bf-4a97-9026-1b27207efbdc.png" > | <img width="200" alt="image" src="https://user-images.githubusercontent.com/65652094/214295922-1c4dd843-e0ff-4fe0-83c7-389cc3868784.png" > | <img width="200" alt="image" src="https://user-images.githubusercontent.com/65652094/214295935-2d1a8760-90f8-4273-84d8-b240430cdf95.png" > |

<img width="300" alt="image" src="https://user-images.githubusercontent.com/65652094/214295962-515ddfdf-a962-4e95-9041-1fa0c9ff7e0f.png" >

</div>
</details>

- 책상 위에 놓인 하나의 주사위의 눈 읽기
- 여러 면이 보이는 주사위에 대해서 가장 넓은 면의 주사위의 눈을 읽어서 console에 출력하기
