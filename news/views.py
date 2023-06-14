from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from news.form import Add_news, LoginForm, SignupForm, update_news
from news.models import newsData
from django.views.generic import ListView


# def newslist(request):
#     newsdata=newsData.objects.all()
#     paginator = Paginator(newsdata, 5)  # Display 5 items per page
#     page_number = request.GET.get('page')  # Get the current page number from the request
#     newsdata = paginator.get_page(page_number)
#     return render(request,'newslist.html',{'newsdata':newsdata})

class newsListview(ListView):
    model = newsData
    template_name = 'newslist.html'
    context_object_name = 'newsdata'
    paginate_by = 5
    

def signup_user(request):
    if request.method=='POST':
        signupform=SignupForm(request.POST)
        if signupform.is_valid():
            username=signupform.cleaned_data["username"]
            name=signupform.cleaned_data["name"]
            email=signupform.cleaned_data["emailid"]
            password=signupform.cleaned_data["password"]
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username Already exists pick a new one')
            return redirect('signup')
        else:
            user=User.objects.create_user(username=username,
                                          first_name=name,
                                          email=email,
                                          password=password)
            user.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        signupform=SignupForm()
        return render(request,'signup.html',{'signupform':signupform})
        
        
def login_user(request):
    if request.method=='POST':
        loginform=LoginForm(request.POST)
        if loginform.is_valid():
            username=loginform.cleaned_data["username"]
            password=loginform.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
        if User.objects.filter(username=username).exists():
            if user is not None:
                login(request,user)
                return redirect('newslist')

            else:
                messages.error(request,'Incorrect Password')
                return redirect('login')
        else:
            messages.error(request,'Incorrect Username')
            return redirect('login')
    else:
        loginform=LoginForm()
        return render(request,'login.html',{'loginform':loginform})

def logout_user(request):
    logout(request)
    return redirect('newslist')

    
login_required(login_url='login')   
def addnews(request):
    if request.method == 'POST':
        addform = Add_news(request.POST, request.FILES)
        if addform.is_valid():
            title = addform.cleaned_data['title']
            content = addform.cleaned_data['content']
            image = addform.cleaned_data['image']
            video = addform.cleaned_data['video']
            user_id = request.user
            
            news_data = newsData(title=title, content=content, image=image, video=video, user_id=user_id)
            news_data.save()
            
            return HttpResponseRedirect(reverse('newslist'))
        else:
            messages.error(request, 'Enter valid news')
            return HttpResponseRedirect(reverse('addnews'))
    else:
        addform = Add_news()
        return render(request, 'addnews.html', {'addform': addform})
    
login_required(login_url='login')           
def updatenews(request, uid):
    data = get_object_or_404(newsData, id=uid)
    updateform = update_news(instance=data)
    if request.method == 'POST':
        updateform = update_news(request.POST,request.FILES,instance=data)
        if updateform.is_valid():
            updateform.save()
            return HttpResponseRedirect(reverse('newslist'))
        else:
            return HttpResponseRedirect(reverse('editnews'))
    else:
        return render(request, 'editnews.html', {'updateform': updateform})
# @login_required
def detailnews(request,uid):
    user_id = request.user.id
    print('user_id is', user_id)
    data = newsData.objects.get(id=uid)
    return render(request,'detailnews.html',{'detail':data,"user_id":user_id})

login_required(login_url='login')   
def deletenews(request,uid):
    data = newsData.objects.get(id=uid)
    data.delete()
    return redirect('newslist')


@login_required(login_url='login')
def user_added_(request):
    user_id = request.user.id
    newsdata=newsData.objects.all()
    return render(request,'mynews.html',{'newsdata':newsdata,"user_id":user_id})


    
        
            
        
            
            
