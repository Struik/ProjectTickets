# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemStatus'
        db.create_table('impl_tickets_itemstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('impl_tickets', ['ItemStatus'])

        # Adding model 'Items'
        db.create_table('impl_tickets_items', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('status_customer', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('status_solvo', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('date_found', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_fixed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_fix_confirmed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('impl_tickets', ['Items'])


    def backwards(self, orm):
        # Deleting model 'ItemStatus'
        db.delete_table('impl_tickets_itemstatus')

        # Deleting model 'Items'
        db.delete_table('impl_tickets_items')


    models = {
        'impl_tickets.items': {
            'Meta': {'object_name': 'Items'},
            'date_fix_confirmed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_fixed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_found': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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