from django.contrib.auth.views import LoginView
from django.urls import path, include

from .views import main_page

urlpatterns = [
    # Путь к главной странице
    path('', main_page, name='main_page'),
    # Путь к странице авторизации
    path('login/', LoginView.as_view(), name='login'),
    # Путь к приложению материалов
    path('materials/', include('materialslk.urls')),  
    # Путь к приложению списка дополнительной информации (Список учителей, список мероприятий)
    path('info/', include('infolistlk.urls')),
]
