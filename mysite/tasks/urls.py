from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView)

urlpatterns = [
    path("tasks/", PostListView.as_view(), name="tasks"),
    path("tasks/<int:pk>", PostDetailView.as_view(), name="task"),
    path("tasks/create", PostCreateView.as_view(), name="task_create"),
    path("tasks/<int:pk>/update", PostUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/delete", PostDeleteView.as_view(), name="task_delete"),
]
