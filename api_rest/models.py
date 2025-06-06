from django.db import models

# definindo campos do db
class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_nickname = models.CharField(max_length=100, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)

# pra printar a classe, retorna um String
    def __str__(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'
