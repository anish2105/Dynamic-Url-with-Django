from django.shortcuts import render,redirect
from .models import dict
from .forms import dictform
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = dictform(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = dict.objects.all().order_by('letter')
            return render(request,'index.html',{'all_items':all_items})
    else:
        all_items = dict.objects.all().order_by('letter')
        return render(request,'index.html',{'all_items':all_items})


def posts(request,pk_id):
    post = dict.objects.get(letter = pk_id)
    return render(request,'posts.html',{'post':post})
