# Generated by Django 2.2.12 on 2023-01-02 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=100)),
                ('comment', models.TextField(default='Enter Comment Here', max_length=300)),
                ('chore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Chore')),
            ],
        ),
    ]
