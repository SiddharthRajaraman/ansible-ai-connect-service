# Generated by Django 4.2.7 on 2023-11-21 00:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_alter_user_rh_user_is_org_admin"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="external_username",
            field=models.CharField(default=""),
        ),
    ]
