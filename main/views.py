from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from main.models import Todo
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'main/index.html', {
        "todo_items": todo_items
    })


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    todo_items = Todo.objects.all()
    print(todo_items)
    task_list = []
    for i in todo_items:
        task_list.append(i.text)
    content = request.POST["content"]
    if content not in task_list:
        created_obj = Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect("/main/")


@csrf_exempt
def delete_todo(request, todo_id):
    content = Todo.objects.get(id=todo_id)
    content.delete()
    return HttpResponseRedirect("/main/")
