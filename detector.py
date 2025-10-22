from ultralytics import YOLO
import cv2

# Carrega o modelo padrão (pode ser yolov8n.pt, yolov8s.pt, etc.)
model = YOLO("yolov8n.pt")

# Inicia a captura da câmera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Faz a predição
    results = model(frame)

    # Variável para verificar se há capacete
    person_detected = False
    helmet_detected = False

    # Percorre os objetos detectados
    for r in results[0].boxes:
        cls = int(r.cls[0])  # classe do objeto
        label = model.names[cls]
        conf = float(r.conf[0])

        if conf > 0.5:  # só considera detecções com mais de 50% de confiança
            x1, y1, x2, y2 = map(int, r.xyxy[0])
            color = (0, 255, 0)

            if label == "person":
                person_detected = True
                color = (0, 255, 255)
                helmet_detected = True
                color = (0, 255, 0)

            # desenha a caixa no frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Se detectou pessoa mas não detectou capacete → alerta
    if person_detected and not helmet_detected:
        cv2.putText(frame, "⚠ Pessoa sem capacete detectada!", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # Mostra o vídeo
    cv2.imshow("Detecção de EPI", frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
