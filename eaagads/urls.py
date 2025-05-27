from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('assets.urls')),  # ✅ Load all routes from the assets app
    path('login/', include('django.contrib.auth.urls')),  # for login/logout
]
