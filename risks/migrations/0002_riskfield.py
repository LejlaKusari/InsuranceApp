# Generated by Django 2.1.3 on 2018-11-12 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('field_type', models.CharField(choices=[('text', 'Text'), ('number', 'Number'), ('date', 'Date'), ('enum', 'Enum')], max_length=16)),
                ('is_required', models.BooleanField(default=True)),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='risks.RiskType')),
            ],
        ),
    ]
