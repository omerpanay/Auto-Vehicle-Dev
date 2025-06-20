import cv2
from ultralytics import YOLO
import numpy as np
from utils.decisions import make_decision
from utils.drawing import draw_results

# 🔌 MODEL YÜKLEME
model_sign = YOLO('traffic_sign.pt')                # Trafik işaretleri
model_light = YOLO('traffic_light.pt')              # Trafik ışıkları
model_seg_road = YOLO('road_segmentation.pt')       # Yol segmentasyonu
model_seg_lane = YOLO('lane_segmentation.pt')       # Şerit segmentasyonu
model_person_car = YOLO('person_and_car_detection.pt') # Yaya ve araç tespiti

# 📹 Video dosyasını aç
cap = cv2.VideoCapture('test.mp4')

# 🔁 Ana Döngü
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 🔍 Trafik işaretleri tespiti
    result_sign = model_sign(frame)[0]
    # 🔍 Trafik ışığı tespiti
    result_light = model_light(frame)[0]
    # 🛣 Yol segmentasyonu
    result_road = model_seg_road(frame)[0]
    # ➖ Şerit segmentasyonu
    result_lane = model_seg_lane(frame)[0]
    # 🚶‍♂️ Yaya ve araç tespiti
    result_person_car = model_person_car(frame)[0]

    # Karar ver
    decision = make_decision(result_sign, result_light, result_road, result_lane, result_person_car)

    # Sonuçları çiz
    output_frame = draw_results(
        frame, result_sign, result_light, result_road, result_lane, result_person_car, decision
    )

    cv2.imshow('Otonom Algılama Sistemi', output_frame)
    if cv2.waitKey(1) == 27:  # ESC ile çık
        break

cap.release()
cv2.destroyAllWindows() 