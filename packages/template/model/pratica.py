# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('pratica', pkey='id', caption_field='num_pratica', name_long='Pratica', name_plural='Pratiche')
        self.sysFields(tbl,user_upd=True)
        
        tbl.column('num_pratica', dtype='I', name_long='N. Prat.')


