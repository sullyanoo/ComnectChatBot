from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required # Realizando isso ele só irá abrir a minha página se eu estiver logado.
from django.contrib.auth import authenticate, login, logout
#from tensorflow.keras.utils import to_categorical
#from tensorflow.keras.preprocessing.text import Tokenizer
#from tensorflow.keras.preprocessing.sequence import pad_sequences
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Embedding, LSTM, Dense
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from App.models import Evento
from django.conf import settings
from datetime import datetime
from docx import Document
from django.conf import settings
from spellchecker import SpellChecker # Biblioteca corrige acentuação da frase
import numpy as np
import logging
import uuid
import os
import re
logger = logging.getLogger('django')

# Create your views here.

## Bloco home --------------------------------------------------------------------------------------------------------------------------------------------------------------

def index(request):
    return render(request, 'index.html')

## Bloco agenda ---------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def submit_evento(request): # Feature for increment data in database.
    if request.POST:
        title = request.POST.get('title')
        datetime = request.POST.get('datetime')
        description = request.POST.get('description')
        local = request.POST.get('address')
        user = request.user
        id_event = request.POST.get('id') # Esse Id eu só pego para poder fazer a edição.
        protocol = generateProtocol() # Generate random protocol.
        if id_event:
            Evento.objects.filter(id=id_event).update(titulo = title, descricao = description, data_evento = datetime, local=local)
        else:
            Evento.objects.create(titulo = title, descricao = description, data_evento = datetime, usuario = user, local=local, protocolo=protocol)
            messages.success(request, f"Adicionado um novo evento com sucesso aqui está seu protocolo: {protocol}")

    return redirect("/agenda/") # redirect to home.

def generateProtocol(): # Função que gera o token do evento, essa função está sendo utilizada no submit_evento.
    protocol = str(uuid.uuid4())
    return protocol

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    user = request.user
    event = Evento.objects.get(id=id_evento)
    if user == event.usuario: # Valida se aquele evento é daquele usuário, se não for ele não exclui.
        event.delete() # Id receive and event delete.
    return redirect('/agenda/')

@login_required(login_url='/login/')
def evento(request):
    id_event = request.GET.get("id")
    data = {}
    if id_event:
        data['evento'] = Evento.objects.get(id = id_event)
    return render(request, 'evento.html', data)


@login_required(login_url='/login/') # Coloco isso pra identificar que as funções abaixo são decoradores.
def agenda(request):
    user = request.user
    username = user.username
    #data_atual = datetime.now() # Pega o horário atual
    event = Evento.objects.filter(usuario=user) # Cath all the files into my class Evento # __gt se refere á um valor maior __lt para um valor menor. # Fazendo essa query ele só irá me trazer os eventos futuros e não mais os que venceram.
    data = {'eventos': event, 'username': username}
    return render(request, "agenda.html", data)


## Bloco enviar e-mail ------------------------------------------------------------------------------------------------------------------------------------------------------

def enviar_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        destination_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Mensagem com detalhes adicionais (se necessário)
        full_message = f"Mensagem de: {name}\n\n{message}"
        try:
            # Envio do e-mail com o cabeçalho "Reply-To" opcional
            email = EmailMessage(
                subject,
                full_message,
                'lolegario@comnect.com.br',  # Remetente deve ser igual ao EMAIL_HOST_USER
                ['luciano_guilherme@outlook.com'],
                headers={'Reply-To': destination_email}  # Opcional
            )
            email.send(fail_silently=False)
            return HttpResponse("Email enviado com sucesso")
        except Exception as e:
            return HttpResponse(f"Erro ao enviar e-mail: {str(e)}")
    else:
        return HttpResponse("Método HTTP não permitido")




