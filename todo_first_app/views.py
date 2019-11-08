from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo_first_app.models import Task

def index(request):

    task_obj_list = Task.objects.all()
    if request.method == "POST":
        todoId = request.POST.get('todo_id')

        if "taskAdd" in request.POST:
            title = request.POST["title"]
            date = str(request.POST["date"])
            description = str(request.POST['description'])
            content = title + " to be completed by " + date
            Todo = Task(title=title, content=content, description=description, due_date=date)
            Todo.save()                 #save new task
            return redirect("/")        #reload page

    return render(request, 'todo_first_app/index.html', context={'tasks_objects': task_obj_list})

def delete(request, list_id):
    todo = Task.objects.get(id=list_id)
    todo.delete()
    return redirect('/')

def cross(request, list_id):
    todo = Task.objects.get(id=list_id)
    todo.completed = True
    todo.save()
    return redirect('/')

def uncross(request, list_id):
    todo = Task.objects.get(id=list_id)
    todo.completed = False
    todo.save()
    return redirect('/')

def edit(request):
    print('insde edit')
    print (request.POST)
    todoId = request.POST["todoid"]
    print(todoId)
    todo = Task.objects.get(id=int(todoId))

    if (request.method == "POST") and ("taskUpdate" in request.POST):
        print("inside second if")
        todo.title = request.POST["title"]
        todo.date = str(request.POST["date"])
        todo.description = str(request.POST['description'])
        todo.content = todo.title + " to be completed by " + todo.date
        #Todo = Task(title=title, content=content, description=description, due_date=date)
        todo.save()
        return redirect("/")

    print("outside if")
    return render(request, 'todo_first_app/snippets/modal.html', context={'todo_edit': todo})




# def all_completed(tof= False, show_all=True):
#     task_obj_list = Task.objects.all()
#
#     if(show_all == True):
#         return task_obj_list
#     else:
#         list=[]
#         for obj in task_obj_list:
#             if obj.completed == tof:
#                 list.append(obj)
#         return list


def filtering(request, temp):
    temp_list = Task.objects.all()
    task_obj_list=[]
    print("inside filtering")
    if temp == '1':       #if completed is to be shown
        list=[]
        for obj in temp_list:
            if obj.completed == True:
                list.append(obj)
        task_obj_list = list
        print("if completed is to be shown")
        print(*task_obj_list, sep=', ')

    elif temp == '0':     #if pending is to be shown
        list=[]
        for obj in temp_list:
            if obj.completed == False:
                list.append(obj)
        task_obj_list = list
        print("if pending is to be shown")
        print(*task_obj_list, sep=', ')

    else:
        task_obj_list = temp_list
        print("if all is to be shown")
        print(*task_obj_list, sep=', ')

    return render(request, 'todo_first_app/index.html', context={'tasks_objects': task_obj_list})
