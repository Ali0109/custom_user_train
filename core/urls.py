from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    # path('users/', include('main_app.urls')),
    # path('users/', include('django.contrib.auth.urls')),
]
