from django.urls import path
from . import views

urlpatterns = [
    # path('students/',views.studentView ),
    # path('students/<int:pk>',views.studentDetailsView),
    path('students/',views.studentView.as_view() ),
    path('students/<int:pk>',views.studentDetailsView.as_view()),

    path('employee/',views.Employees.as_view()),
    path('employee/<int:pk>',views.EmployeesDetails.as_view())
    
]