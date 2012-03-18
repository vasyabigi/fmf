# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SectionImage'
        db.create_table('sections_sectionimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['sections.Section'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('title_uk', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal('sections', ['SectionImage'])


    def backwards(self, orm):
        
        # Deleting model 'SectionImage'
        db.delete_table('sections_sectionimage')


    models = {
        'sections.article': {
            'Meta': {'ordering': "('position',)", 'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'articles'", 'null': 'True', 'to': "orm['sections.Section']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'sections.articleimage': {
            'Meta': {'ordering': "('position',)", 'object_name': 'ArticleImage'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['sections.Article']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'sections.section': {
            'Meta': {'ordering': "('position',)", 'object_name': 'Section'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'sections.sectionimage': {
            'Meta': {'ordering': "('position',)", 'object_name': 'SectionImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['sections.Section']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sections']
