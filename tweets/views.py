from django.shortcuts import render
import tweepy
import re

def index(request):
	return render(request, 'index.html')

def buscar(request):
	requisicao = dict(request.GET)
	idioma = requisicao['idioma'][0]
	keywords = requisicao['busca'][0]

	# Credenciais
	consumer_key = "nGFKutA5OZC0VIe8t3HzI4gyo"
	consumer_secret_key = "3O4KMmSNyTBIJpQkMG1IP4NjRtF5czogVYUO1Lqz89fT91Yh6L"
	access_token = "882377451720122368-NYca0un6atcVwM0VHhqJSvLn07mgiFr"
	access_token_secret = "m6AWSW2FfrBbd3gJA7N0cVY4a7qoKiONKQ5YR2MOyp1DU"

	# Autenticação
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
	auth.set_access_token(access_token, access_token_secret)
	token = tweepy.API(auth)

	# Busca
	keywords = (keywords)
	lista_de_dados = []
	tweets = token.search(q=keywords, count=100, result_type='mixed', lang=idioma)
	i = 1
	for tweet in tweets:
	  user = tweet._json['user']
	  lista_de_dados.append([i, user['screen_name'], user['name'], tweet._json['text'], tweet._json['created_at'][0:-10]])

	  #user['location']

	  i += 1

	if len(lista_de_dados)>0:
		mensagem = ''
	else: mensagem = 'Nenhum tweet encontrado no momento... Talvez mais tarde.'

	return render(request, 'index.html', {'dados': lista_de_dados, 'quantidade': len(lista_de_dados), 'mensagem': mensagem})