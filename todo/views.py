from django.shortcuts import render, redirect

# Create your views here.
from django import views
from django.urls import reverse_lazy
from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import JSONParser
from .models import Todo, AccountUser, Document
from .serializers import TodoSerializer, AccountUserSerializer
from .forms import DocumentForm, TodoForm
from django.http import JsonResponse, HttpResponse
from django.middleware.csrf import get_token

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class ListAccountUser(generics.ListAPIView):
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer

class DetailAccountUser(generics.RetrieveAPIView):
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer

def modelform_upload(request):
    print(request.POST, request.FILES)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print(request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'modelform_upload.html', {
        'form': form
    })

def todo_post(request):
    print(request)
    if request.method == 'POST':
        todo_data = JSONParser().parse(request)
        print(todo_data)
        todo_serializer = TodoSerializer(data=todo_data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse(":)))", safe=False)
        else:
            return JsonResponse(f':((((', safe=False)
    else:
        todo_serializer = TodoSerializer()
        return render(request, 'todoform.html', {
            'form': form
        })
    return HttpResponse(f'{request.method} :)', status=200)

def todoform_upload(request):
    print(request.POST)
    print(JSONParser().parse(request))
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(f':)', status=200)
        else:
            return HttpResponse(f':(', status=200)
    else:
        form = TodoForm()
        return render(request, 'todoform.html', {
            'form': form
        })
    return HttpResponse(f'{request.method} :)', status=200)

class DocumentListView(views.generic.ListView):
    model = Document
    template_name = 'list.html'

class DocumentCreateView(views.generic.CreateView):
    template_name = 'modelform_upload.html'
    model = Document
    form_class = DocumentForm
    success_url = reverse_lazy('home')

class TodoCreateView(views.generic.CreateView):
    template_name = 'todoform.html'
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo')

def CsrfView(request):
    return JsonResponse({'token': get_token(request)})

def PingView(request):
    return JsonResponse({'result': True})
# todo_create = DocumentCreateView.as_view()
