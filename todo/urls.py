from django.urls import path, include
from .views import ListTodo, DetailTodo, ListAccountUser, DetailAccountUser, modelform_upload, DocumentListView, DocumentCreateView, TodoCreateView, todoform_upload
from .views import CsrfView, PingView, todo_post

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view(), name="todo"),
    path('account/<int:pk>/', DetailAccountUser.as_view()),
    path('account/', ListAccountUser.as_view()),
    path('hoge/', DocumentListView.as_view(), name="home"),
    # path('hoge/upload/', DocumentCreateView.as_view()),
    path('hoge/upload/', modelform_upload),
    # path('hoge/todo/', TodoCreateView.as_view()),
    path('hoge/todo/', todo_post),
    path('csrf/', CsrfView),
]
