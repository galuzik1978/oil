from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("import/", views.ImportFile.as_view(), name="file-import"),
    path("thanks/", views.SuccessLoadedView.as_view(), name="thanks"),
    path("notready/", views.NotReadyView.as_view(), name="notready")
]
