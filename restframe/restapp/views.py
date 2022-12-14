from django.shortcuts import render
from .serializer import TaskSerilaizer,UserSerilizer
from .models import Task
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

# Create your views here.


class CreateUserview(CreateAPIView):
    model=get_user_model()
    permission_classes=(AllowAny,)
    serializer_class=UserSerilizer

class Taskviewset(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Task.objects.all().order_by('-date')
    serializer_class=TaskSerilaizer
    
class Dueviewset(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('-date').filter(status=False)
    serializer_class=TaskSerilaizer
    
class Completed(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('-date').filter(status=True)
    serializer_class=TaskSerilaizer    
    
    
    
    
    
    
    
    
    
        
    
