from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, phonenumber, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)

        user = self.model(
            phonenumber=phonenumber,
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phonenumber, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phonenumber, username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phonenumber = models.CharField(max_length=15, unique=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=30, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phonenumber', 'email']

    objects = CustomUserManager()

 #{
#"phonenumber": "9090909000",
#"username":"admin1",
#"full_name": "asdf" ,

#"email": "admin11@gmail.com",
#"password": "admin@000"

#}


#{
#"username":"admin1",
#"password": "admin@000"
#}

#"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTg2OTc1MywiaWF0IjoxNjg5NzgzMzUzLCJqdGkiOiJlODZhYmQyNjJmYzQ0ZDM3OWVjNzJiOWZiY2E2YzYzNyIsInVzZXJfaWQiOjJ9.9FMM80A918aj-_1Y7YmrjklOa5PoQwFc_4O8m-Y3xtY",
  #  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5Nzg0MjUzLCJpYXQiOjE2ODk3ODMzNTMsImp0aSI6ImYzNjM1MGI2ZDA5YzQ1NDM4MWI5ODBmOTljNDM3MWFkIiwidXNlcl9pZCI6Mn0.Qgfuh9xGuqUhxDspkd110fEWJuG-969YH8zeE_5dvXg"

  #{
   # "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTg3MDE2OCwiaWF0IjoxNjg5NzgzNzY4LCJqdGkiOiJjOGRhOWJmYWM2N2M0ZmM4OGNmYTE0YmVlNDc0ZWI5OCIsInVzZXJfaWQiOjN9.QkTtMg1AcUEgJmDDst42Rg1bBQNaoPiXT5_oO2u5GD0",
   # "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5Nzg0NjY4LCJpYXQiOjE2ODk3ODM3NjgsImp0aSI6IjUyZDM3ZDlkNDQwNjQyN2M4NDQ1MjMwNTYwZjY0ZDA0IiwidXNlcl9pZCI6M30.8BQMM9JlfLAHVCMHSiA4AbEnfNjePdM0e4QDcYTuByg"
#}

# git init
#git status
#git add -A
#git status
#git commit -m "newauth"
#that github command
#git push origin master