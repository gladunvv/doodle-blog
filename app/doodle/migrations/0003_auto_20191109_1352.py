# Generated by Django 2.2.6 on 2019-11-09 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0002_auto_20191107_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='posts_coments', to='doodle.Post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='tags_posts', to='doodle.Post'),
        ),
    ]
