from django.urls import path, include
from contact_us import views

urlpatterns = [
    path('feedback-create/', views.FeedbackCreate.as_view()),
    path('feedback-RUD/<int:pk>/', views.FeedbackRUD.as_view()),
    path('admin/feedback-list/', views.FeedbackList.as_view()),
    path('admin/feedback-list/<int:pk>/', views.SelectedFeedback.as_view()),
]