# Generated by Django 2.0 on 2018-01-17 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojomanager', '0004_auto_20180117_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='responsavel',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsavel', to='dojomanager.Pessoa'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='slug_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
