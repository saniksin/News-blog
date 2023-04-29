from django.db import models
from apps.accounts.models import User

# Модель - это представление таблицы из бд в виде класса Python в Django
# makemigration - Создает файл для миграций
# migrate - Мигрирует миграцию в бд
# createsuperuser - создаем супер юзера

# Create your models here.

class Category(models.Model):
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField(max_length=150)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField("Фото", upload_to="posts/images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    #выставит время во время создания записи
    created_at = models.DateTimeField(auto_now_add=True)
    #выставит время во время повторного обновления данных
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField("Активный", default=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"