from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="media/")
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    description = models.TextField(blank=True, max_length=100)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    interviews = 'لقاء العدد'
    arts = 'الفنون'
    films = 'فيلم شاهدته'
    books = 'كتاب قرأته'
    travel = 'رحلات وتجارب'

    CATEGORIES = [
        (interviews, 'Interviews'),
        (arts, 'Arts & Culture'),
        (films, 'Film Reviews'),
        (books, 'Book Reviews'),
        (travel, 'Travel & Experience'),
    ]

    category = models.CharField(
        max_length = 20,
        choices=CATEGORIES,
        default=interviews,
    )

    isCurrentFeature = models.BooleanField(default=False)
    isFeature1 = models.BooleanField(default=False)
    isFeature2 = models.BooleanField(default=False)
    isFeature3 = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title



