from django.shortcuts import render ,redirect
from django.http import HttpResponse
import random 	                # import the random module

def index(request):
    if not 'attempts' in request.session:
        request.session['attempts']=0
    if not 'target_number' in request.session:
        request.session['target_number']=random.randint(1, 100)
    if not 'num' in request.session:
        request.session['num']=0
        print(request.session['target_number'])
    return render(request,"index.html")

def play(request):
    if request.method == 'POST':
        request.session['attempts']+=1
        request.session['num'] =int(request.POST["num"])
    return render(request,'response.html')

def reset(request):
    request.session.clear()
    return redirect('/')