# encoding: utf-8
from gnr.core.gnrdecorator import public_method  # rendere un metodo "chiamabile" dalla TH
from datetime import datetime, timedelta
from decimal import Decimal

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('pratica_anag', pkey='id', name_long='Pratica-Anag', caption_field='titolo')
        self.sysFields(tbl,user_upd=True)

        tbl.column('pratica_id',size='22', group='_', name_long='Pratica ID'
                    ).relation('pratica.id',relation_name='pratica_anag', mode='foreignkey', onDelete='cascade')
        
        tbl.column('anagrafica_id',size='22', group='_', name_long='Ctrb ID'
                    ).relation('anagrafica.id', relation_name='pratica_anag', mode='foreignkey', onDelete='raise')
        
        tbl.aliasColumn('num_pratica', '@pratica_id.num_pratica',dtype='I', name_long='N. Prat.')
        tbl.aliasColumn('anagrafica_nominativo', '@anagrafica_id.nominativo', name_long='Nominativo')
        tbl.formulaColumn('titolo',"$num_pratica || ' - ' || $anagrafica_nominativo",name_long='Titolo')