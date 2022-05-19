from django.shortcuts import render

def main_page(request):
    """Функция осуществляет обработку и рендеринг главной страницы веб-приложения"""
    return render(request, 'mainlk/main_page.html')
