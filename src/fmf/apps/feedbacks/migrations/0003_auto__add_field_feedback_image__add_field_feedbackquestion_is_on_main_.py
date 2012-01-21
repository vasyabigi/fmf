# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Feedback.image'
        db.add_column('feedbacks_feedback', 'image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'FeedbackQuestion.is_on_main'
        db.add_column('feedbacks_feedbackquestion', 'is_on_main', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Adding field 'FeedbackQuestion.position'
        db.add_column('feedbacks_feedbackquestion', 'position', self.gf('django.db.models.fields.IntegerField')(default=-1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Feedback.image'
        db.delete_column('feedbacks_feedback', 'image')

        # Deleting field 'FeedbackQuestion.is_on_main'
        db.delete_column('feedbacks_feedbackquestion', 'is_on_main')

        # Deleting field 'FeedbackQuestion.position'
        db.delete_column('feedbacks_feedbackquestion', 'position')


    models = {
        'feedbacks.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'feedbacks.feedbackquestion': {
            'Meta': {'object_name': 'FeedbackQuestion'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'answer_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'answer_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'feedback': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['feedbacks.Feedback']"}),
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
