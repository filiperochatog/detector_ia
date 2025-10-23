# Helmet Detection Project

Este projeto tem como objetivo detectar pessoas a partir da câmera do notebook e verificar se elas estão usando capacete. O sistema utiliza técnicas de visão computacional para realizar a detecção em tempo real.

## Estrutura do Projeto

```
helmet-detection-project
├── src
│   ├── __init__.py
│   ├── app.py
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── detectors
│   │   ├── __init__.py
│   │   ├── helmet_classifier.py
│   │   └── person_detector.py
│   ├── pipelines
│   │   ├── __init__.py
│   │   └── realtime_monitor.py
│   └── utils
│       ├── __init__.py
│       └── video_stream.py
├── configs
│   └── default.yaml
├── models
│   └── README.md
├── scripts
│   └── download_models.py
├── tests
│   ├── __init__.py
│   └── test_realtime_monitor.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── docs
    └── USAGE.md
```

## Instruções para Rodar o Sistema

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Instale as dependências do projeto executando o comando:
   ```
   pip install -r requirements.txt
   ```
3. Baixe os modelos necessários executando o script:
   ```
   python scripts/download_models.py
   ```
4. Execute a aplicação com o seguinte comando:
   ```
   python src/app.py
   ```
5. A câmera do notebook será aberta e o sistema começará a monitorar se as pessoas estão usando capacete. Se alguém não estiver usando, uma mensagem será exibida.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.