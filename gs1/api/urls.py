from django.urls import path
from api import views
from .views import student_details
from .views import student_list
urlpatterns = [
    path('stuinfo/<int:pk>', views.student_details.as_view()),
    path('stuinfo/', views.student_list.as_view()),
]