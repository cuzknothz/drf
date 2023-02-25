# Generated by Django 4.1.7 on 2023-02-25 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_feed_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='feed',
            name='image',
        ),
        migrations.CreateModel(
            name='FeedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.feed')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.image')),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='images',
            field=models.ManyToManyField(through='feed.FeedImage', to='feed.image'),
        ),
    ]
