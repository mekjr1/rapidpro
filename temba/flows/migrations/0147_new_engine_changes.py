# Generated by Django 1.11.2 on 2017-06-28 18:17

from django.db import migrations, models

import temba.utils.models


class Migration(migrations.Migration):

    dependencies = [("flows", "0146_auto_20180202_1228")]

    operations = [
        migrations.AddField(
            model_name="flowsession", name="output", field=temba.utils.models.JSONAsTextField(null=True, default=dict)
        ),
        migrations.AddField(
            model_name="flowsession",
            name="responded",
            field=models.BooleanField(default=False, help_text="Whether the contact has responded in this session"),
        ),
        migrations.AddField(
            model_name="flowsession",
            name="status",
            field=models.CharField(
                choices=[
                    ("W", "Waiting"),
                    ("C", "Completed"),
                    ("I", "Interrupted"),
                    ("X", "Expired"),
                    ("F", "Failed"),
                ],
                help_text="The status of this session",
                max_length=1,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="actionlog",
            name="created_on",
            field=models.DateTimeField(help_text="When this log event occurred"),
        ),
        migrations.AddField(
            model_name="flow",
            name="flow_server_enabled",
            field=models.BooleanField(default=False, help_text="Run this flow using the flow server"),
        ),
    ]