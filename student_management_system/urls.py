"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from student_management_app import views, HodViews
from student_management_system import settings

urlpatterns = [
                  path('demo', views.showDemoPage),
                  path('admin/', admin.site.urls),
                  path('', views.ShowLoginPage),
                  path('get_user_deatials', views.GetUserDetails),
                  path('logout_user', views.logout_user),
                  path('dologin', views.doLogin),
                  path('admin_home', HodViews.admin_home),
                  path('logout', views.logout),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
