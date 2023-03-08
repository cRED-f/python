from django.shortcuts import render
from appTwo.models import User
# Create your views here.
def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    user_list=User.objects.order_by('first_name')
    user_dic={"users":user_list}
    return render(request,'appTwo/user.html',context=user_dic)
