class HelmetDetector:
    def __init__(self, person_detector, helmet_model):
        self.person_detector = person_detector
        self.helmet_model = helmet_model

    def detect(self, frame):
        # Detectar pessoas na imagem
        people = self.person_detector.detect(frame)

        results = []
        for person in people:
            # Para cada pessoa detectada, verificar se está usando capacete
            helmet_detected = self.helmet_model.predict(person['image'])
            results.append({
                'person': person,
                'helmet_detected': helmet_detected
            })

        return results

    def draw_results(self, frame, results):
        for result in results:
            person = result['person']
            helmet_status = "Wearing Helmet" if result['helmet_detected'] else "Not Wearing Helmet"
            # Desenhar a caixa delimitadora e o status na imagem
            # (Implementar a lógica de desenho usando funções de utilidade)
            # Exemplo: draw_box(frame, person['bbox'], helmet_status)

        return frame