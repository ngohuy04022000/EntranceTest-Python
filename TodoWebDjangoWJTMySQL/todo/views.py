from django.urls import reverse, reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import ToDoItem, ToDoList, UserList
from django.contrib.auth.models import User

from .signform import RegistrationForm
from django.http import HttpResponseRedirect 
from django.shortcuts import render

def Register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})

# ToDoItem: id, task, description, user_id, modification_date, status, created_date, due_date, todo_list

class ListUserView(ListView):
    model = User
    template_name = "todo/index_user.html"

class ListListView(ListView):
    model = ToDoList
    template_name = "todo/index.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["task"] = "Add a new list"
        return context

class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "id",
        "task",
        "description",
        "status",
        "created_date",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["task"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "id",
        "task",
        "description",
        "modification_date",
        "status",
        "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["task"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ListDelete(DeleteView):
    model = ToDoList
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("index")

class ItemDelete(DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context