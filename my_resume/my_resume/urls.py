from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('', include('resume.urls', namespace='resume')),
    path('admin/', admin.site.urls),
]
