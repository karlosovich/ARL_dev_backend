from django.contrib                 import admin
from django.urls                    import path
from authAppExample                 import views  as authAppViews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/',                                  admin.site.urls),  # use defaul Djando Admin
    path('login/',                                  TokenObtainPairView.as_view()), # use credentials to return tokens
    path('refresh/',                                TokenRefreshView.as_view()), # generate new access token
    path('user/',                                   authAppViews.UserCreateView.as_view()), # create a new user
    path('user/<int:pk>/',                          authAppViews.UserDetailView.as_view()), # check info for an specific user based on id(pk)
    path('transaction/create/',                     authAppViews.TransactionCreateView.as_view()), # create a new transaction
    path('transaction/<int:user>/<int:pk>/',        authAppViews.TransactionsDetailView.as_view()), # view information for a transaction
    path('transaction/update/<int:user>/<int:pk>/', authAppViews.TransactionsUpdateView.as_view()), # update a transaction
    path('transaction/remove/<int:user>/<int:pk>/', authAppViews.TransactionsDeleteView.as_view()), # delete a transaction
    path('transactions/<int:user>/<int:account>/',  authAppViews.TransactionsAccountView.as_view()), # view all transactions for an specific account
    path('deposit/create/',                     authAppViews.DepositCreateView.as_view()), # create a new deposit
    path('deposit/<int:user>/<int:pk>/',        authAppViews.DepositDetailView.as_view()), # view information for a deposit
    path('deposits/<int:user>/<int:account>/',  authAppViews.DepositsAccountView.as_view()), # view all depositss for an specific account
]