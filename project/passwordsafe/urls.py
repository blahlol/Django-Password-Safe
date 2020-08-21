"""passwordsafe URL Configuration

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
from django.urls import include,path
from . import views
from safe import views as safe_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',safe_views.home,name='home'),
    path('safe/',include('safe.urls')),
    path('login/',views.login_view,name="login"),
    path('signup/',views.signup_view,name='signup'),
    path('admin/', admin.site.urls),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)