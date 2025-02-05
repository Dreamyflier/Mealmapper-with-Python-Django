# Generated by Django 4.2.10 on 2024-02-19 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('photo', models.ImageField(upload_to='images')),
                ('price', models.FloatField(default=0)),
                ('description', models.CharField(default='Description about Component', max_length=255)),
            ],
            options={
                'db_table': 'Pc',
            },
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='pet',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='pet',
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=9999999999, max_length=11),
        ),
        migrations.DeleteModel(
            name='Pet',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='component',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mmapp.pc'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='component',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mmapp.pc'),
        ),
    ]
