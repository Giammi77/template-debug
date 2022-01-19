#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('data')
        r.fieldcell('descrizione')
        r.fieldcell('note')
        r.fieldcell('letterhead_id')

    def th_order(self):
        return 'data'

    def th_query(self):
        return dict(column='descrizione', op='contains', val='')


class Form(BaseComponent):

    def th_form(self, form):

        bc = form.center.borderContainer()
        left = bc.borderContainer(region='left',width='45%',splitter=True)

        fb =left.contentPane(region='top',splitter=True,datapath='.record').div(margin_top='3px' ,margin_left='40px',margin_right='70px'
                            ).formbuilder(cols=2, border_spacing='3px',colswidth='auto',fld_width='100%')
        fb.field('data')
        fb.field('descrizione',colspan=2)
        fb.field('note',colspan=2)
        fb.field('letterhead_id')
        fb.dbSelect(dbtable='template.invio',value='^#FORM.testAtto.pkey',lbl='Record di Test',hasDownArrow=True)   
        fb.dataController("""PUT #FORM.testAtto.samplepkey = null;
                            SET #FORM.testAtto.samplepkey = selected_pkey || sample_pkey""",
                    selected_pkey='^#FORM.testAtto.pkey',sample_pkey='*sample*',_fired='^#FORM.controller.loaded')
        centerpane = bc.contentPane(region='center',datapath='.record')
        centerpane.dataRecord('#FORM.sample_letterhead','adm.htmltemplate',pkey='^#FORM.record.letterhead_id',
                                _if='pkey',_else='return new gnr.GnrBag();')
        centerpane.dataFormula('#FORM.available_height','(center_height || 297)+"mm";',center_height='^#FORM.sample_letterhead.center_height')
        centerpane.dataFormula('#FORM.available_width','(center_width || 210)+"mm";',center_width='^#FORM.sample_letterhead.center_width')
        paper = centerpane.div(height='^#FORM.available_height',width='^#FORM.available_width',margin='10px',border='1px dotted silver')
        paper.templateChunk(template='^#FORM.record.template_bag',table='template.invio',editable=True,
                                record_id='^#FORM.testAtto.samplepkey',
                                showLetterhead='^#FORM.sample_letterhead.id',
                                constrain_height='^#FORM.available_height',
                                constrain_width='^#FORM.available_width',
                                constrain_border='1px solid silver',
                                constrain_shadow='3px 3px 5px gray',
                                constrain_margin='4px',
                                constrain_rounded=3,
                                selfsubscribe_onChunkEdit="this.form.save();")


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px', duplicate=True)
























    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
