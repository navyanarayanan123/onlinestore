from django.urls import path
from customer import views
urlpatterns = [
    path("all/",views.ListAllView.as_view(),name="allbooks"),
    path("accounts/signup/",views.SignupView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("accounts/signout",views.Sign_out,name="signout"),
    path("customer/cart/add/<int:id>",views.AddToCartView.as_view(),name="addtocart"),
    path("customer/cart/items",views.CartItemsView.as_view(),name="cartitems"),
    path("customer/cart/items/remove/<int:id>",views.RemoveCartItemView.as_view(),name="removecartitem")
    ]

