# Generated by Django 5.1.3 on 2025-03-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administracao", "0004_clientes_alter_gerente_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="clientes",
            name="email",
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
