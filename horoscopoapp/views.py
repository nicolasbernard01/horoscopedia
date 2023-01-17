from django.shortcuts import render,redirect
from django.contrib import messages
import requests


def horoscopo(request):

	total_signos = {
	
	'aries': 'Aries',
	'tauro': 'Taurus',
	'geminis': 'Gemini',
	'cancer': 'Cancer',
	'leo': 'Leo',
	'virgo': 'Virgo',
	'libra': 'Libra',
	'escorpio': 'Scorpio',
	'sagitario': 'Sagittarius',
	'capricornio': 'Capricorn',
	'acuario': 'Aquarius',
	'piscis': 'Pisces',
	'Aries': 'Aries',
	'Tauro': 'Taurus',
	'Geminis': 'Gemini',
	'Cancer': 'Cancer',
	'Leo': 'Leo',
	'Virgo': 'Virgo',
	'Libra': 'Libra',
	'Escorpio': 'Scorpio',
	'Sagitario': 'Sagittarius',
	'Capricornio': 'Capricorn',
	'Acuario': 'Aquarius',
	'Piscis': 'Pisces'


	}

	if 'sign' in request.POST:

		sign = request.POST['sign']

	else:

		sign = 'Aries'

	try:

		url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/?sign="+total_signos[sign]+'&day=today'

		headers = {
			"X-RapidAPI-Key": "fe956f1f3fmshccd6278365d23fdp1e5983jsn2b0a96a7f84d",
			"X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com"
		}

		response = requests.post(url, headers=headers)

		r = response.json()

		signo = r['description']
		humor = r['mood']
		numero_suerte = r['lucky_number']

		url = "https://text-translator2.p.rapidapi.com/translate"

		payload = "source_language=en&target_language=es&text="+signo
		headers = {
			"content-type": "application/x-www-form-urlencoded",
			"X-RapidAPI-Key": "fe956f1f3fmshccd6278365d23fdp1e5983jsn2b0a96a7f84d",
			"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
		}

		response = requests.request("POST", url, data=payload, headers=headers).json()

		resp_signo = response['data']['translatedText']

		url = "https://text-translator2.p.rapidapi.com/translate"

		payload = "source_language=en&target_language=es&text="+humor
		headers = {
			"content-type": "application/x-www-form-urlencoded",
			"X-RapidAPI-Key": "fe956f1f3fmshccd6278365d23fdp1e5983jsn2b0a96a7f84d",
			"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
		}

		response = requests.request("POST", url, data=payload, headers=headers).json()

		resp_humor = response['data']['translatedText']

		return render(request, 'horoscopoapp\index.html', {'sign':sign, 'resp_signo':resp_signo, 'resp_humor':resp_humor,'numero':numero_suerte})

	
	except KeyError or ValueError:

		messages.error(request, 'Verifica el signo que haz introducido')

		return redirect('index')

	
	
	
