
from django.urls import path
#rom footprints.todolist_app.views import contactUs, todolist
from todolist_app import views


urlpatterns = [
    path('todo/',views.todolist , name= 'todolist'),
    path('todo/delete/<task_id>',views.delete_task  , name= 'delete_task'),
    path('todo/update/<task_id>', views.update_task , name='update_task'),

] 