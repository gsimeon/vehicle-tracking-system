# Generated by Django 4.0.2 on 2022-03-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CikisZamanlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarihSaat', models.DateTimeField(verbose_name='Tarih ve Saat')),
                ('kullaniciAdi', models.CharField(max_length=50, verbose_name='Kullanıcı Adı')),
            ],
        ),
    ]
