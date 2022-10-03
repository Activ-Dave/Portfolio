"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='API portfolio by Wąsi',
        default_version='v1',
        descritpion='WąsiPhotografp photo portfolio',
        terms_of_service='',
        #contact=openapi.Contact(email='dawidwasala92@gmail.com')
        license=openapi.License(name='(c) 2022 | OpenSource')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/v1/',include('portal.urls')),
    path('swager/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
