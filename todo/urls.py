from django.urls import path
from .views import todo_list, todo_create, todo_update, todo_delete, management_view, toggle_completion

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('create/', todo_create, name='todo_create'),
    path('update/<int:todo_id>/', todo_update, name='todo_update'),
    path('delete/<int:todo_id>/', todo_delete, name='todo_delete'),
    path('management/', management_view, name='management_view'),
    path('toggle-completion/<int:todo_id>/', toggle_completion, name='toggle_completion'),
]