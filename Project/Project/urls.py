"""
URL configuration for projetoAgenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views, viewsLogin, viewsChats
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('agenda/', views.agenda, name='agenda'),
    path('login/', viewsLogin.login_user, name='login'),
    path('login/submit', viewsLogin.submit_login),
    path('logout/', viewsLogin.logout_user, name="logout"),
    path('evento/', views.evento, name='evento'),
    path('evento/submit', views.submit_evento),
    path('delete/<int:id_evento>', views.delete_evento, name="delete"),
    path('enviar_email', views.enviar_email),
    path('chatbot/', viewsChats.chatbot, name="chatbot"),
    path('chatbot/chatbot_submit', viewsChats.chatbot_view, name='chatbot_submit'),
    path('chatbotInterno/submit', viewsChats.chatbotInterno_view, name='chatbotInterno_submit'),
    path('chatbotInterno/', viewsChats.chatbotInterno, name='chatbotInterno'),
    path('chat/', viewsChats.chat, name='chat'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

