# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Event.position'
        db.delete_column('news_event', 'position')

        # Deleting field 'Event.is_main'
        db.delete_column('news_event', 'is_main')

        # Changing field 'Event.date'
        db.alter_column('news_event', 'date', self.gf('django.db.models.fields.DateField')(default=datetime.date(2011, 12, 16)))


    def backwards(self, orm):
        
        # Adding field 'Event.position'
        db.add_column('news_event', 'position', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Event.is_main'
        db.add_column('news_event', 'is_main', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Changing field 'Event.date'
        db.alter_column('news_event', 'date', self.gf('django.db.models.fields.DateField')(null=True))


    models = {
        'news.event': {
            'Meta': {'ordering': "('date',)", 'object_name': 'Event'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {}),
            'short_description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_description_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'news.news': {
            'Meta': {'ordering': "('position',)", 'object_name': 'News'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_main': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'main_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'short_description': ('django.db.models.fields.TextField', [], {}),
            'short_description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_description_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'news.newsimage': {
            'Meta': {'ordering': "('position',)", 'object_name': 'NewsImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'news': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['news.News']"}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['news']
