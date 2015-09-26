# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sblog', '0005_auto_20150926_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wordlist',
            name='catalogue',
        ),
    ]
