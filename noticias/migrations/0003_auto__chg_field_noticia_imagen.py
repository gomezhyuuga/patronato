# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Noticia.imagen'
        db.alter_column(u'noticias_noticia', 'imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'Noticia.imagen'
        db.alter_column(u'noticias_noticia', 'imagen', self.gf('django.db.models.fields.files.ImageField')(default='uploads/noimage.png', max_length=100))

    models = {
        u'noticias.noticia': {
            'Meta': {'object_name': 'Noticia'},
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

    complete_apps = ['noticias']