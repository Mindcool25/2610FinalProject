# Generated by Django 4.2.4 on 2023-12-13 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_post_userpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='parent',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.userpost'),
        ),
    ]
