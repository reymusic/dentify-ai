# Generated by Django 5.1.1 on 2024-10-19 13:38

import accounts.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_image', models.ImageField(default='uploads/default.jpg', upload_to='original_images/')),
                ('cropped_image', models.ImageField(blank=True, null=True, upload_to='cropped_images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('pred_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='home_prediction_pk')),
                ('message', models.TextField(blank=True, max_length=300)),
                ('xray_file', models.FileField(storage=accounts.models.SupabaseStorage(), upload_to='')),
                ('pred_ts', models.DateTimeField(auto_now=True)),
                ('result', models.CharField(max_length=30)),
                ('confidence', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Prediction',
                'db_table': 'Predictions',
            },
        ),
    ]
