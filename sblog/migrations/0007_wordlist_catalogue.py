# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sblog', '0006_remove_wordlist_catalogue'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordlist',
            name='catalogue',
            field=models.ForeignKey(default=2, to='sblog.Catalogue'),
        ),
    ]
