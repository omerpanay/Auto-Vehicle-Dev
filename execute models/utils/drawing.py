import cv2
import numpy as np

def draw_results(frame, result_sign, result_light, result_road, result_lane, result_person_car, decision):
    # Trafik işareti kutuları (yeşil)
    if result_sign.boxes is not None:
        for box in result_sign.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = result_sign.names[cls]
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    # Trafik ışığı kutuları (kırmızı)
    if result_light.boxes is not None:
        for box in result_light.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = result_light.names[cls]
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    # Yol segmentasyonu (gri maske)
    if result_road.masks is not None:
        mask = result_road.masks.data[0].cpu().numpy()
        mask = (mask * 255).astype(np.uint8)
        mask = cv2.resize(mask, (frame.shape[1], frame.shape[0]))
        frame[mask > 128] = cv2.addWeighted(frame, 0.5, np.zeros_like(frame), 0.5, 0)[mask > 128]
    # Şerit segmentasyonu (sarı maske)
    if result_lane.masks is not None:
        mask = result_lane.masks.data[0].cpu().numpy()
        mask = (mask * 255).astype(np.uint8)
        mask = cv2.resize(mask, (frame.shape[1], frame.shape[0]))
        frame[mask > 128] = cv2.addWeighted(frame, 0.5, np.full_like(frame, (0, 255, 255)), 0.5, 0)[mask > 128]
    # Yaya ve araç kutuları (mavi)
    if result_person_car.boxes is not None:
        for box in result_person_car.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = result_person_car.names[cls]
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    # Karar bilgisini ekrana yaz
    cv2.putText(frame, f'Decision: {decision}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    return frame 