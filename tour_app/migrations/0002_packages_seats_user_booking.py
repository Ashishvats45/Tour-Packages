# Generated by Django 4.2.6 on 2023-11-10 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tour_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="packages",
            name="seats",
            field=models.CharField(
                default=0,
                max_length=100,
                verbose_name=[
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30,
                    31,
                    32,
                    33,
                    34,
                    35,
                    36,
                    37,
                    38,
                    39,
                    40,
                    41,
                    42,
                    43,
                    44,
                    45,
                    46,
                    47,
                    48,
                    49,
                ],
            ),
        ),
        migrations.CreateModel(
            name="user_booking",
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
                ("name", models.CharField(max_length=50)),
                (
                    "type",
                    models.CharField(
                        choices=[("Adults", "Adults"), ("child", "child")],
                        max_length=50,
                    ),
                ),
                ("Adult_price", models.IntegerField(default=0)),
                ("child_price", models.IntegerField(default=0)),
                ("confirm", models.BooleanField(default=False)),
                (
                    "package_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="tour_app.packages",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
