# Generated by Django 3.0.2 on 2020-01-06 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Under',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('url', models.SlugField(blank=True, null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Under', to='items.Category')),
            ],
            options={
                'verbose_name': 'under',
                'verbose_name_plural': 'under',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='under',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='items.Under'),
            preserve_default=False,
        ),
    ]
