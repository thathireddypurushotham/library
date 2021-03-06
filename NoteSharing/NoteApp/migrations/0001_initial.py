# Generated by Django 3.0 on 2021-04-30 07:14

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
            name='Books_Avail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_name', models.CharField(max_length=120, unique=True)),
                ('Book_author', models.CharField(default='', max_length=120)),
                ('Book_count', models.IntegerField(default=0)),
                ('Book_Updatedcount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=120)),
                ('p_email', models.EmailField(max_length=120)),
                ('p_complaint', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='st_admin_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rg_No', models.CharField(max_length=120)),
                ('Branch', models.CharField(max_length=120)),
                ('Name', models.CharField(max_length=120)),
                ('issue_status', models.IntegerField(default=0)),
                ('Book_name', models.CharField(max_length=120)),
                ('Book_author', models.CharField(max_length=120)),
                ('Book_count', models.IntegerField(default=0)),
                ('Issue_date', models.DateField(null=True)),
                ('Expire_date', models.DateField(null=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=10)),
                ('impf', models.ImageField(default='profile.jpg', upload_to='profiles/')),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=20)),
                ('uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
