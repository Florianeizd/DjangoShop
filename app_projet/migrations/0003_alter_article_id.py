# Generated by Django 4.1.4 on 2022-12-17 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projet', '0002_article_delete_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
