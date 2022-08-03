from django.urls import path
from operations import views
urlpatterns=[
    path("",views.IndexView.as_view(),name="index"),
    path("add",views.AddView.as_view(),name="add"),
    path("sub",views.SubView.as_view(),name="sub"),
    path("mul",views.MulView.as_view(),name="mul"),
    path("div",views.DivView.as_view(),name="div"),
    path("square",views.SquareView.as_view(),name="square"),
    path("cube",views.CubeView.as_view(),name="cube"),
    path("fact",views.FactView.as_view(),name="fact")
]