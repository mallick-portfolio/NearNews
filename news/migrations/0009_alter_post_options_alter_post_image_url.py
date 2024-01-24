# Generated by Django 5.0.1 on 2024-01-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_post_avg_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.ImageField(upload_to='news/media/upload/'),
        ),
    ]