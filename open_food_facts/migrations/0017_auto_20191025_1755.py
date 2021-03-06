# Generated by Django 2.2 on 2019-10-25 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('open_food_facts', '0016_auto_20191018_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='substitute',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='open_food_facts.Product'),
        ),
        migrations.AlterField(
            model_name='substitute',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
