# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Question'
        db.create_table('feedbacks_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('question_uk', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('question_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('feedbacks', ['Question'])

        # Adding model 'Feedback'
        db.create_table('feedbacks_feedback', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('feedbacks', ['Feedback'])

        # Adding model 'FeedbackQuestion'
        db.create_table('feedbacks_feedbackquestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feedback', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedbacks.Feedback'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedbacks.Question'])),
            ('answer', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('feedbacks', ['FeedbackQuestion'])


    def backwards(self, orm):
        
        # Deleting model 'Question'
        db.delete_table('feedbacks_question')

        # Deleting model 'Feedback'
        db.delete_table('feedbacks_feedback')

        # Deleting model 'FeedbackQuestion'
        db.delete_table('feedbacks_feedbackquestion')


    models = {
        'feedbacks.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'feedbacks.feedbackquestion': {
            'Meta': {'object_name': 'FeedbackQuestion'},
            'answer': ('django.db.models.fields.TextField', [], {}),
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
