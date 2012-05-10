# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Feedback.content'
        db.alter_column('feedbacks_feedback', 'content', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Feedback.description'
        db.alter_column('feedbacks_feedback', 'description', self.gf('django.db.models.fields.TextField')(default='olo'))
    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Feedback.content'
        raise RuntimeError("Cannot reverse this migration. 'Feedback.content' and its values cannot be restored.")

        # Changing field 'Feedback.description'
        db.alter_column('feedbacks_feedback', 'description', self.gf('django.db.models.fields.TextField')(null=True))
    models = {
        'feedbacks.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['feedbacks']