# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_details', '0002_remove_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_by',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
