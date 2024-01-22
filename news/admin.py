from django.contrib import admin
from news.models import Category, Post, PostCommentRating
# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCommentRating)