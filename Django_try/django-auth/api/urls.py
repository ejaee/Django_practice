from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/v1/', include('accounts.urls')),
    path('api/dashboard/v1/', include('accounts.urls')),
]