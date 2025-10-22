# models/README.md

# EPI Helmet Detection Models

Este diretório contém informações sobre os modelos de aprendizado de máquina utilizados no projeto de detecção de pessoas e verificação do uso de Equipamentos de Proteção Individual (EPI), especificamente capacetes.

## Modelos Utilizados

1. **Modelo de Detecção de Pessoas**
   - Descrição: Este modelo é responsável por identificar a presença de pessoas em imagens ou vídeos.
   - Arquivo: `src/detectors/person_detector.py`

2. **Modelo de Detecção de Capacetes**
   - Descrição: Este modelo verifica se as pessoas detectadas estão usando capacetes.
   - Arquivo: `src/detectors/helmet_detector.py`

## Treinamento dos Modelos

Os modelos podem ser treinados utilizando dados de imagens de pessoas com e sem capacetes. Os dados brutos devem ser armazenados no diretório `data/raw`, enquanto os dados processados devem ser colocados em `data/processed`.

## Instruções para Uso

Para utilizar os modelos no sistema de detecção, siga as instruções abaixo:

1. Certifique-se de que todos os requisitos estão instalados conforme descrito no `requirements.txt`.
2. Execute o script de download de modelos, se necessário:
   - `python scripts/download_models.py`
3. Inicie o sistema de detecção:
   - `python src/main.py`

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](../LICENSE) para mais detalhes.