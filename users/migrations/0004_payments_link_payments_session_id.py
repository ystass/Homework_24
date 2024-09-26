# Generated by Django 5.1.1 on 2024-09-26 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_payments"),
    ]

    operations = [
        migrations.AddField(
            model_name="payments",
            name="link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=260, null=True, verbose_name="ID сессии"
            ),
        ),
    ]
