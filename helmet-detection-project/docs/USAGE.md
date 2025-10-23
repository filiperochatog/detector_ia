# Uso do Sistema de Detecção de Capacetes

Este documento fornece instruções detalhadas sobre como usar o sistema de detecção de capacetes.

## Pré-requisitos

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Verifique se você possui uma câmera conectada e funcionando no seu notebook.

## Instalação

1. Clone o repositório do projeto:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd helmet-detection-project
   ```

2. Instale as dependências do projeto executando o comando:
   ```
   pip install -r requirements.txt
   ```

3. Baixe os modelos necessários executando o script:
   ```
   python scripts/download_models.py
   ```

## Execução

Para executar a aplicação, utilize o seguinte comando:
```
python src/app.py
```

## Funcionamento

- Ao executar o sistema, a câmera do notebook será aberta.
- O sistema começará a monitorar se as pessoas estão usando capacete.
- Se alguém não estiver usando capacete, uma mensagem será exibida na tela alertando sobre a falta do Equipamento de Proteção Individual (EPI).

## Observações

- Certifique-se de que a câmera esteja liberada para uso pelo sistema.
- O desempenho do sistema pode variar dependendo das especificações do seu hardware.