# Generated by Django 4.1.7 on 2023-05-03 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_remove_messages_f_user_remove_messages_t_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='Updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Task_Updator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='todo',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Task_Creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
