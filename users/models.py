from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField



# === Custom Manager ===
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'utilisateur doit avoir une adresse email")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Le superutilisateur doit avoir is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Le superutilisateur doit avoir is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


# === Custom User Model ===
class User(AbstractUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('user', 'Client'),
        ('admin', 'Admin'),
    ]

    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Le numéro doit être au format '+999999999'. Jusqu'à 15 chiffres autorisés."
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150)
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[phone_validator],
        verbose_name="Téléphone",
        unique=True,
    )
    avatar = CloudinaryField('image', blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']

    objects = UserManager()

    def __str__(self):
        return f"{self.email} ({self.role})"
