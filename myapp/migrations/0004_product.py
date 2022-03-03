# Generated by Django 4.0.2 on 2022-02-21 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('Nike', 'Nike'), ('Fasttrack', 'Fasttrack'), ('G Shock', 'G Shock'), ('Puma', 'Puma'), ('Hublot', 'Hublot'), ('Alleny Solly', 'Alleny Solly'), ('Raymond', 'Raymond')], max_length=100)),
                ('product_model', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('product_desc', models.TextField()),
                ('product_image', models.ImageField(upload_to='product_image/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
