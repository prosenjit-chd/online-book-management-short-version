from django.urls import path
from. import views

urlpatterns =[
    path('', views.index),
    path('books/', views.bookList, name='books'),
    path('create_books/', views.createBook, name= 'create_books'),
    path('update_books/<str:pk>/', views.updateBook, name= 'update_books'),
    path('delete_books/<str:pk>/', views.deleteBook, name= 'delete_books'),

    path('user_List/', views.userList, name='user_List'),
    path('user_create/', views.createUser, name= 'user_create'),
    path('user_update/<str:pk>/', views.updateUser, name= 'user_update'),
    path('user_delete/<str:pk>/', views.deleteUser, name= 'user_delete'),

    path('rent_List/', views.rentList, name='rent_List'),
    path('rent_create/', views.createRent, name='rent_create' ),
    path('rent_update/<str:pk>/', views.updateRent, name= 'rent_update'),
]