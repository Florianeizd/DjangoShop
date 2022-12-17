from django.urls import path
from . import views
from django.contrib import admin

app_name = 'app_projet'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/', views.article, name='article'),
    path('show/', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('destroy/<int:id>', views.destroy, name='destroy'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('cart/', views.cart, name='cart')

]