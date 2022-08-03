from django.urls import path
from owner import views
urlpatterns = [
    path("home",views.OwnerHomeView.as_view(),name='index'),
    path("books/add",views.AddBookView.as_view(),name='addbook'),
    path("emp/add",views.AddEmployeeView.as_view(),name='addemp'),
    path("books/all",views.BookListView.as_view(),name='booklist'),
    path("books/<int:id>",views.BookDetailView.as_view(),name='bookdetail'),
    path("books/change/<int:id>",views.BookEditView.as_view(),name='editbook'),
    path("books/remove/<int:id>",views.BookDeleteView.as_view(),name='removebook')
    ]