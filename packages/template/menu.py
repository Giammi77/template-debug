#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    template = root.branch('Template')
    template.thpage('Anagrafica',table='template.anagrafica')
    template.thpage('Pratiche',table='template.pratica')
    template.thpage('Dettagli Pratica',table='template.pratica_riga')
    template.thpage('Pratica-Anag',table='template.pratica_anag')
    template.thpage('Invii',table='template.invio')
    template.thpage('Template',table='template.template')
