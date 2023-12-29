# Generated by Django 4.2.8 on 2023-12-29 17:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("MainPage", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderItem",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orderItem",
                        to="MainPage.products",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderSuccess",
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
                (
                    "order_number",
                    models.CharField(blank=True, max_length=225, null=True),
                ),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                (
                    "number",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^\\+?1?\\d{8,15}$"
                            )
                        ],
                    ),
                ),
                ("address", models.CharField(max_length=225)),
                ("reference_point", models.CharField(max_length=225)),
                ("comments", models.CharField(max_length=225)),
                (
                    "order_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_item",
                        to="Order.orderitem",
                    ),
                ),
            ],
        ),
    ]
