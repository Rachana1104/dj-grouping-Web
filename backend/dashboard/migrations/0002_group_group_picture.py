# Generated by Django 4.0.3 on 2022-04-02 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_picture',
            field=models.ImageField(default=2, upload_to='images/'),
            preserve_default=False,
        ),
    ]
