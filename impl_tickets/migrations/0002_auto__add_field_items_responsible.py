# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Items.responsible'
        db.add_column('impl_tickets_items', 'responsible',
                      self.gf('django.db.models.fields.TextField')(blank='true', default='', max_length=2000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Items.responsible'
        db.delete_column('impl_tickets_items', 'responsible')


    models = {
        'impl_tickets.items': {
            'Meta': {'object_name': 'Items'},
            'date_fix_confirmed': ('django.db.models.fields.DateTimeField', [], {'blank': "'true'"}),
            'date_fixed': ('django.db.models.fields.DateTimeField', [], {'blank': "'true'"}),
            'date_found': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'responsible': ('django.db.models.fields.TextField', [], {'blank': "'true'", 'max_length': '2000'}),
            'status_customer': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'status_solvo': ('django.db.models.fields.TextField', [], {'max_length': '2000'})
        },
        'impl_tickets.itemstatus': {
            'Meta': {'object_name': 'ItemStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['impl_tickets']