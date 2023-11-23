# Generated by Django 4.1 on 2023-10-21 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("skripsi", "0008_delete_fasilitas_delete_jarak_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Favorite",
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
                ("waktu_pemilihan", models.DateTimeField(auto_now_add=True)),
                (
                    "coffee_shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="skripsi.coffeeshop",
                    ),
                ),
            ],
        ),
    ]
