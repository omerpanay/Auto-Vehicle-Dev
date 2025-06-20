def make_decision(result_sign, result_light, result_road, result_lane, result_person_car):
    # Basit örnek karar mekanizması
    # Trafik ışığı kırmızıysa dur, değilse devam et
    decision = 'GO'
    if result_light.boxes is not None and len(result_light.boxes) > 0:
        for box in result_light.boxes:
            cls = int(box.cls[0])
            label = result_light.names[cls]
            if label.lower() == 'red':
                decision = 'STOP'
                break
    # Trafik işareti STOP ise dur
    if result_sign.boxes is not None and len(result_sign.boxes) > 0:
        for box in result_sign.boxes:
            cls = int(box.cls[0])
            label = result_sign.names[cls]
            if label.lower() == 'stop':
                decision = 'STOP'
                break
    # Yaya tespit edilirse yavaşla
    if result_person_car.boxes is not None and len(result_person_car.boxes) > 0:
        for box in result_person_car.boxes:
            cls = int(box.cls[0])
            label = result_person_car.names[cls]
            if label.lower() == 'person':
                decision = 'SLOW DOWN'
                break
    return decision 