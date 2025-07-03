from django.urls import path
from . import views

urlpatterns = [   
    path('',views.index,name="index"),
    path('store_data/',views.store_data,name="store_data"),
    path('<int:task_id>/completed/',views.completed,name="completed"),
    path('<int:delete_id>/delete_task/',views.delete_task,name="delete_task"),
    path('<int:task_id>/completed/task_id/edit_task/',views.edit_task,name="edit_task"),
    path('<int:task_id>/update/',views.update,name="update"),
]