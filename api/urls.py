from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee',views.EmployeeViewSet)

urlpatterns = [
    # path('students/',views.studentView ),
    # path('students/<int:pk>',views.studentDetailsView),
    path('students/',views.studentView.as_view() ),
    path('students/<int:pk>',views.studentDetailsView.as_view()),

    # path('employee/',views.Employees.as_view()),
    # path('employee/<int:pk>',views.EmployeesDetails.as_view())

    path('',include(router.urls)),
    
]