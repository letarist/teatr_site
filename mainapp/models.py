from django.db import models


# from django.contrib import
class Genre(models.Model):
    title = models.CharField(max_length=30, verbose_name="Жанр")
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Artist(models.Model):
    MALE = "ML"
    FEMALE = "FM"
    GENDER = [(MALE, "male"), (FEMALE, "female")]
    name = models.CharField(max_length=30, verbose_name="Имя артиста")
    middle_name = models.CharField(max_length=30, verbose_name="Отчество")
    surname = models.CharField(max_length=50, verbose_name="Фамилия артиста")
    age = models.SmallIntegerField(verbose_name="возраст")
    gender = models.CharField(verbose_name="Гендер", choices=GENDER, default=MALE, max_length=2)
    profession = models.CharField(verbose_name="Профессия", max_length=40)
    bio = models.TextField(blank=True, null=True, verbose_name="биография")
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True, verbose_name="Аватар")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"


class Repertoire(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название произведения", unique=True)
    genre = models.ManyToManyField(Genre, verbose_name="Жанр")
    year = models.SmallIntegerField(verbose_name="Год постановки")
    description = models.TextField(verbose_name="Описание")
    artist = models.ManyToManyField(Artist, verbose_name="Артист", related_name="repertoire")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Репертуар"
        verbose_name_plural = "Репертуар"


class Contact(models.Model):
    phone = models.IntegerField(verbose_name='Номер телефона', null=True, blank=True)
    email = models.EmailField(verbose_name='почта')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


