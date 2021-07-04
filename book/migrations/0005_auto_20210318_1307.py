# Generated by Django 3.1.7 on 2021-03-18 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20210318_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rent',
            old_name='bookId',
            new_name='book',
        ),
        migrations.RemoveField(
            model_name='rent',
            name='rentId',
        ),
        migrations.AddField(
            model_name='rent',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.user'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
