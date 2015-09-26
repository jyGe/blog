# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sblog', '0004_auto_20150926_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordlist',
            name='word_list_caption',
            field=models.CharField(max_length=50),
        ),
    ]
