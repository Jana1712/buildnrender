# Generated by Django 5.2.3 on 2025-06-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0007_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generalsetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='image_favicon')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='image_logo')),
                ('companyname', models.CharField(default='', max_length=100)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=200)),
                ('url_x', models.CharField(default='', max_length=100)),
                ('url_facebook', models.CharField(default='', max_length=100)),
                ('url_instagram', models.CharField(default='', max_length=100)),
                ('url_linkedin', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
