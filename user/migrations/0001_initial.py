# Generated by Django 4.0.4 on 2022-05-13 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('bio', models.CharField(default='', max_length=999)),
                ('profile_image', models.CharField(default='https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png', max_length=9999)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
