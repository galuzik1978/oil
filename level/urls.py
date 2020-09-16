from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("import/", views.ImportFile.as_view(), name="file-import")
]
