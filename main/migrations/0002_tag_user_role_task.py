# Generated by Django 4.2 on 2023-05-28 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("developer", "Developer"), ("manager", "Manager"), ("admin", "Admin")],
                default="developer",
                max_length=255,
            ),
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("date_finish", models.DateTimeField(null=True)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("new task", "New"),
                            ("in development", "In Development"),
                            ("in qa", "In Qa"),
                            ("in code review", "In Code Review"),
                            ("ready for release", "Ready For Release"),
                            ("released", "Released"),
                            ("archived", "Archived"),
                        ],
                        default="new task",
                        max_length=255,
                    ),
                ),
                (
                    "priority",
                    models.IntegerField(choices=[(0, "Low"), (1, "Medium"), (2, "High"), (3, "Critical")], default=0),
                ),
                ("tags", models.ManyToManyField(related_name="tasks", to="main.tag")),
                (
                    "task_creator",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_tasks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "task_performer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="assigned_tasks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
