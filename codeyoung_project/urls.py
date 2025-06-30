from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('codeyoung_api.urls')),  # ✅ Includes your app’s URLs
]
