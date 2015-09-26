# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sblog', '0003_auto_20150926_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordlist',
            name='catalogue',
            field=models.ForeignKey(default=1, to='sblog.Catalogue'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wordlist',
            name='word_list_caption',
            field=models.CharField(max_length=60),
        ),
    ]
