from django.db import models
from django.utils.text import slugify
from account.models import CustomUser

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=50, unique=True)
  slug =  models.SlugField(null=True, blank=True, unique=True, max_length=50)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name, allow_unicode=True)
    return super(Category, self).save(*args, **kwargs)\

  def __str__(self) -> str:
    return self.name


class Post(models.Model):
  title = models.CharField(max_length=250,blank=True, null=True)
  slug =  models.SlugField(null=True, blank=True, unique=True,max_length=250)
  description = models.TextField()
  author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='news')
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news_category')
  image_url = models.ImageField(upload_to="news/")
  avg_rating = models.FloatField(blank=True, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
  published_at = models.DateTimeField(blank=True, null=True)

  class Meta:
    ordering = ['-created_at']


  def save(self, *args, **kwargs):
    self.slug = slugify(self.title, allow_unicode=True)
    return super(Post, self).save(*args, **kwargs)

class PostCommentRating(models.Model):

  STAR_CHOICES = [
    ('1.0', '⭐'),
    ('2.0', '⭐⭐'),
    ('3.0', '⭐⭐⭐'),
    ('4.0', '⭐⭐⭐⭐'),
    ('5.0', '⭐⭐⭐⭐⭐'),
]
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  body = models.TextField()
  rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
  created = models.DateTimeField(auto_now_add = True)