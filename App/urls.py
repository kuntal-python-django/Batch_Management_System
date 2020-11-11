from django.urls import path
from . import views


urlpatterns = [
    # path('/', ),
    path('', views.BatchList, name="batch-list"),
    path('completed/', views.CompletedBatchList, name="completed-batch-list"),
    path('student/<slug:slug>', views.StudentList, name="student-list"),
    path('notice/<slug:slug>', views.Notice, name="student-notice"),
    path('feedback/', views.Feedback, name="feedback"),
    path('submit-feedback/', views.SubmitFeedback, name="submit-feedback"),
    path('404/', views.NotFound, name="404"),
]