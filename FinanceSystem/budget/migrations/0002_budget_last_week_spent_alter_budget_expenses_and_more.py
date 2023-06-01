# Generated by Django 4.2.1 on 2023-06-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='last_week_spent',
            field=models.FloatField(default=0, max_length=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='budget',
            name='expenses',
            field=models.ManyToManyField(related_name='budget', to='budget.expense'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='incomes',
            field=models.ManyToManyField(related_name='budget', to='budget.income'),
        ),
    ]
