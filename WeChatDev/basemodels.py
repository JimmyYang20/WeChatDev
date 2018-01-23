# -*- coding: utf-8 -*-
from django.db import models
class BaseModel(models.Model):
    class Meta:
        abstract = True

    def toDict(self):
        _dict = {}
        desired_format = '%Y-%m-%d %H:%M'
        for f in self._meta._get_fields():
            if isinstance(f, models.ForeignKey):
                pass
            elif isinstance(f, models.DateTimeField):
                _dict[f.name] = getattr(self, f.name).strftime(desired_format)
            elif isinstance(f, models.Field):
                _dict[f.name] = getattr(self, f.name)
        return _dict

    def __str__(self):
        tmp = ''
        for k, v in self.toDict().iteritems():
            tmp = tmp + '{}:{},'.format(k, v)
        return tmp[0:len(tmp) - 1]
