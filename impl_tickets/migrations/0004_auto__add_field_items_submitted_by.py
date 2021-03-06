# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Items.submitted_by'
        db.add_column('impl_tickets_items', 'submitted_by',
                      self.gf('django.db.models.fields.TextField')(default='User', max_length=2000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Items.submitted_by'
        db.delete_column('impl_tickets_items', 'submitted_by')


    models = {
        'impl_tickets.items': {
            'Meta': {'object_name': 'Items'},
            'date_fix_confirmed': ('django.db.models.fields.DateTimeField', [], {'null': "'true'"}),
            'date_fixed': ('django.db.models.fields.DateTimeField', [], {'null': "'true'"}),
            'date_found': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'responsible': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': "'true'"}),
            'status_customer': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'status_solvo': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'submitted_by': ('django.db.models.fields.TextField', [], {'max_length': '2000'})
        },
        'impl_tickets.itemstatus': {
            'Meta': {'object_name': 'ItemStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['impl_tickets']