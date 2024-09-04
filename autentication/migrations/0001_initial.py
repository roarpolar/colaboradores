# Generated by Django 5.1.1 on 2024-09-04 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colaborador', models.CharField(max_length=30)),
                ('matricola', models.CharField(max_length=30)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='icones')),
            ],
        ),
    ]
