# Generated by Django 4.0.6 on 2023-04-27 05:10

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
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('not sure', 'not sure')], max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('nationality', models.CharField(choices=[('Nigeria', 'Nigeria'), ('Ghana', 'Ghana'), ('United Kingdom', 'UK'), ('USA', 'USA')], max_length=20, null=True)),
                ('state', models.CharField(choices=[('Abia', 'Abia'), ('Abuja', 'Abuja'), ('Niger', 'Niger'), ('Kano', 'Kano'), ('Lagos', 'Lagos'), ('Osun', 'Osun'), ('Oyo', 'Oyo')], max_length=20, null=True)),
                ('means_of_identity', models.ImageField(null=True, upload_to='identityImage/')),
                ('particulars', models.FileField(null=True, upload_to='particulars/')),
                ('profile_passport', models.ImageField(null=True, upload_to='staffImage/')),
                ('position', models.CharField(choices=[('CEO', 'CEO'), ('GMD', 'GMD'), ('CTO', 'CTO'), ('Supervisor', 'Supervisor'), ('Accountant', 'Accountant'), ('Marketer', 'Marketer'), ('Staff', 'Staff'), ('HR', 'HR')], max_length=20, null=True)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorce', 'Divorce'), ('Complicate', 'Complicate')], max_length=20, null=True)),
                ('staff', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
