# Generated by Django 3.2.5 on 2021-10-28 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ryosai_2021', '0003_remove_pro_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pro',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
