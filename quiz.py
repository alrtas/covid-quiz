import sources as src
import helpers as hlp
import random

country    = 'brazil'

dayOne     = src.dayOne(country) 
confirmed  = src.confirmed(country)
recovered  = src.recovered(country)
deaths     = src.deaths(country)
newDeaths  = src.newDeaths()
mostDeaths = src.countryWithMostDeaths()
mostCases  = src.countryWithMostCases() 


rawQuestions = [
    {
      "question" : "Qual foi a data do primeiro caso de COVID 19 no Brasil?",
      "response" : dayOne,
      "options"  : hlp.format((hlp.createOptionsForDates(dayOne))),
      "answer"   : "",
      "correct"  : False
    },
    {
      "question" : "Quantos casos confirmados tivemos hoje em todo o pais?",
      "response" : confirmed,
      "options"  : hlp.format(hlp.createOptionsForNumbers(confirmed)),
      "answer"   : "",
      "correct"  : False
    },
    {
      "question" : "Quantos casos confirmados no Brasil conseguiram se recuperar?",
      "response" : recovered,
      "options"  : hlp.format(hlp.createOptionsForNumbers(recovered)),
      "answer"   : "",
      "correct"  : False
    },
    {
      "question" : "Quantos casos confirmados no Brasil evoluiram ao falecimento?",
      "response" : deaths,
      "options"  : hlp.format(hlp.createOptionsForNumbers(deaths)),
      "answer"   : "",
      "correct"  : False
    },
    {
      "question" : "Qual pais apresentou o maior indice de casos confirmados no mundo?",
      "response" : mostCases,
      "options"  : hlp.format(hlp.createOptionsForCountries(mostCases)),
      "answer"   : "",
      "correct"  : False
    },
    {
      "question" : "Qual pais apresentou o maior indice de mortes no mundo?",
      "response" : mostDeaths,
      "options"  : hlp.format(hlp.createOptionsForCountries(mostDeaths)),
      "answer"   : "",
      "correct"  : False
    },
    {
      "question" : "Quantos casos evoluiram a morte hoje no mundo?",
      "response" : newDeaths,
      "options"  : hlp.format(hlp.createOptionsForNumbers(newDeaths)),
      "answer"   : "",
      "correct"  : False
    }
]

questions = hlp.shuffleAndReturn(rawQuestions)