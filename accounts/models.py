from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, type, password=None):
        if not email:
            raise ValueError('User must have an Email address')
        
        if not username:
            raise ValueError('User must have an username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            type = type,
        )
        
        user.set_password(password)
        user.save(using=self.db)
        return user
# <<<<<<< HEAD
# =======
        
# >>>>>>> caf6102fd222ff60697431bf4ce4180c679b7ff9
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name= first_name,
            last_name= last_name,
# <<<<<<< HEAD
            type=type,
# =======
            # type = type,
# >>>>>>> caf6102fd222ff60697431bf4ce4180c679b7ff9
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using = self._db)
        return user
    
    
type_choices = [
    ('user','user'),
    ('business','business'),
]

class Account(AbstractBaseUser):
    type = models.CharField(max_length=20, choices=type_choices, default='user')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique = True)
    
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.email
# <<<<<<< HEAD
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
# =======
    def has_module_perms(self, add_label):
        return True
    def has_perm(self, perm, obj=None):
        return self.is_admin
# >>>>>>> caf6102fd222ff60697431bf4ce4180c679b7ff9