#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='template package',sqlschema='template',sqlprefix=True,
                    name_short='Template', name_long='Template', name_full='Template')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
