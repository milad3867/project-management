# Generated by Django 2.2.5 on 2019-12-26 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webSite', '0007_auto_20191227_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='webSite.Semester'),
        ),
    ]
