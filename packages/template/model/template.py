# encoding: utf-8
from gnr.core.gnrbag import Bag

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('template', pkey='id', name_long='Template', name_plural='Template',
            caption_field='descrizione')
        self.sysFields(tbl,user_upd=True)

        tbl.column('data', dtype='D', name_long='Data')
        tbl.column('descrizione', size=':50', name_long='Descrizione')
        tbl.column('note', 'T', name_long='!![it]Note')
        tbl.column('template_bag', dtype='X', name_long='Template')
        tbl.column('letterhead_id',size='22',group='_',name_long='!!Letterhead'
                    ).relation('adm.htmltemplate.id',relation_name='template',mode='foreignkey')
        
    def onDuplicating_many(self, record, copy_number=None, copy_label=None):
        record['descrizione'] = record['descrizione'] + '/ Copia ' + str(copy_number+1)