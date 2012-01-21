# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Feedback.name_uk'
        db.add_column('feedbacks_feedback', 'name_uk', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Feedback.name_en'
        db.add_column('feedbacks_feedback', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FeedbackQuestion.answer_uk'
        db.add_column('feedbacks_feedbackquestion', 'answer_uk', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FeedbackQuestion.answer_en'
        db.add_column('feedbacks_feedbackquestion', 'answer_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Feedback.name_uk'
        db.delete_column('feedbacks_feedback', 'name_uk')

        # Deleting field 'Feedback.name_en'
        db.delete_column('feedbacks_feedback', 'name_en')

        # Deleting field 'FeedbackQuestion.answer_uk'
        db.delete_column('feedbacks_feedbackquestion', 'answer_uk')

        # Deleting field 'FeedbackQuestion.answer_en'
        db.delete_column('feedbacks_feedbackquestion', 'answer_en')


    models = {
        'feedbacks.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
