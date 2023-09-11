from django.contrib import admin
from django.urls import path,include

from todoapp import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<pk>/',views.Taskdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),


    # path('detail',views.details,name='details')
]
