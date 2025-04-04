# Generated by Django 5.1.3 on 2024-12-13 13:15

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administracao", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Gerente",
        ),
        migrations.DeleteModel(
            name="Vendedor",
        ),
        migrations.CreateModel(
            name="Gerente",
            fields=[
                (
                    "users_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Gerente",
                "verbose_name_plural": "Gerentes",
            },
            bases=("administracao.users",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Vendedor",
            fields=[
                (
                    "users_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Vendedor",
                "verbose_name_plural": "Vendedores",
            },
            bases=("administracao.users",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
