from django.urls import path
from Usermanage import views

urlpatterns = [
    path('Usermanage/', views.UserList.as_view()),
    path('Usermanage/<int:pk>/', views.UserDetail.as_view()),
]