# Generated by Django 5.0.1 on 2024-01-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_postcommentrating_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcommentrating',
            name='rating',
            field=models.CharField(choices=[('1.0', '⭐'), ('2.0', '⭐⭐'), ('3.0', '⭐⭐⭐'), ('4.0', '⭐⭐⭐⭐'), ('5.0', '⭐⭐⭐⭐⭐')], max_length=10),
        ),
    ]
