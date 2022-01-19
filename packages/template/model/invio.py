# encoding: utf-8

from gnr.core.gnrdecorator import public_method
from gnr.web.gnrbaseclasses import TableTemplateToHtml

# from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('invio', pkey='id', name_long='Invio', name_plural='Invii',caption_field='prot_int')
        self.sysFields(tbl,user_upd=True)

        tbl.column('prot_int', size='13', name_long='Protocollo Interno', name_short='Prot.Int.')
        tbl.column('pratica_anag_id', size='22', group='_', name_long='id prat ana'
                    ).relation('pratica_anag.id', relation_name='invio', mode='foreignkey', onDelete='cascade')

        tbl.column('data_invio', dtype='D', name_long='Data invio')
