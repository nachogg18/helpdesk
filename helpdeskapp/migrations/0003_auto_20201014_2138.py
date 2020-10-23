# Generated by Django 2.2.16 on 2020-10-15 00:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('helpdeskapp', '0002_question_question_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='message',
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.CharField(default=django.utils.timezone.now, max_length=72),
            preserve_default=False,
        ),
    ]
