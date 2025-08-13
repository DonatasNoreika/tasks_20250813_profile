from django.urls import reverse_lazy
from django.views import generic
from .models import Task


class PostListView(generic.ListView):
    model = Task
    template_name = "tasks.html"
    context_object_name = "tasks"


class PostDetailView(generic.DetailView):
    model = Task
    template_name = "task.html"
    context_object_name = "task"


class PostCreateView(generic.CreateView):
    model = Task
    template_name = "task_form.html"
    fields = ['name', 'done']
    success_url = reverse_lazy('tasks')


class PostUpdateView(generic.UpdateView):
    model = Task
    template_name = "task_form.html"
    fields = ['name', 'done']
    success_url = reverse_lazy('tasks')


class PostDeleteView(generic.DeleteView):
    model = Task
    template_name = "task_delete.html"
    context_object_name = "task"
    success_url = reverse_lazy('tasks')