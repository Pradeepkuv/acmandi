# Generated by Django 4.1.7 on 2023-03-29 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
                ('origin_country', models.CharField(max_length=50)),
                ('manufacture_country', models.CharField(max_length=50)),
                ('support_contact', models.CharField(max_length=50)),
                ('support_email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MarketPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='')),
                ('website', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.brand')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductHighlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('highlight', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('1', 'TITLE_TAG'), ('2', 'FEATURE')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpecificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('label', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=100)),
                ('specification_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.specificationtype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductToSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.product')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.specification')),
            ],
        ),
        migrations.CreateModel(
            name='ProductToProductHighlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.producthighlight')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('is_thumbnail', models.BooleanField()),
                ('media_file', models.FileField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('link', models.CharField(max_length=100)),
                ('mrp', models.FloatField()),
                ('discount', models.FloatField()),
                ('sales_price', models.FloatField()),
                ('marketplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.marketplace')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PerHourEnergyConsumed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_consumed', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.product')),
            ],
        ),
    ]
