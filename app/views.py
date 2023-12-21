from django.shortcuts import render, redirect
from .models import InsertData
from django.contrib import messages

def Register(request):
    request.session.clear()
    if request.POST:
        firstname = request.POST['firstname']
    
        if firstname:
            request.session['firstname'] = firstname
            return redirect('second')
        else:
            pass
    return render(request, 'register.html')


def Register2(request):
    if 'firstname' not in request.session or request.session['firstname'] is None:
        return redirect('404')  

    # firstname = request.session['firstname']

    if request.method == 'POST':
        secondname = request.POST.get('secondname', '')

        if secondname:
            request.session['secondname'] = secondname
            return redirect('last')  
        else:
            return redirect('second')  

    return render(request, 'register2.html')
 
    

def Submits(request):
    firstname=request.session['firstname']
    secondname=request.session['secondname']
    if firstname and secondname is None:
        return redirect('')
    if request.POST:
        thirdname = request.POST['thirdname']
        if thirdname:
            saveData=InsertData(firstname=firstname,secondname=secondname,thirdname=thirdname)
            saveData.save()
            request.session.clear()
            messages.success(request, 'data submitted successfully!')

        else:
            print('something occured')
    else:
        return redirect('')
    return render(request, 'submits.html')
  
def NotFound(request):
    return render(request,'404.html')