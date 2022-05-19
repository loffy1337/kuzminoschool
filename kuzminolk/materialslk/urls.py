from django.urls import path

from . import views

urlpatterns = [
    # Пути к страницам материалов для обучения
    path('for_study/', views.for_study, name='for_study'),
    path('for_study/parts/<int:subject_id>/', views.for_study_parts, name='for_study_parts'),
    path('for_study/parts/detail/<slug:theme_slug>/', views.for_study_detail, name='for_study_detail'),
    # Пути к страницам методических материалов
    path('methodical/', views.methodical, name='methodical'),
    path('methodical/parts/<int:subject_id>/', views.methodical_parts, name='methodical_parts'),
    path('methodical/parts/detail/<slug:theme_slug>/', views.methodical_detail, name='methodical_detail'),
    # Пути к избранным материалам
    path('favourites/add/<str:type_of_material>/<slug:theme_slug>/', views.favourites_add, name='favourites_add'),
    path('favourites/', views.favourites, name='favourites'),
]
