from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('login/' , views.loginPage, name="login"),
    path('logout/' , views.logoutUser, name="logout"),
    path('register/' , views.registerPage, name="register"),
    path('providerForm/' , views.providerForm, name="providerForm"),
    

    path('' , views.home, name="home"),
    path('catagoryProviders/<str:pk>/' , views.catagoryProviders, name="catagoryProviders"),
    path('profile/<str:pk>/' , views.profile, name="profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
