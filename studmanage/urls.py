from django.urls import path
from .views import CheckEmailExists, StudentCreateView, StudentDeleteView, StudentDetailView, StudentEditView, StudentListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/create/', StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('students/edit/<int:pk>/', StudentEditView.as_view(), name='student-edit'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('check-email/', CheckEmailExists.as_view(), name='check-email'),

]
    