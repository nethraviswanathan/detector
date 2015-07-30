# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('lightsite', '0009_auto_20150703_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinvite',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='companyinvite',
            name='html',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='companylogo',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
