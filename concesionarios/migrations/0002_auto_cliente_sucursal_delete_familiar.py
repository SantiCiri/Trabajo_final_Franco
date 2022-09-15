# Generated by Django 4.1 on 2022-08-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("concesionarios", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="auto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("marca", models.CharField(max_length=50)),
                ("patente", models.CharField(max_length=50)),
                ("modelo", models.IntegerField()),
                ("fecha_ing", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                ("dni", models.IntegerField()),
                ("fecha_compra", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="sucursal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("provincia", models.CharField(max_length=50)),
                ("localidad", models.CharField(max_length=50)),
                ("empleados", models.IntegerField()),
                ("fecha_inaugural", models.DateField()),
            ],
        ),
        migrations.DeleteModel(name="familiar",),
    ]
