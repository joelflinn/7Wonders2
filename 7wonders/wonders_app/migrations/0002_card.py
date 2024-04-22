# Generated by Django 4.2 on 2024-04-22 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wonders_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('add_to_board', models.BooleanField(default=False)),
                ('pointValue', models.PositiveBigIntegerField(default=0)),
                ('board', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wonders_app.board')),
            ],
        ),
    ]
