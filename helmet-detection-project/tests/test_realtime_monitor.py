from src.pipelines.realtime_monitor import RealtimeMonitor

def test_realtime_monitor():
    monitor = RealtimeMonitor()
    
    # Teste se o monitor está inicializando corretamente
    assert monitor is not None, "O monitor não foi inicializado corretamente."
    
    # Teste se a detecção de pessoas está funcionando
    people_detected = monitor.detect_people()
    assert isinstance(people_detected, list), "A detecção de pessoas deve retornar uma lista."
    
    # Teste se a verificação de capacete está funcionando
    for person in people_detected:
        has_helmet = monitor.check_helmet(person)
        assert isinstance(has_helmet, bool), "A verificação de capacete deve retornar um valor booleano."
    
    # Teste se a mensagem é exibida corretamente
    for person in people_detected:
        if not monitor.check_helmet(person):
            message = monitor.display_message(person)
            assert message == "Atenção: Pessoa sem capacete!", "A mensagem exibida está incorreta."