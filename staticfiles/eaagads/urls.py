from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('assets.urls')),  # ✅ Load all routes from the assets app
    path('accounts/', include('django.contrib.auth.urls')),  # ✅ this adds /accounts/login/
 # for login/logout
]
