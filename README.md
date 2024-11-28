# 산학협력프로젝트 머리스타일 변경
---

프로젝트 수행 내용
CelebAMask-HQ dataset로 학습시킨 BiSeNet을 기반으로 얼굴 구역을 나누고, 이것을 토대로 머리색, 입술색, 눈썹색 변경 작업 진행 및 StyleGAN2를 이용하여 입력값에 머리스타일, 얼굴을 각각 넣으면 자연스럽게 합성해주는 작업을 진행, 마지막으로 이 두 모델이 같이 동작할 수 있도록 진행

---


---
## 프로젝트 결과

사용자로부터 입력받은 인물 이미지를 바탕으로 얼굴,모발 범위를 추출하여  각각 합성하고 사용자의 가능한 색에 맞는 얼굴 이미지를 효과적으로 생성하는 기술을 구현함 

![image](https://github.com/user-attachments/assets/81baa6b8-b736-4215-8f69-b57ec5feb90b)

---
## 프로젝트 기대효과

한정된 스타일 변화뿐만 아니라 사용자가 원하는 폭넓은 스타일 변화를 주어 데이터를 생성할 수 있으므로 개인화된 경험을 개선하는데 탁월함. 또한 AI 기반 개인화된 필터 시스템을 통해 사용자 경험을 혁신함으로써 얼굴 교체 및 복원 작업의 정밀성과 신뢰성을 높이며, 타 분야 응용 가능성 증대, 다양한 산업 분야에 적용 가능한 기술을 상용화하여 고객 맞춤형 서비스 확대, 새로운 시장 창출에 기여할 것으로 기대됨.

---
## 향후 계획

BiSeNet모델을 더욱 발전시켜 얼굴 파싱 성능향상을 지속적으로 추구할 계획임 향후 목표는 이를 통하여 더욱 세세한 조정이 가능하도록 얼굴 이미지 합성 기능에 대한 가능성을 탐구하는 것임. 또한 다양한 환경에서의 이미지에 원활하게 적용 가능한 모델을 구축할 계획임

---
## 실행방법

requirments.txt

img 폴더에 face.png, hair.png를 넣고 main.py를 실행시킨다.



---
---
## References

이 코드는 [Style-Your-Hair](https://github.com/Taeu/Style-Your-Hair.git) [face-makeup](https://github.com/zllrunning/face-makeup.PyTorch.git) [face-parsing](https://github.com/zllrunning/face-parsing.PyTorch.git) 로부터 작성되었습니다.

