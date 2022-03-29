from django.shortcuts import render

from kitovu.forms import post_form

# Create your views here.


def home(request):
    print('home')
    form = post_form(request.POST)
    if form.is_valid():
        form.save()
        form = post_form

    else:
        bad =form.errors
        context = {'bad':bad}

    context = {'form':form}

    return render(request, 'index.html', context)


def about ( request):

    return render(request, 'about ')