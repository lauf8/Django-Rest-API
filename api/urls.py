from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('locador/', include('app.urls')),
    path('account/', include('autenticacao.urls')),
    path('objeto/', include('objetos.urls')),
    path('emprestimo/', include('emprestimos.urls')),
]
