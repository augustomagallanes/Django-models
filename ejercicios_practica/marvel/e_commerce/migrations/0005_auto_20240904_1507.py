# Generated by Django 3.2.2 on 2024-09-04 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e_commerce', '0004_whishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('favorite', models.BooleanField(default=True, verbose_name='favorite')),
                ('cart', models.BooleanField(default=True, verbose_name='cart')),
                ('wished_qty', models.PositiveIntegerField(default=0, verbose_name='wished qty')),
                ('bought_qty', models.PositiveIntegerField(default=0, verbose_name='bought qty')),
                ('comic', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.comic', verbose_name='Comic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='WhishList',
        ),
    ]
