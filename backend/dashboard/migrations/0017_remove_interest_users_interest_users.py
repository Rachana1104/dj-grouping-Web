# Generated by Django 4.0.3 on 2022-05-04 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_remove_interest_category_alter_interest_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest',
            name='users',
        ),
        migrations.AddField(
            model_name='interest',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.userprofile'),
        ),
    ]