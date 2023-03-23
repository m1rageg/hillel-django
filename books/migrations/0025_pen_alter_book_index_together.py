# Generated by Django 4.1.6 on 2023-03-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0024_alter_book_pages_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('count_sold', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterIndexTogether(
            name='book',
            index_together={('country', 'name')},
        ),
    ]
