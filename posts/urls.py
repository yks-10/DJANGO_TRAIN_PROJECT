from django.urls import path 
from .views import * #UserList, UserDetail, PostList, PostDetail

urlpatterns = [
	#path('user/', UserList.as_view()),
	#path('users/<int:pk>/', UserDetail.as_view()),
	path('<int:pk>/', PostDetail.as_view()),
	path('train/', TrainList.as_view()),
	path('book/', TicketBooking.as_view()),
]