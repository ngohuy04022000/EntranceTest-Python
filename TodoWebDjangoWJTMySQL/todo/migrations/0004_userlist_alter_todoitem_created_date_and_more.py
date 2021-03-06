# Generated by Django 4.0.4 on 2022-04-28 09:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todoitem_created_date_alter_todoitem_due_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 28, 9, 20, 3, 375950, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 9, 20, 3, 375950, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='modification_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 28, 9, 20, 3, 375950, tzinfo=utc)),
        ),
    ]
