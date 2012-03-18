# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'IndexSliderImage.page'
        db.delete_column('core_indexsliderimage', 'page_id')


    def backwards(self, orm):
        
        # Adding field 'IndexSliderImage.page'
        db.add_column('core_indexsliderimage', 'page', self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['flatpages.FlatPage'], unique=True), keep_default=False)


    models = {
        'core.indexsliderimage': {
            'Meta': {'ordering': "('position',)", 'object_name': 'IndexSliderImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        }
    }

    complete_apps = ['core']
