from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('goos69.pythonanywhere.com', include('polls.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
