from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='app'
urlpatterns = [
    path('', views.home, name='home'),
    path('passeios', views.passeios, name='passeios'),
    path('contato', views.contato, name='contato'),
    path('values/<int:id>', views.values, name='values'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)