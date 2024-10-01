from django.urls import path
from home import views

from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    
    path('', views.home, name='home'),
    path('market', views.market, name='market'),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
