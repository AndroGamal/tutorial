from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin , BaseUserManager

class User(BaseUserManager):
    def create_user(self,mail,name,password):
        if not mail:
            raise ValueError("mail is empty")
        mail=self.normalize_email(mail)
        user=self.model(mail=mail,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,mail,name,password):
        superuser=self.create_user("androgamal21@gmail.com","Andro","admin")
        superuser.is_superuser=True
        superuser.is_staff=True
        superuser.save(using=self._db)
        return superuser

class DataBase(AbstractBaseUser,PermissionsMixin):
    id=models.Index
    mail=models.EmailField(max_length=288,unique=True)
    name=models.CharField(max_length=288)
    password=models.TextField(editable=True)
    is_staff=models.BooleanField(default=False)
    objects = User()
    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = ["name"]


# Create your models here.
