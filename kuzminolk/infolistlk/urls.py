from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Путь к списку преподавателей
    path('teachers_list/', views.teachers_list, name='teachers_list'),
    # Путь к списку мероприятий
    # path('events_list/', views.events_list, name='events_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
