#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('pratica_id')
        r.fieldcell('anagrafica_id')
        r.fieldcell('titolo')

    def th_order(self):
        return 'pratica_id'

    def th_query(self):
        return dict(column='num_pratica', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('pratica_id' )
        fb.field('anagrafica_id' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
