import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


URL = 'https://api.covid19api.com/'


# Pega a data do primero caso reportado no pais passado
def dayOne(country):
  URI = URL + f'dayone/country/{country}/status/confirmed'
  response = requests.request("GET", URI, verify=False)
  if(response.status_code == 200):
      res = response.json()
      return res[0]['Date']
  return 'Erro ao acessar a API'

# Pega o numero total acumulado de casos confirmados no pais passado
def confirmed(country):
  res = getSummaryDataFor(country)
  return res['TotalConfirmed']

# Pega o numero total acumulado de casos recuperados no pais passado
def recovered(country):
  res = getSummaryDataFor(country)
  return res['TotalConfirmed']- res['TotalDeaths']

# Pega o numero total acumulado de mortes no pais passado
def deaths(country):
  res = getSummaryDataFor(country)
  return res['TotalDeaths']


# Pega o numero total de mortes acumuladas no mundo no dia de hoje
def newDeaths():
  res = getSummaryData()
  return res['Global']['NewDeaths']

# Pega o numero total de casos ativos no Brazil
def active(country):
  URI = URL + f'live/country/{country}/status/confirmed'
  response = requests.request("GET", URI, verify=False)
  if(response.status_code == 200):
    res = response.json()
    active = 0
    res = res[len(res)-27 : len(res)]
    for state in res:
      active += state['Active']
    return active


# Pega o nome do pais com maior numero de casos confirmados acumuladas
def countryWithMostCases():
  res = getSummaryData()
  champion = ''
  deaths   = 0
  for country in res['Countries']:
    if (country['TotalDeaths'] > deaths):
      deaths   = country['TotalConfirmed']
      champion = country['Country']
  return champion

# Pega o nome do pais com maior numero de mortes acumuladas
def countryWithMostDeaths():
  res = getSummaryData()
  champion = ''
  deaths   = 0
  for country in res['Countries']:
     if (country['TotalDeaths'] > deaths):
      deaths   = country['TotalDeaths']
      champion = country['Country']
  return champion


# Coleta dados da API de Summary        
def getSummaryData():
  URI     = URL + 'summary'
  response = requests.request("GET", URI, verify=False)

  if(response.status_code == 200):
    return response.json()
  return 'Erro ao acessar a API'

# Coleta dados da API de Summary para um pais
def getSummaryDataFor(country):
  country  = country.capitalize() 
  res = getSummaryData()
  for c in res['Countries']:
    if(c['Country'] == country):
      return c

  return 'Erro ao acessar a API'


# Coleta todos os paises
def getCountries():
  URI = URL + 'countries'
  response = requests.request("GET", URI, verify=False)
  if(response.status_code == 200):
    return response.json()
  return 'Erro ao acessar a API'
  