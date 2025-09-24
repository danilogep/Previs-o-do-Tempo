PREVISÃO DO TEMPO
Uma aplicação de linha de comando em Python que fornece a previsão do tempo atualizada para qualquer cidade do mundo. Este projeto é um exemplo prático de como integrar um software com serviços externos para obter dados em tempo real.

✨ Funcionalidades
	- Consulta por Nome da Cidade: Basta digitar o nome de uma cidade para obter a previsão do tempo.
	- Seleção Interativa: Caso a busca retorne múltiplas cidades com o mesmo nome, um menu é exibido para que o usuário escolha a localidade correta.
	- Dados Meteorológicos Essenciais: Exibe a condição do tempo (céu limpo, nublado, chuva), as temperaturas máxima e mínima, e a velocidade máxima do vento.
	- Descrições Amigáveis: Converte os códigos de clima (WMO) da API em descrições claras e em português, acompanhadas de emojis.
	- Tratamento de Erros: Lida de forma robusta com erros de conexão ou cidades não encontradas.

🚀 Demonstração
	- Veja um exemplo de como o programa funciona no terminal: python clima_cidade.py

Digite o nome da cidade para a previsão do tempo: Joao Pessoa
========================================
PREVISÃO DO TEMPO PARA: JOÃO PESSOA, BRAZIL
========================================
Data: 23/09/2025
Condição: 🌤️ Principalmente limpo
🌡️ Temperatura Máxima: 28.5°C
🌡️ Temperatura Mínima: 24.2°C
💨 Vento Máximo: 21.7 km/h
========================================

🔗 APIs Utilizadas
	- Este projeto depende inteiramente dos dados fantásticos fornecidos pela Open-Meteo, uma API de código aberto e gratuita para dados meteorológicos.
	- Open-Meteo Geocoding API: Utilizada para converter o nome da cidade digitado pelo usuário em coordenadas geográficas precisas (latitude e longitude).
	- Open-Meteo Weather Forecast API: Utilizada para obter os dados da previsão do tempo com base nas coordenadas fornecidas pela API de Geocodificação.

🛠️ Tecnologias Utilizadas
	- Python 3: Linguagem principal do projeto.
	- Biblioteca requests: Para fazer as requisições HTTP às APIs externas de forma eficiente.
	- Biblioteca datetime: Para formatar as datas recebidas da API em um padrão legível (DD/MM/AAAA).

⚙️ Como Usar

1. git clone https://github.com/[SEU-USUARIO-GITHUB]/[NOME-DO-SEU-REPOSITORIO].git
2. Navegue até a pasta do projeto: cd [NOME-DO-SEU-REPOSITORIO]
3. O projeto requer a biblioteca requests. Instale-a com o seguinte comando: pip install requests
4. Com tudo pronto, execute o programa: python clima_cidade.py
5. O programa solicitará que você digite o nome de uma cidade.
