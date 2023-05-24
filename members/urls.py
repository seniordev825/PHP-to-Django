from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    

    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # change password urls
    # path('password-change/',
    #      auth_views.PasswordChangeView.as_view(),
    #      name='password_change'),
    # path('password-change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),

    # reset password urls
    # path('password-reset/',
    #      auth_views.PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('password-reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('password-reset/complete/',
    #      auth_views.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),

  
    path('', views.user_login, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('login1/', views.user_login, name='login1'),
    path('forget/', views.forget, name='forget'),
    path('register/', views.register, name='register'),
    path('usercompany/', views.usercompany, name='usercompany'),
    path('userpayment/', views.userpayment, name='userpayment'),
    path('clientdashboard/', views.clientdashboard, name='clientdashboard'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('saveusercompany1/', views.saveusercompany1, name='saveusercompany1'),
    path('saveuserpayment1/', views.saveuserpayment1, name='saveuserpayment1'),
    path('saveclient/', views.saveclient, name='saveclient'),
    path('invoicedashboard/', views.invoicedashboard, name='invoicedashboard'),
    path('goodsdashboard/', views.goodsdashboard, name='goodsdashboard'),
    #path('addinvoice/', views.addinvoice, name='addinvoice'),
    path('saveinvoice1/', views.saveinvoice1, name='saveinvoice1'),
    path('saveproduct/', views.saveproduct, name='saveproduct'),
    path('savegoods/', views.savegoods, name='savegoods'),
    path('pdf/<int:id>',views.render_pdf_view,name='pdf')
      
]
