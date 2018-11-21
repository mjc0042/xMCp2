"""xMCp2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from catalog.views import CatalogView
from member.views import MemberView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('auth/obtain_token/', obtain_jwt_token),
    #path('auth/refresh_token/', refresh_jwt_token),
    #path('auth/verify_token/', verify_jwt_token),
    path('api/create/user', MemberView.create_member),
    path('api/login/user/<str:username>/<str:password>', MemberView.login),
    path('api/member/(<member_id>[0-9]+', MemberView.get_member),
    path('api/products/', CatalogView.product_list),
    path('api/products/(<pk>[0-9]+)', CatalogView.product_detail),
    #path('api/', include(router.urls)),
    #path('member', TemplateView.as_view(template_name='index.html')),
]
