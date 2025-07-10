# 🤖 디지털 트윈 기반 서비스 로봇 시스템 구성

> ROS2 기반 자율주행 라인트레이싱과 ArUco 마커 인식을 통해 로봇팔의 픽 앤 플레이스(Pick & Place) 작업을 수행하는 서비스 로봇 시스템입니다.  
> 
> **DetectLane.py**에 중점을 두고, **aruco_detect.py**를 통해 Manipulation을 작동시키는 구조로 구성하였습니다.  
> 
> 시나리오보다는 **주요 코드 분석 및 최적화**에 중점을 두고 개발한 프로젝트입니다.

---

### 📄 더 자세한 내용은 아래의 PDF 또는 발표 자료에서 확인하실 수 있습니다.

---

## 🎥 시연 영상  
[![Demo Video](https://img.youtube.com/vi/JMnDxCcO9bU/0.jpg)](https://youtube.com/shorts/JMnDxCcO9bU?feature=share)

---

## 1. 📊 개발 과정


### 📅 작업 일정

| 날짜 | 작업 내용 |
|------|-----------|
| 2025.06.16 | 기획안 작성 및 주제 선정 |
| 2025.06.17 | 로봇팔 초기 포즈 설정, 카메라 캘리브레이션, 차선 인식 1차 |
| 2025.06.18 | 차선 인식 2차 개선(빛 반사, 라인트래킹, 예외처리), ArUco 마커 인식 구현 |
| 2025.06.19 | 차선 인식 3차(오류 수정), Pick & Place 시나리오 완성, 발표자료 제작 |

> 총 개발 기간: **4일**

---

## 2. ⚙️ 주요 기능

- HSV + 밝기 기반 차선 마스킹 및 보정 → 자율주행 구현 (DetectLane.py)
- PD 제어 기반의 부드러운 Steering 및 직진 속도 조절 (ControlLane.py)
- ArUco 마커 기반 위치 추정 및 TF 변환을 통한 좌표 추출(aruco_detector.py)
- 로봇팔 Pick & Place 동작 시나리오 구현 (Pick_n_place.py)

---

## 3. 💡 도전 과제 & 해결

| 문제 | 해결 방법 |
|------|-----------|
| 카메라 위치 및 포지셔닝 오류 | Calibration 값 수정 및 image_raw 사용 |
| 바닥 반사로 인해 잘못된 차선 인식 | equalizeHist 기반 밝기 보정 + HSV 범위 자동 설정 |
| 차선이 불안정하거나 탐지 실패 | Morphology 연산 + Sliding Window 탐지 보완 |
| ArUco 위치 인식 정확도 부족 | Calibration.yaml 기반 외부 파라미터 조정 및 오차 보정 |

---

## 4. 👥 팀원 역할 분담

| 이름 | 담당 역할 |
|------|-----------|
| 정민섭 | 팀장, 차선 인식 및 PD 제어 알고리즘 |
| 문준웅 | 코드 통합, 전체 주행 로직 및 통신 구조 |
| 이경민 | 하드웨어 세팅, ArUco 인식 로직, 발표자료 제작 |
| 최정호 | 카메라 캘리브레이션, Manipulator 제어 로직 구성 |

---

## 5. 🎯 성과 및 결과물

- HSV 마스킹 → 밝기 보정 → Morphology 연산 기반 차선 검출 정확도 향상
- 안정적인 자율주행 구현 및 조향/속도 제어 최적화
- ArUco 마커 기반 물체 위치 인식 및 조작 성공
- ROS2 기반 서비스 구조 구성 및 노드 통신 완성

---

## 6. 📸 프로젝트 주요 장면

### 1) 카메라 캘리브레이션  
![캘리브레이션1](https://github.com/user-attachments/assets/6becd47b-97c9-4232-ba3e-52231181b117)  
![캘리브레이션2](https://github.com/user-attachments/assets/bf3f3783-5f5d-4dcf-a7fa-a29712724e83)

### 2) ArUco Marker 인식  
![ArUco1](https://github.com/user-attachments/assets/e0323ad8-20b0-4071-be4a-b4a4f49276ae)  
![ArUco2](https://github.com/user-attachments/assets/3b6d4c11-e446-4fc8-adda-8b32225c55b3)

### 3) Pick & Place 시나리오  
![PickPlace](https://github.com/user-attachments/assets/a908ae5a-6856-4fdf-8776-f9ac8c2921f7)

---

## 7. ✍ 후기 및 개선 사항

- PD 제어의 민감도 조절 및 안정성 확보 필요성 확인
- 밝기 기반 HSV 마스킹 성능 개선 → 실시간성 확보 필요
- ArUco 좌표 인식 오차에 대한 후처리 로직 도입 필요
- Manipulation 트리거를 GUI 또는 서비스 기반으로 구조화 예정

---

## 8. 🎓 개인적인 배움

- ROS2 통신 구조와 노드 간 인터페이스 설계 이해
- Vision 기반 주행 및 영상 전처리 알고리즘 실습
- HSV 마스킹, Equalize, Morphology 등 영상 처리 로직 직접 구현
- ArUco 마커 인식과 로봇팔 연동을 통한 조작 시나리오 설계 경험

---

## 9. 🚀 향후 개선 및 확장 아이디어

- ROS2 서비스 기반 Manipulator 동작 모듈화
- ArUco 인식 신뢰도 및 필터링 고도화
- 실제 거리 기반 좌표 정밀도 보정 로직 추가
- GUI 및 CLI 기반 조작 인터페이스 연동
- LiDAR 기반 장애물 감지 기능 확장

---

> 본 프로젝트는 ROS2 기반으로 자율주행과 물체 인식, 로봇팔 조작 등 다양한 기능을 통합하며, 실시간 영상처리와 센서 통신 기술을 융합한 서비스 로봇 시스템 구현에 중점을 두었습니다.
