# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('anagrafica', pkey='id', name_long='Anagrafica', name_plural='Anagrafica',
                            caption_field='nominativo')
        self.sysFields(tbl,user_upd=True)
        tbl.column('nominativo',name_long='Nominativo')
  