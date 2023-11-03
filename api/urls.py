from django.urls import path
from .views import *

urlpatterns=[
     path('webinars/', WebinarViewList.as_view(), name='webinar-list'),
     path('webinars/<int:pk>/', WebinarDetails.as_view(), name='webinar-detail'),

     path('feedback_second_page/', FeedBack2List.as_view(), name='feedback2-list'),
     path('feedback_second_page/<int:pk>/', FeedBack2Details.as_view(), name='feedback2-details'),

     path('feedback_first_page/', Feedback1List.as_view(), name='feedback1-list'),
     path('feedback_first_page/<int:pk>/', Feedback1Details.as_view(), name='feedback1-details'),

]