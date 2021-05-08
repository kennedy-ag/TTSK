from django.shortcuts import render
import tweepy
import re

def index(request):
	return render(request, 'index.html')

def busca_30_dias(request):
	return render(request, 'busca_mensal.html')

def busca_7_dias(request):
	return render(request, 'busca_semanal.html')

def exemplos(request):
	return render(request, 'exemplos.html')

def sobre(request):
	return render(request, 'sobre.html')

def buscar(request):
	requisicao = dict(request.GET)
	idioma = requisicao['idioma'][0]
	keywords = requisicao['busca'][0]

	# Credenciais

	consumer_key = "OWPItxGFF5e146jrcbsPMCs83"
	consumer_secret_key = "ZUxSH8ziCj5pWL4steFrv5ob9CQdmpmHa01AAGDBtxjzDqTHLg"
	access_token = "882377451720122368-wH3JkhYE78C5Y0L4c7R75qmLRQE4LP6"
	access_token_secret = "kcOKYhMc30lw7mKvACmgTrvt4y8VOzCwbSoS0Xc3Udv99"

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

	  i += 1

	if len(lista_de_dados)>0:
		mensagem = ''
	else: mensagem = 'Nenhum tweet encontrado no momento... Talvez mais tarde.'

	return render(request, 'busca_semanal.html', {'dados': lista_de_dados, 'quantidade': len(lista_de_dados), 'mensagem': mensagem})


def busca_mensal(request):
	requisicao = dict(request.GET)
	keywords = requisicao['busca'][0]
	quantidade = int(requisicao['quantidade'][0])

	# Credenciais
	consumer_key = "OWPItxGFF5e146jrcbsPMCs83"
	consumer_secret_key = "ZUxSH8ziCj5pWL4steFrv5ob9CQdmpmHa01AAGDBtxjzDqTHLg"
	access_token = "882377451720122368-wH3JkhYE78C5Y0L4c7R75qmLRQE4LP6"
	access_token_secret = "kcOKYhMc30lw7mKvACmgTrvt4y8VOzCwbSoS0Xc3Udv99"

	# Autenticação
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
	auth.set_access_token(access_token, access_token_secret)
	token = tweepy.API(auth)

	lista_de_dados = []
	lista_de_textos = []
	tweets = tweepy.Cursor(token.search_30_day,environment_name='TweetFromTheOthers', query=keywords).items()


	controlador = 0
	for tweet in tweets:
	  user = tweet._json['user']
	  if tweet.text not in lista_de_textos:
	  	lista_de_textos.append(tweet.text)
	  	lista_de_dados.append([user['screen_name'], user['name'], tweet._json['text'], tweet._json['created_at'][0:-10]])
	  	controlador += 1
	  	if controlador == quantidade:
	  		break

	for i in range(1, len(lista_de_dados)+1):
		lista_de_dados[i-1].append(i)


	if len(lista_de_dados)>0:
		mensagem = ''
	else: mensagem = 'Nenhum tweet encontrado no momento... Talvez mais tarde.'



	return render(request, 'busca_mensal.html', {'dados': lista_de_dados, 'quantidade': len(lista_de_dados), 'mensagem': mensagem})