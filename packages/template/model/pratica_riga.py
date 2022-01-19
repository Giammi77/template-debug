# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('pratica_riga', pkey='id', caption_field='anno', name_long='Dettaglio Pratica', name_plural='Dettagli Pratica')
        self.sysFields(tbl,user_upd=True)
        tbl.column('pratica_id', size='22', name_long='num.pratica'
                    ).relation('pratica.id', relation_name='pratica_riga', mode='foreignkey', onDelete='cascade')
        tbl.column('anno',dtype='I',name_long='anno',legacy_name='anno')
