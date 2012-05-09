# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'FeedbackQuestion', fields ['feedback', 'question']
        db.delete_unique('feedbacks_feedbackquestion', ['feedback_id', 'question_id'])

        # Deleting model 'FeedbackQuestion'
        db.delete_table('feedbacks_feedbackquestion')

        # Deleting field 'Question.question_en'
        db.delete_column('feedbacks_question', 'question_en')

        # Deleting field 'Question.question_uk'
        db.delete_column('feedbacks_question', 'question_uk')

        # Adding field 'Feedback.short_description'
        db.add_column('feedbacks_feedback', 'short_description',
                      self.gf('django.db.models.fields.TextField')(default='test'),
                      keep_default=False)

        # Adding field 'Feedback.content'
        db.add_column('feedbacks_feedback', 'content',
                      self.gf('django.db.models.fields.TextField')(default='test'),
                      keep_default=False)

    def backwards(self, orm):
        # Adding model 'FeedbackQuestion'
        db.create_table('feedbacks_feedbackquestion', (
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedbacks.Question'])),
            ('feedback', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', to=orm['feedbacks.Feedback'])),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('answer_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_on_main', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('answer_uk', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('feedbacks', ['FeedbackQuestion'])

        # Adding unique constraint on 'FeedbackQuestion', fields ['feedback', 'question']
        db.create_unique('feedbacks_feedbackquestion', ['feedback_id', 'question_id'])

        # Adding field 'Question.question_en'
        db.add_column('feedbacks_question', 'question_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Question.question_uk'
        db.add_column('feedbacks_question', 'question_uk',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Feedback.short_description'
        db.delete_column('feedbacks_feedback', 'short_description')

        # Deleting field 'Feedback.content'
        db.delete_column('feedbacks_feedback', 'content')

    models = {
        'feedbacks.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'content': ('django.db.models.fields.TextField', [], {}),
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
        },
        'feedbacks.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['feedbacks']