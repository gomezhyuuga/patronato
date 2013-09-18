# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Convocatoria'
        db.create_table(u'convocatorias_convocatoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('extracto', self.gf('django.db.models.fields.TextField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(default='uplaods/noimage.png', max_length=100, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'convocatorias', ['Convocatoria'])


    def backwards(self, orm):
        # Deleting model 'Convocatoria'
        db.delete_table(u'convocatorias_convocatoria')


    models = {
        u'convocatorias.convocatoria': {
            'Meta': {'object_name': 'Convocatoria'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'extracto': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'default': "'uplaods/noimage.png'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['convocatorias']