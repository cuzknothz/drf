# Generated by Django 4.1.7 on 2023-02-25 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0011_rename_image_image_src_rename_video_video_src'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.feed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='save',
            field=models.ManyToManyField(related_name='feed_save', through='feed.FeedSave', to=settings.AUTH_USER_MODEL),
        ),
    ]
