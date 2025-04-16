from django.test import TestCase
from django.urls import reverse
from .models import User

class UserListViewTest(TestCase):
    
    #seta usuários (cria) para testar
    def setUp(self): 
        User.objects.create(user_nickname='pedrolc', user_name='Pedro Lucas')
        User.objects.create(user_nickname='cst_lara', user_name='Lara Costa')
    
    def test_user_list_view(self):
        #self.client = cliente de testes do django
        # .get = método do request simulado
        # reverse = chama a view que mapeei lá nas urls
        response = self.client.get(reverse('user_list_view'))
        self.assertEqual(response.status_code, 200) # verifica código HTTP da resposta
        self.assertTemplateUsed(response, 'api_rest/users/user_list.html') # verifica so template utilizado
        
        #verifica se os usuários criados foram adicionados
        self.assertContains(response, 'Pedro Lucas')
        self.assertContains(response, 'Lara Costa')
        
        
class UserCreateViewTest(TestCase):
    
    def test_user_create_view(self):
        
        # simula requisição para a view 
        response = self.client.get(reverse('user_create_view'))
        #verifica status HTTP da resposta 
        self.assertEqual(response.status_code, 200)
        #verifica template utilizado
        self.assertTemplateUsed(response, 'api_rest/users/user_form.html')
        
        # cria um objeto pra ser enviado na simulação
        data = {
             'user_nickname': 'novousuario',
             'user_name': 'Novo Usuário',
             'user_email': 'novo@email.com',
             'user_age': 25
        }
        
        # testa o POST pra view
        response = self.client.post(reverse('user_create_view'), data)
        #redireciona pra outra view
        self.assertRedirects(response, reverse('user_list_view'))
        
        self.assertEqual(User.objects.count(), 1)