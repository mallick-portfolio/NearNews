from django.db import models
from django.utils.text import slugify
from account.models import CustomUser

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=50, unique=True)
  slug =  models.SlugField(null=True, blank=True, unique=True)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name, allow_unicode=True)
    return super(Category, self).save(*args, **kwargs)


class Post(models.Model):
  title = models.TextField(blank=True, null=True)
  slug =  models.SlugField(null=True, blank=True, unique=True)
  description = models.TextField()
  rating = models.IntegerField(blank=True, null=True)
  author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='news')
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news_category')
  image_url = models.ImageField(upload_to="news/")

  created_at = models.DateTimeField(auto_now_add=True)
  published_at = models.DateTimeField(blank=True, null=True)


  def save(self, *args, **kwargs):
    self.slug = slugify(self.title, allow_unicode=True)
    return super(Post, self).save(*args, **kwargs)