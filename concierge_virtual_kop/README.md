# Concierge Virtual - Kopenhagen Tacaruna

Este é o bot da Kopenhagen Tacaruna para atendimento automático via WhatsApp Cloud API.

## Como usar

1. Copie o arquivo `.env.example` para `.env` e preencha com suas credenciais.
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Execute o app localmente ou faça deploy no Render/Railway.
4. Configure seu webhook na Meta com a URL `/webhook`.

## Variáveis de ambiente

- ACCESS_TOKEN
- PHONE_NUMBER_ID
- VERIFY_TOKEN
