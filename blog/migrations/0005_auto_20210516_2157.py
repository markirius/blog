# Generated by Django 3.2.3 on 2021-05-16 21:57

from django.db import migrations
import django.db.models.manager
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('actived', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]