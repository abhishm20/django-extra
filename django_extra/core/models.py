# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import time

from django.db import models

# pylint: disable=no-member


class _DateTimeStampingModel(models.Model):
    created_at = models.CharField(max_length=32, null=True, default=None)
    updated_at = models.CharField(max_length=32, null=True, default=None)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = int(time.time())
        self.updated_at = int(time.time())
        super().save(*args, **kwargs)


class AbstractModel(_DateTimeStampingModel):
    id = models.CharField(editable=False, unique=True, primary_key=True, max_length=50)

    class Meta:
        abstract = True
