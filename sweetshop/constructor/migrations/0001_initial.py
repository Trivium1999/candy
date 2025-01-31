# Generated by Django 4.2.8 on 2024-04-22 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BentoFilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название начинки')),
                ('description', models.TextField(verbose_name='Описание начинки')),
                ('image', models.ImageField(null=True, upload_to='image/filling/bento/')),
            ],
            options={
                'verbose_name': 'Начинка для бенто-торта',
                'verbose_name_plural': 'Начинки для бенто-тортов',
            },
        ),
        migrations.CreateModel(
            name='CakeDecoration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тип оформления')),
                ('description', models.TextField(verbose_name='Описание оформления')),
                ('price', models.IntegerField(verbose_name='Наценка')),
            ],
            options={
                'verbose_name': 'Оформление тортов',
                'verbose_name_plural': 'Оформление тортов',
            },
        ),
        migrations.CreateModel(
            name='CakeFilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название начинки')),
                ('description', models.TextField(verbose_name='Описание начинки')),
                ('price', models.IntegerField(verbose_name='Наценка')),
                ('image', models.ImageField(null=True, upload_to='image/filling/cake/')),
            ],
            options={
                'verbose_name': 'Начинка для торта',
                'verbose_name_plural': 'Начинки для тортов',
            },
        ),
        migrations.CreateModel(
            name='CupcakeDecoration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тип оформления')),
                ('description', models.TextField(verbose_name='Описание оформления')),
                ('price', models.IntegerField(verbose_name='Наценка')),
            ],
            options={
                'verbose_name': 'Оформление капкейков',
                'verbose_name_plural': 'Оформление капкейков',
            },
        ),
        migrations.CreateModel(
            name='CupcakeFilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название начинки')),
                ('description', models.TextField(verbose_name='Описание начинки')),
            ],
            options={
                'verbose_name': 'Начинка для капкейков',
                'verbose_name_plural': 'Начинки для капкейков',
            },
        ),
        migrations.CreateModel(
            name='OtherDessert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, verbose_name='На какое число хотите заказать?')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('name', models.CharField(max_length=100, verbose_name='Тип десерта')),
            ],
            options={
                'verbose_name': 'Десерт',
                'verbose_name_plural': 'Разные Десерты',
            },
        ),
        migrations.CreateModel(
            name='Cupcake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, verbose_name='На какое число хотите заказать?')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('decoration', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='constructor.cupcakedecoration', verbose_name='Оформление')),
                ('filling', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='constructor.cupcakefilling', verbose_name='Начинка')),
            ],
            options={
                'verbose_name': 'Капкейки',
                'verbose_name_plural': 'Капкейки',
            },
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, verbose_name='На какое число хотите заказать?')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('decoration', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='constructor.cakedecoration', verbose_name='Оформление')),
                ('filling', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='constructor.cakefilling', verbose_name='Начинка')),
            ],
            options={
                'verbose_name': 'Торт',
                'verbose_name_plural': 'Торты',
            },
        ),
        migrations.CreateModel(
            name='BentoCake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, verbose_name='На какое число хотите заказать?')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('filling', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='constructor.bentofilling', verbose_name='Начинка')),
            ],
            options={
                'verbose_name': 'Бенто-торт',
                'verbose_name_plural': 'Бенто-торты',
            },
        ),
    ]
