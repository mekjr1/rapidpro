# Generated by Django 1.11.2 on 2017-08-01 11:13

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("contacts", "0060_auto_20170512_2001")]

    operations = [
        migrations.AddField(model_name="contactfield", name="uuid", field=models.UUIDField(null=True)),
        migrations.AlterField(
            model_name="contactfield", name="uuid", field=models.UUIDField(default=uuid.uuid4, null=True)
        ),
    ]
