from django.urls import path
from app import views

urlpatterns = [
    path('', views.StoreView.as_view(), name='store'),
    path('store/<int:pk>', views.StaffView.as_view(), name='staff'),
    path('calender/<int:pk>', views.CalendarView.as_view(), name='calender'),
    path('calender/<int:pk>/<int:year>/<int:month>/<int:day>', views.CalendarView.as_view(), name='calendar')
    ]