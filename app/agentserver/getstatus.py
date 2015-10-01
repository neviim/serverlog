#!/usr/bin/env python
# -*- coding: utf-8 -*-

# agente de captura

__author__ = 'Neviim JAds'
__versao__ = '0.1'

import sys
import psutil
import socket
import pymongo

from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# conect
def monta_jason():
        # le as informacoes do sistema.
        cpu = psutil.cpu_times_percent()
        disk_root = psutil.disk_usage('/')
        ram = psutil.virtual_memory()
        phymem = ram.total

        # monta um dicionario com as informacoes.
        doc = dict()
        doc['server'] = socket.gethostname()
        doc['date'] = datetime.now()
        doc['disk_root'] = disk_root.free,
        doc['phymem'] = ram.free
        doc['cpu'] = {
            'user': cpu.user,
            'nice': cpu.nice,
            'system': cpu.system,
            'idle': cpu.idle,
            'irq': cpu.irq
        }
        return doc

# main
def main():
    try:
        c = MongoClient(host="10.0.36.5", port=27017)   # aqui coloque o IP e Porta do seu servidor MongoDB.
    except ConnectionFailure, e:
        sys.stderr.write("Falha ao conectar no MongoDB: %s" % e)
        sys.exit(1)

    # abre o banco logserver
    dbh = c["logserver"]

    # se altenticação for true
    if dbh.authenticate('neviim', 'logserver'):     # aqui coloque seu Usuario e Senha do banco MongoDB.

        # monta o json das variaveis
        pdoc = monta_jason()

        # escreve na collection neviim
        dbh.neviim.insert(pdoc)      # aqui entra o nome da sua maqui monitorada, neviim dev é a minha.
        #print "Successfully inserted document: %s" % doc

# --- inicio
if __name__ == '__main__':
    main()
