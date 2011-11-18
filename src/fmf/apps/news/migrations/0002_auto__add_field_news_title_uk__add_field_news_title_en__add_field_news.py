# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'News.title_uk'
        db.add_column('news_news', 'title_uk', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True), keep_default=False)

        # Adding field 'News.title_en'
        db.add_column('news_news', 'title_en', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True), keep_default=False)

        # Adding field 'News.short_description_uk'
        db.add_column('news_news', 'short_description_uk', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'News.short_description_en'
        db.add_column('news_news', 'short_description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'News.description_uk'
        db.add_column('news_news', 'description_uk', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'News.description_en'
        db.add_column('news_news', 'description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'NewsImage.title_uk'
        db.add_column('news_newsimage', 'title_uk', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True), keep_default=False)

        # Adding field 'NewsImage.title_en'
        db.add_column('news_newsimage', 'title_en', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'News.title_uk'
        db.delete_column('news_news', 'title_uk')

        # Deleting field 'News.title_en'
        db.delete_column('news_news', 'title_en')

        # Deleting field 'News.short_description_uk'
        db.delete_column('news_news', 'short_description_uk')

        # Deleting field 'News.short_description_en'
        db.delete_column('news_news', 'short_description_en')

        # Deleting field 'News.description_uk'
        db.delete_column('news_news', 'description_uk')

        # Deleting field 'News.description_en'
        db.delete_column('news_news', 'description_en')

        # Deleting field 'NewsImage.title_uk'
        db.delete_column('news_newsimage', 'title_uk')

        # Deleting field 'NewsImage.title_en'
        db.delete_column('news_newsimage', 'title_en')


    models = {
        'news.news': {
            'Meta': {'ordering': "('created',)", 'object_name': 'News'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_main': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'main_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'short_description': ('django.db.models.fields.TextField', [], {}),
            'short_description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_description_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'news.newsimage': {
            'Meta': {'ordering': "('title', 'news')", 'object_name': 'NewsImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'news': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['news.News']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['news']
