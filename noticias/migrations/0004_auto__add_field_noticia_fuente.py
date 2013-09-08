# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Noticia.fuente'
        db.add_column(u'noticias_noticia', 'fuente',
                      self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Noticia.fuente'
        db.delete_column(u'noticias_noticia', 'fuente')


    models = {
        u'noticias.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'extracto': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fuente': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'default': "'uplaods/noimage.png'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['noticias']