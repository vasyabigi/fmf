# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Feedback.description_uk'
        db.add_column('feedbacks_feedback', 'description_uk', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Feedback.description_en'
        db.add_column('feedbacks_feedback', 'description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Feedback.description_uk'
        db.delete_column('feedbacks_feedback', 'description_uk')

        # Deleting field 'Feedback.description_en'
        db.delete_column('feedbacks_feedback', 'description_en')


    models = {
        'feedbacks.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'feedbacks.feedbackquestion': {
            'Meta': {'unique_together': "(('feedback', 'question'),)", 'object_name': 'FeedbackQuestion'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'answer_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'answer_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'feedback': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': "orm['feedbacks.Feedback']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_on_main': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['feedbacks.Question']"})
        },
        'feedbacks.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'question_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'question_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['feedbacks']
