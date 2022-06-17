# Generated by Django 4.0.3 on 2022-06-15 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_alter_group_group_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroupRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join', models.BooleanField(default=False)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.userprofile')),
            ],
        ),
    ]