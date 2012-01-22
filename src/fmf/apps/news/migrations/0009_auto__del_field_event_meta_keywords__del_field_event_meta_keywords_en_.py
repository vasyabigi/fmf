# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Event.meta_keywords'
        db.delete_column('news_event', 'meta_keywords')

        # Deleting field 'Event.meta_keywords_en'
        db.delete_column('news_event', 'meta_keywords_en')

        # Deleting field 'Event.meta_keywords_uk'
        db.delete_column('news_event', 'meta_keywords_uk')

        # Deleting field 'Event.meta_description'
        db.delete_column('news_event', 'meta_description')

        # Deleting field 'Event.meta_description_en'
        db.delete_column('news_event', 'meta_description_en')

        # Deleting field 'Event.meta_description_uk'
        db.delete_column('news_event', 'meta_description_uk')

        # Deleting field 'News.meta_keywords'
        db.delete_column('news_news', 'meta_keywords')

        # Deleting field 'News.meta_keywords_en'
        db.delete_column('news_news', 'meta_keywords_en')

        # Deleting field 'News.meta_keywords_uk'
        db.delete_column('news_news', 'meta_keywords_uk')

        # Deleting field 'News.meta_description'
        db.delete_column('news_news', 'meta_description')

        # Deleting field 'News.meta_description_en'
        db.delete_column('news_news', 'meta_description_en')

        # Deleting field 'News.meta_description_uk'
        db.delete_column('news_news', 'meta_description_uk')


    def backwards(self, orm):
        
        # Adding field 'Event.meta_keywords'
        db.add_column('news_event', 'meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'Event.meta_keywords_en'
        db.add_column('news_event', 'meta_keywords_en', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'Event.meta_keywords_uk'
        db.add_column('news_event', 'meta_keywords_uk', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'Event.meta_description'
        db.add_column('news_event', 'meta_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Event.meta_description_en'
        db.add_column('news_event', 'meta_description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Event.meta_description_uk'
        db.add_column('news_event', 'meta_description_uk', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'News.meta_keywords'
        db.add_column('news_news', 'meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'News.meta_keywords_en'
        db.add_column('news_news', 'meta_keywords_en', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'News.meta_keywords_uk'
        db.add_column('news_news', 'meta_keywords_uk', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'News.meta_description'
        db.add_column('news_news', 'meta_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'News.meta_description_en'
        db.add_column('news_news', 'meta_description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'News.meta_description_uk'
        db.add_column('news_news', 'meta_description_uk', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    models = {
        'news.event': {
            'Meta': {'ordering': "('-date_to',)", 'object_name': 'Event'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_from': ('django.db.models.fields.DateField', [], {}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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
