from django.db import models
from AuthorLoginApp.models import User
from django.utils import timezone

class NewsArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'articles')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='NewsApp/', null= True, blank=True)
    views = models.IntegerField(default=0)
    topic = (
        ('politics', 'Politics'),
        ('sports', 'Sports'),
        ('entertainment', 'Entertainment'),
        ('finance', 'Finance'),
        ('international', 'International'),
        ('social', 'Social'),
        ('nature', 'Nature'),
        ('science', 'Science'),
        ('tech', 'Tech'),
        ('national', 'National'),
        ('life style', 'LifeStyle'),
        ('trending', 'Trending'),
    )
    category = models.CharField(max_length=20,choices=topic, default='world')
    position = (
        ('main','Main'),
        ('r2c1','Row 2 Column 1'),
        ('r2c2','Row 2 Column 2'),
        ('r2c3','Row 2 Column 3'),
        ('r3c1','Row 3 Column 1'),
        ('r3c2','Row 3 Column 2'),
        ('r3c3','Row 3 Column 3'),
        ('r4c1','Row 4 Column 1'),
        ('r4c2','Row 4 Column 2'),
        ('r4c3','Row 4 Column 3'),
        ('r4c4','Row 4 Column 4'),
        ('r5c1','Row 5 Column 1'),
        ('r5c2','Row 5 Column 2'),
        ('r5c3','Row 5 Column 3'),
        ('r5c4','Row 5 Column 4')
    )
    importance_level = models.CharField(max_length=20,choices=position, default='main')
    article_ad = models.ImageField(blank=True, null=True, upload_to='article_ad')
    company = models.TextField(blank=True, null=True)
    link_ad = models.URLField(blank=True, null=True)
    description_ad = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__ (self):
        return self.title
    

class Advertisement(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='advertisement')
    link = models.URLField(blank=True, null=True)
    clicks = models.IntegerField(default=0)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    validity = models.DateField(null=True, blank=True)

    class Meta:
        ordering =['-created']
