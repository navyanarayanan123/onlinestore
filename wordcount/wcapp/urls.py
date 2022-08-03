from django.urls import path
from wcapp import views

urlpatterns=[
    path("",views.IndexView.as_view(),name="index"),
    path("wordcount",views.WordCountView.as_view(),name="wordcount"),
    path("vowelcount",views.VowelCountView.as_view(),name="vowelcount")
]