from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=228,null=True)
    def __str__(self):
        return self.title

class Animal(models.Model):
    name = models.CharField(max_length=228,null=True)
    price = models.FloatField()
    description = models.TextField()
    digital = models.BooleanField(default=True,null=True,blank=False)
    image = models.ImageField(null=True,blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image1 = models.ImageField(upload_to='about_us_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='about_us_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Donation(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    credit_card_number = models.CharField(max_length=16)

class VolunteerApplication(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    reasons_for_volunteering = models.TextField()
    skills = models.TextField()