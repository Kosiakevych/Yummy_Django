from django.core.validators import RegexValidator
from django.db import models
import uuid


# Create your models here.


class Categories(models.Model):
    name = models.CharField(unique=True, max_length=15)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)


class Dishes(models.Model):

    def rename_image(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        next_file = f'{uuid.uuid4()}.{ext_file}'
        return next_file

    name = models.CharField(unique=True, max_length=25)
    discription = models.TextField(max_length=70)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)
    image = models.ImageField(upload_to=rename_image)
    slug = models.SlugField(max_length=200, db_index=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        ordering = ('position', 'price',)
        index_together = (('id', 'slug'),)


class About_Us(models.Model):
    header = models.TextField(unique=True, max_length=170)
    check_flag = models.TextField(max_length=170)
    check_flag2 = models.TextField(max_length=170)
    check_flag3 = models.TextField(max_length=170)
    finish = models.TextField(max_length=400)
    phone = models.CharField(unique=True, max_length=20)
    image = models.ImageField()
    youtube_video = models.CharField(max_length=1000)


class Stats(models.Model):
    name = models.CharField(unique=True, max_length=30)
    count = models.IntegerField()
    position = models.SmallIntegerField(unique=True)

    class Meta:
        ordering = ('position',)


class Why_us(models.Model):
    main_text = models.TextField(max_length=300)
    my_url = models.URLField()

    header1 = models.CharField(max_length=40)
    text1 = models.TextField(max_length=200)

    header2 = models.CharField(max_length=40)
    text2 = models.TextField(max_length=200)

    header3 = models.CharField(max_length=40)
    text3 = models.TextField(max_length=200)


class Home(models.Model):
    header = models.CharField(max_length=70)
    discription = models.TextField(max_length=150, blank=True)
    watch_video = models.URLField()
    image = models.ImageField()


class Testimonials(models.Model):
    name = models.CharField(max_length=30)
    job = models.CharField(max_length=30)
    comment = models.TextField(max_length=250)
    image = models.ImageField()
    is_visible = models.BooleanField(default=True)
    stars = models.SmallIntegerField(default=5)


class Event(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    discription = models.TextField(max_length=300)
    position = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True)
    image = models.ImageField()

    class Meta:
        ordering = ('position',)


class Chefs(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=30)
    image = models.ImageField()
    comment = models.TextField(max_length=500)
    position = models.PositiveIntegerField()

    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    class Meta:
        ordering = ('position',)


class Gallery(models.Model):
    image = models.ImageField()
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ('position',)


class UserReservation(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    persons = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=500, blank=True)
    admin_date = models.DateTimeField(auto_now_add=True)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    email = models.CharField(max_length=70)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-admin_date', '-is_processed',)

    def __str__(self):
        return f'{self.name}, {self.phone}, {self.persons}, {self.email}, {self.date}, {self.time}, {self.message}'


class Contact(models.Model):
    our_address = models.CharField(max_length=200)
    call_us = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    opening = models.CharField(max_length=70)


class UserContact(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=70)
    subject = models.CharField(max_length=70)
    message = models.TextField(max_length=600)
    admin_date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}, {self.email}, {self.subject}, {self.message}'

    class Meta:
        ordering = ('-admin_date', '-is_processed',)
