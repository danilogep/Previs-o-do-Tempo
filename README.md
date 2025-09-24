PREVISÃO DO TEMPO
Uma aplicação de linha de comando em Python que fornece a previsão do tempo atualizada para qualquer cidade do mundo. Este projeto é um exemplo prático de como integrar um software com serviços externos para obter dados em tempo real.

✨ Funcionalidades
1. Consulta por Nome da Cidade: Basta digitar o nome de uma cidade para obter a previsão do tempo.
2. Seleção Interativa: Caso a busca retorne múltiplas cidades com o mesmo nome, um menu é exibido para que o usuário escolha a localidade correta.
3. Dados Meteorológicos Essenciais: Exibe a condição do tempo (céu limpo, nublado, chuva), as temperaturas máxima e mínima, e a velocidade máxima do vento.
4. Descrições Amigáveis: Converte os códigos de clima (WMO) da API em descrições claras e em português, acompanhadas de emojis.
5. Tratamento de Erros: Lida de forma robusta com erros de conexão ou cidades não encontradas.

🔗 APIs Utilizadas
1. Este projeto depende inteiramente dos dados fantásticos fornecidos pela Open-Meteo, uma API de código aberto e gratuita para dados meteorológicos.
2. Open-Meteo Geocoding API: Utilizada para converter o nome da cidade digitado pelo usuário em coordenadas geográficas precisas (latitude e longitude).
3. Open-Meteo Weather Forecast API: Utilizada para obter os dados da previsão do tempo com base nas coordenadas fornecidas pela API de Geocodificação.

🛠️ Tecnologias Utilizadas
1. Python 3: Linguagem principal do projeto.
2. Biblioteca requests: Para fazer as requisições HTTP às APIs externas de forma eficiente.
3. Biblioteca datetime: Para formatar as datas recebidas da API em um padrão legível (DD/MM/AAAA).

⚙️ Como Usar

1. git clone https://github.com/danilogep/Previsao_Do_Tempo.git
2. Navegue até a pasta do projeto: cd [NOME-DO-SEU-REPOSITORIO]
3. O projeto requer a biblioteca requests. Instale-a com o seguinte comando: pip install requests
4. Com tudo pronto, execute o programa: python clima_cidade.py
5. O programa solicitará que você digite o nome de uma cidade.
