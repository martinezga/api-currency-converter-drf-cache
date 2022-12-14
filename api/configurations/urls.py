"""configurations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.home.urls', 'home'), namespace='home')),
    # OAuth urls
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # Auth
    path('auth/', include(('apps.accounts.urls', 'accounts'), namespace="accounts")),
    # API version 1
    path('v1/', include([
        # Apps urls
        path('', include(('apps.currencies.urls', 'currencies'), namespace="currencies")),
        path('', include(('apps.exchanges.urls', 'exchanges'), namespace="exchanges")),
    ])),
]
