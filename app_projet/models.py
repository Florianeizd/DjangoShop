from django.db import models
from django.urls import reverse

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    article_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    stock = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.article_name

from django import forms  

class ArticleForm(forms.ModelForm):  
    class Meta:  
        model = Article  
        fields = "__all__"  

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.article.article_name

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return str(self.id)