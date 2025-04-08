from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

# funções de GET

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()  # all() retorna todos os objetos do meu model User
        serializer = UserSerializer(users, many=True)  # serializando
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)

# view GET que faz o request via URL Parameter
@api_view(['GET'])
def get_by_nick(request, nick):
    try:
        # busca user pelo nickname passado pelo endpoint no path user\<str:nickname>\
        user = User.objects.get(user_nickname=nick)  
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)  # serializa o user encontrado
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):
    try:
        if request.GET.get('user'):  # se existir parâmetro 'user' na URL

            
            user_nickname = request.GET['user']  # pega o valor do parâmetro
            try:
                user = User.objects.get(pk=user_nickname)  # busca por pk = user_nickname
            except: 
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = UserSerializer(user)  # serializa o user
            return Response(serializer.data)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# função de POST
@api_view(['POST'])
def new_user(request):
    if request.method == 'POST':
        new_user = request.data
        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# função de PUT

@api_view(['PUT'])
def edit_user(request):
    if request.method == 'PUT':

        nickname = request.data['user_nickname']
        updated_user = User.objects.get(pk=nickname)

        print(request.data)

        serializer = UserSerializer(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


    return Response(status=status.HTTP_400_BAD_REQUEST)

# função de delete

@api_view(['DELETE'])
def delete_user(request):
    if request.method == 'DELETE': # verifica o método da request
        try: 
            user_nickname = request.data['user_nickname'] # pegando o user_nickname do request
            user = User.objects.get(user_nickname=user_nickname) #pegando  o objeto correspondente aquele user_nickname
            user.delete() # deletando esse objeto
            return Response(status=status.HTTP_204_NO_CONTENT) # caso bem sucedido

        except User.DoesNotExist: # caso mal sucedido
            return Response(status=status.HTTP_404_NOT_FOUND)
            
    return Response(status=status.HTTP_400_BAD_REQUEST)
