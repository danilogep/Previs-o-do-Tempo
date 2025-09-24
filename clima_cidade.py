import requests
from datetime import datetime

# URLs base para as APIs do Open-Meteo
GEOCODING_API_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"

# Dicionário para traduzir os códigos de clima (WMO) para descrições amigáveis
WMO_CODES = {
    0: "☀️ Céu limpo",
    1: "🌤️ Principalmente limpo",
    2: "🌥️ Parcialmente nublado",
    3: "☁️ Nublado",
    45: "🌫️ Nevoeiro",
    48: "🌫️ Nevoeiro depositando geada",
    51: "🌧️ Chuvisco leve",
    53: "🌧️ Chuvisco moderado",
    55: "🌧️ Chuvisco denso",
    61: "🌦️ Chuva fraca",
    63: "🌧️ Chuva moderada",
    65: "⛈️ Chuva forte",
    80: "🌦️ Pancadas de chuva fracas",
    81: "🌧️ Pancadas de chuva moderadas",
    82: "⛈️ Pancadas de chuva violentas",
    95: "🌩️ Trovoada",
}

def obter_coordenadas(cidade):
    """Busca as coordenadas (latitude e longitude) de uma cidade."""
    params = {'name': cidade, 'count': 10, 'language': 'pt', 'format': 'json'}
    try:
        response = requests.get(GEOCODING_API_URL, params=params)
        response.raise_for_status()  # Lança um erro para respostas ruins (4xx ou 5xx)
        resultados = response.json().get('results', [])
        return resultados
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao buscar coordenadas: {e}")
        return None

def selecionar_cidade(resultados):
    """Permite ao usuário selecionar a cidade correta de uma lista de resultados."""
    if not resultados:
        print("Nenhuma cidade encontrada com esse nome.")
        return None
    
    if len(resultados) == 1:
        return resultados[0]

    print("Várias cidades encontradas. Por favor, escolha a correta:")
    for i, local in enumerate(resultados):
        # Exibe nome, estado (se houver) e país
        nome_exibicao = f"{local.get('name', '')}, {local.get('admin1', '')} - {local.get('country', '')}"
        print(f"{i + 1}: {nome_exibicao}")
    
    while True:
        try:
            escolha = int(input("Digite o número da sua escolha: "))
            if 1 <= escolha <= len(resultados):
                return resultados[escolha - 1]
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número.")

def obter_previsao(lat, lon):
    """Busca a previsão do tempo para uma dada latitude e longitude."""
    params = {
        'latitude': lat,
        'longitude': lon,
        'daily': 'weather_code,temperature_2m_max,temperature_2m_min,wind_speed_10m_max',
        'timezone': 'America/Sao_Paulo'
    }
    try:
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao buscar previsão do tempo: {e}")
        return None

def exibir_previsao(previsao, info_cidade):
    """Formata e exibe a previsão do tempo para o usuário."""
    if not previsao or not previsao.get('daily'):
        print("Não foi possível obter a previsão do tempo.")
        return

    print("\n" + "="*40)
    nome_cidade = f"{info_cidade.get('name')}, {info_cidade.get('country')}"
    print(f"PREVISÃO DO TEMPO PARA: {nome_cidade.upper()}")
    print("="*40)

    previsao_diaria = previsao['daily']
    data_hoje = datetime.strptime(previsao_diaria['time'][0], '%Y-%m-%d').strftime('%d/%m/%Y')
    
    codigo_clima = previsao_diaria['weather_code'][0]
    descricao_clima = WMO_CODES.get(codigo_clima, "Condição do tempo desconhecida")
    
    print(f"Data: {data_hoje}")
    print(f"Condição: {descricao_clima}")
    print(f"🌡️ Temperatura Máxima: {previsao_diaria['temperature_2m_max'][0]}°C")
    print(f"🌡️ Temperatura Mínima: {previsao_diaria['temperature_2m_min'][0]}°C")
    print(f"💨 Vento Máximo: {previsao_diaria['wind_speed_10m_max'][0]} km/h")
    print("="*40)

# Função principal que executa o programa
def main():
    """Função principal para orquestrar as chamadas do programa."""
    cidade_input = input("Digite o nome da cidade para a previsão do tempo: ")
    
    resultados_cidades = obter_coordenadas(cidade_input)
    
    if resultados_cidades:
        cidade_escolhida = selecionar_cidade(resultados_cidades)
        
        if cidade_escolhida:
            lat = cidade_escolhida['latitude']
            lon = cidade_escolhida['longitude']
            
            dados_previsao = obter_previsao(lat, lon)
            
            if dados_previsao:
                exibir_previsao(dados_previsao, cidade_escolhida)

if __name__ == "__main__":
    main()