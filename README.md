# 🤖 ROS2 기반 라인트레이싱 및 ArUco 인식 서비스 로봇 시스템

> ROS2 기반 자율주행(라인트레이싱)과 ArUco 마커 인식을 통해 로봇팔의 Pick & Place 작업을 수행하는 **서비스 로봇 시스템**입니다.  
> 본 프로젝트는 시나리오보다는 **핵심 기능 구현 및 코드 최적화**에 중점을 두었습니다.

---

## 🎥 데모 영상

[![Demo Video](https://img.youtube.com/vi/JMnDxCcO9bU/0.jpg)](https://youtube.com/shorts/JMnDxCcO9bU?feature=share)

---

## 📅 개발 일정

| 날짜 | 작업 내용 |
|------|-----------|
| 2025.06.16 | 주제 선정 및 기획안 작성 |
| 2025.06.17 | 로봇팔 초기 포즈 설정, 카메라 캘리브레이션, 차선 인식 1차 |
| 2025.06.18 | 차선 인식 개선, ArUco 마커 인식 구현 |
| 2025.06.19 | Pick & Place 시나리오 구성, 발표자료 제작 |

> **총 개발 기간**: 4일

---

## ⚙️ 주요 기능

- `detect_lane.py`: HSV + 밝기 기반 차선 마스킹 및 라인트레이싱
- `control_lane.py`: PD 제어 기반 Steering 및 속도 조절
- `aruco_detector.py`: ArUco 마커 기반 좌표 추출 및 TF 변환
- `pick_n_place.py`: 로봇팔 Pick & Place 시나리오 구현

---

## 💡 도전 과제 & 해결

| 문제 | 해결 방법 |
|------|-----------|
| 카메라 포지셔닝 오류 | Calibration.yaml 보정 + `image_raw` 토픽 사용 |
| 바닥 반사로 인한 차선 오인식 | 밝기 보정(`equalizeHist`) + HSV 자동 범위 설정 |
| 차선 인식 불안정 | Morphology 연산 + Sliding Window 보완 |
| ArUco 위치 인식 정확도 | 카메라 캘리브레이션 및 거리 기반 추정 적용 |

---

## 👥 팀원 역할

| 이름 | 담당 |
|------|------|
| 정민섭 | 차선 인식 및 PD 제어 |
| 문준웅 | 전체 주행 로직, 코드 통합 |
| 이경민 | 하드웨어 세팅, ArUco 인식, 발표 자료 |
| 최정호 | 카메라 캘리브레이션, 로봇팔 제어 |

---

## 🎯 프로젝트 성과

- 밝기 보정 + HSV 마스킹 + Morphology 연산을 통한 차선 검출 정확도 향상
- PD 제어 기반 자율주행 구현
- ArUco 마커 기반 위치 인식 및 Pick & Place 동작 성공
- ROS2 기반 다중 노드 통신 구조 설계 및 실행

---

## 📸 주요 장면

### 📍 카메라 캘리브레이션
<img src="https://github.com/user-attachments/assets/6becd47b-97c9-4232-ba3e-52231181b117" width="300"/>
<img src="https://github.com/user-attachments/assets/bf3f3783-5f5d-4dcf-a7fa-a29712724e83" width="300"/>

### 📍 차선 인식 개선 과정
- 밝기 보정 (equalizeHist)
- Morphology 연산
- HSV 마스킹 자동화

| 빛 반사 보정 | Morphology | HSV 마스킹 | 최종 결과 |
|--------------|-------------|--------------|--------------|
| ![](https://github.com/user-attachments/assets/61782e78-f2cd-46a4-8063-a3bf40bf2eb0) | ![](https://github.com/user-attachments/assets/ec91b4d6-87ea-488b-bc7b-905d2645cc85) | ![](https://github.com/user-attachments/assets/72a95b0c-c514-49d5-85a0-09f791f3fe6b) | ![](https://github.com/user-attachments/assets/0d01514d-5cbb-412c-9e0c-894d3a3c083e) |

### 📍 ArUco 마커 인식
<img src="https://github.com/user-attachments/assets/e0323ad8-20b0-4071-be4a-b4a4f49276ae" width="300"/>
<img src="https://github.com/user-attachments/assets/3b6d4c11-e446-4fc8-adda-8b32225c55b3" width="300"/>

### 📍 Pick & Place 동작
<img src="https://github.com/user-attachments/assets/a908ae5a-6856-4fdf-8776-f9ac8c2921f7" width="500"/>

---

## ✍ 개선 사항 및 회고

- PD 제어 민감도 조정 및 주행 안정성 향상 필요
- HSV 마스킹 실시간 처리 성능 개선 과제 도출
- ArUco 인식 후처리 보정 로직 개발 예정
- Manipulation 트리거 구조를 서비스 or GUI 기반으로 확장 예정

---

## 🧠 배운 점

- ROS2의 퍼블리셔/서브스크라이버 구조 이해
- HSV 마스킹, equalizeHist, Morphology 등 영상 처리 실습
- ArUco 마커 인식 및 TF 프레임 변환 로직 적용
- 로봇팔 제어와 인식 알고리즘의 실시간 통합 경험

---

## 🚀 향후 확장 아이디어

- Manipulator 동작을 ROS2 서비스로 모듈화
- ArUco 마커 위치 신뢰도 향상을 위한 필터링 보완
- 거리 기반 좌표 정밀도 보정 알고리즘 추가
- GUI 및 CLI 제어 인터페이스 개발
- LiDAR 기반 장애물 회피 기능 확장

---

> 이 프로젝트는 ROS2 기반 기술을 활용하여 자율주행, 인식, 로봇팔 제어를 통합한 **실시간 서비스 로봇 시스템 구현**을 목표로 하였습니다.
