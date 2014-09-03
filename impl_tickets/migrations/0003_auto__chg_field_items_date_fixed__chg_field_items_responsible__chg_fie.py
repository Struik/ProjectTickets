# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Items.date_fixed'
        db.alter_column('impl_tickets_items', 'date_fixed', self.gf('django.db.models.fields.DateTimeField')(null='true'))

        # Changing field 'Items.responsible'
        db.alter_column('impl_tickets_items', 'responsible', self.gf('django.db.models.fields.TextField')(null='true', max_length=2000))

        # Changing field 'Items.date_fix_confirmed'
        db.alter_column('impl_tickets_items', 'date_fix_confirmed', self.gf('django.db.models.fields.DateTimeField')(null='true'))

    def backwards(self, orm):

        # Changing field 'Items.date_fixed'
        db.alter_column('impl_tickets_items', 'date_fixed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 8, 21, 0, 0)))

        # Changing field 'Items.responsible'
        db.alter_column('impl_tickets_items', 'responsible', self.gf('django.db.models.fields.TextField')(default='', max_length=2000))

        # Changing field 'Items.date_fix_confirmed'
        db.alter_column('impl_tickets_items', 'date_fix_confirmed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 8, 21, 0, 0)))

    models = {
        'impl_tickets.items': {
            'Meta': {'object_name': 'Items'},
            'date_fix_confirmed': ('django.db.models.fields.DateTimeField', [], {'null': "'true'"}),
            'date_fixed': ('django.db.models.fields.DateTimeField', [], {'null': "'true'"}),
            'date_found': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'responsible': ('django.db.models.fields.TextField', [], {'null': "'true'", 'max_length': '2000'}),
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