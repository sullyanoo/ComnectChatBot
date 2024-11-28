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


## Bloco Login --------------------------------------------------------------------------------------------------------------------------------------------------------------

def login_user(request):
    return render(request, 'login.html')

def logout_user(request): # Log out of the page
    logout(request)
    return redirect('login')

def submit_login(request): # Feature Login
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) # authenticate user.
        if user is not None:
            login(request, user)
            return redirect("/agenda/")
        else:
            messages.error(request, "Usuário ou senha inválido!")
    return redirect('login')