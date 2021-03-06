from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False)
    
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False)
        
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    
        
    body = models.TextField(
        blank=True,
        null=False)
        
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE)
        
    tags = models.ManyToManyField(
        Tag,
        blank=True)

    def __str__(self):
        return self.title
    
    


class Pro(models.Model):
   
    

   name = models.CharField(
        max_length=50,
        blank=False,
        null=True)
   
   body = models.CharField(
        max_length=150,
        blank=False,
        null=True)
    
   place = models.CharField(
        max_length=50,
        blank=False,
        null=True)
   
   image = models.CharField(
        max_length=50,
        blank=False,
        null=True)
   
   
   def __str__(self):
        return str(self.name)