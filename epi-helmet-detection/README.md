# EPI Helmet Detection Project - AgroCalvoTech

Este projeto tem como objetivo detectar a presença de pessoas e verificar se estão usando capacetes de segurança (EPI) através de uma câmera em tempo real.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
epi-helmet-detection
├── pyproject.toml          # Configuração do projeto Python
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação do projeto
├── .env.example            # Exemplo de configuração de variáveis de ambiente
├── src                     # Código-fonte do projeto
│   ├── main.py             # Ponto de entrada da aplicação
│   ├── __init__.py         # Torna o diretório src um pacote Python
│   ├── detectors           # Módulo de detecção
│   │   ├── __init__.py     # Torna o diretório detectors um pacote Python
│   │   ├── helmet_detector.py # Lógica para detectar capacetes
│   │   └── person_detector.py  # Lógica para detectar pessoas
│   ├── pipelines           # Módulo de pipelines
│   │   ├── __init__.py     # Torna o diretório pipelines um pacote Python
│   │   └── realtime_monitor.py # Gerencia a captura de vídeo em tempo real
│   ├── utils               # Módulo de utilitários
│   │   ├── __init__.py     # Torna o diretório utils um pacote Python
│   │   ├── camera.py       # Funções para manipular a câmera
│   │   ├── drawing.py      # Funções para desenhar anotações nas imagens
│   │   └── logging.py      # Funções para registrar logs
│   └── config              # Módulo de configuração
│       ├── __init__.py     # Torna o diretório config um pacote Python
│       └── settings.py     # Configurações do projeto
├── models                  # Modelos de aprendizado de máquina
│   └── README.md           # Informações sobre os modelos utilizados
├── data                    # Dados utilizados no projeto
│   ├── raw                 # Dados brutos
│   └── processed           # Dados processados
├── scripts                 # Scripts auxiliares
│   └── download_models.py   # Script para baixar modelos
└── tests                   # Testes do projeto
    ├── __init__.py         # Torna o diretório tests um pacote Python
    └── test_detectors.py   # Testes unitários para os detectores
```

## Como Rodar o Sistema

Siga os passos abaixo para executar o sistema:

1. Clone o repositório do projeto.
2. Navegue até o diretório do projeto.
3. Crie um ambiente virtual (opcional, mas recomendado):
   - `python -m venv venv`
   - `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows)
4. Instale as dependências:
   - `pip install -r requirements.txt`
5. Configure as variáveis de ambiente copiando `.env.example` para `.env` e ajustando conforme necessário.
6. Execute o programa:
   - `python src/main.py`

**Certifique-se de que a câmera esteja conectada e funcionando corretamente antes de iniciar o sistema.**