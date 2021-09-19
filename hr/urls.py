from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('empreg/', views.registration,name='empreg'),
    path('pendingreq/',views.pendingLeaveRequest, name='pendingreq'),
    path('approveleave/<int:pk>', views.approveLeave, name='approveleave'),
    path('viewleave', views.viewLeave, name='viewleave')
    
]
