# -----------------------------
# Views de fromt (HTML)
# -----------------------------

from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def user_list_view(request):
    users = User.objects.all()
    return render(request, 'api_rest/users/user_list.html', {'users': users}) 

def user_create_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST) # Instanciando um objeto da clase UserForm com so dados do request 
        if form.is_valid():
            form.save()
            return redirect('user_list_view')
    else: 
        form = UserForm() 

    return render(request, 'api_rest/users/user_form.html', {'form': form})

def user_edit_view(request, nickname):
    user = User.objects.get(user_nickname=nickname)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list_view')
    else:
            form = UserForm(instance=user)
    
    return render(request, 'api_rest/users/user_form.html', {'form': form, 'edit': True})

def user_delete_view(request, nickname):
    user = User.objects.get(user_nickname=nickname)

    if request.method == 'POST':
        user.delete()
        return redirect('user_list_view')
    
    return render(request, 'api_rest/users/user_confirm_delete.html',  {'user': user})
    