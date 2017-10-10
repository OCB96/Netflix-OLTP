# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0003_auto_20171010_0820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='access',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cast',
            name='id',
        ),
        migrations.RemoveField(
            model_name='content',
            name='id',
        ),
        migrations.RemoveField(
            model_name='director',
            name='id',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='plans',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='id',
        ),
        migrations.RemoveField(
            model_name='rentals',
            name='id',
        ),
        migrations.RemoveField(
            model_name='type',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user_rentals',
            name='id',
        ),
        migrations.RemoveField(
            model_name='zip',
            name='id',
        ),
        migrations.AddField(
            model_name='access',
            name='access_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='access',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.User'),
        ),
        migrations.AlterField(
            model_name='cast',
            name='cast_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='content',
            name='cast_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.Cast'),
        ),
        migrations.AlterField(
            model_name='content',
            name='content_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='content',
            name='director_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.Director'),
        ),
        migrations.AlterField(
            model_name='content',
            name='genre_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.Genre'),
        ),
        migrations.AlterField(
            model_name='content',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.Type'),
        ),
        migrations.AlterField(
            model_name='director',
            name='director_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.Plans'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.User'),
        ),
        migrations.AlterField(
            model_name='plans',
            name='plan_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plans',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.User'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='content_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.Content'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='ratings_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.User'),
        ),
        migrations.AlterField(
            model_name='rentals',
            name='content_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.Content'),
        ),
        migrations.AlterField(
            model_name='rentals',
            name='rental_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='type',
            name='type_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='zip_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.Zip'),
        ),
        migrations.AlterField(
            model_name='user_rentals',
            name='rental_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.Rentals'),
        ),
        migrations.AlterField(
            model_name='user_rentals',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.User'),
        ),
        migrations.AlterField(
            model_name='user_rentals',
            name='user_rental_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='zip',
            name='zip_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
