from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.status import ( HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND)
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from rest_framework.authtoken.models import Token

from news.form import Add_news, LoginForm, SignupForm, update_news
from news.models import newsData
from newsapi.serializers import  Newsserializer

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def loginapi(request):
    login_form = LoginForm(request.data)
    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response({"error": "Please provide login credentials"}, status=HTTP_400_BAD_REQUEST)
        if not user:
            return Response({"error": "Invalid Credentials"}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)
    return Response({"error": "Invalid form data"}, status=HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def signupapi(request):
    signupform=SignupForm(request.data)
    if signupform.is_valid():
        username=signupform.cleaned_data['username']
        first_name=signupform.cleaned_data['name']
        email=signupform.cleaned_data['emailid']
        password=signupform.cleaned_data['password']
        if User.objects.filter(username=username).exists():
            return Response({"error":"username already exist"})
        else:
            user=User.objects.create_user(username=username,
                                          first_name=first_name,
                                          email=email,
                                          password=password)
            user.save()
            context={'signupform':signupform.data,'success':'Created User'}
            return Response(context,status=HTTP_200_OK)
    else:
        context={'signupform':signupform.data,'error':signupform.errors}
        return Response(context,status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
@permission_classes((AllowAny,))    
def list_news(request):
    search=request.query_params.get('q','')
    if search:
        news_data = newsData.objects.filter(title__istartswith=search)
        if not news_data:
            return Response({'message': 'No matches found'},status=HTTP_404_NOT_FOUND)
    else:
            news_data=newsData.objects.all()
    serializer=Newsserializer(news_data,many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def add_news(request):
    if request.method=='POST':
        addnewsform=Add_news(request.POST, request.FILES)
        if addnewsform.is_valid():
            title = addnewsform.cleaned_data['title']
            content = addnewsform.cleaned_data['content']
            image = addnewsform.cleaned_data['image']
            video = addnewsform.cleaned_data['video']
            user_id = request.user
            
            news_data = newsData(title=title, content=content, image=image, video=video, user_id=user_id)
            news_data.save()
            serializer=Newsserializer(news_data)
            context={'serializer':serializer.data,'success':'News added'}
            return Response(context)
        else:
            return Response({'error':'invalid data'},status=HTTP_400_BAD_REQUEST)
    else:
        return Response({'error':'invalid post'},status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def edit_news(request,uid):
    data = get_object_or_404(newsData, id=uid)
    updateform = update_news(instance=data)
    updateform = update_news(request.POST,request.FILES,instance=data)
    if updateform.is_valid():
        updateform.save()
        return Response(updateform.data,status=HTTP_200_OK)
    else:
        return Response({'error':'invalid data'},status=HTTP_400_BAD_REQUEST)
    
@csrf_exempt
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_news(request,uid):
    data = get_object_or_404(newsData, id=uid)
    data.delete()
    return Response({"success":"Data deleted"},status=HTTP_200_OK)


    





            
            
            
                




    
    