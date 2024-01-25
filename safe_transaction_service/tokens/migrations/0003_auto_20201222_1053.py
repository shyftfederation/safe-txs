# Generated by Django 3.1.4 on 2020-12-22 10:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tokens", "0002_auto_20200903_1045"),
    ]

    operations = [
        migrations.AddField(
            model_name="token",
            name="events_bugged",
            field=models.BooleanField(default=False),
        ),
        migrations.AddIndex(
            model_name="token",
            index=models.Index(
                condition=models.Q(trusted=True),
                fields=["trusted"],
                name="token_trusted_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="token",
            index=models.Index(
                condition=models.Q(events_bugged=True),
                fields=["events_bugged"],
                name="token_events_bugged_idx",
            ),
        ),
    ]
