#!/usr/bin/env python
# -*- coding: utf-8 -*-

# webserver le a captura

__author__ = 'Neviim JAds'
__versao__ = '0.1'

import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def get_loaddata(server):
    data_cursor = list()
    if server == 'neviim':
        data_cursor = dbh.neviim.find()
    elif server == 'jads':
        data_cursor = dbh.jads.find()

    disk_root_free = list()
    phymem_free = list()
    cpu_user = list()
    cpu_nice = list()
    cpu_system = list()
    cpu_idle = list()
    cpu_irq = list()

    for data in data_cursor:
        date = data['date']
        disk_root_free.append([date, data['disk_root']])
        phymem_free.append([date, data['phymem']])
        cpu_user.append([date, data['cpu']['user']])
        cpu_nice.append([date, data['cpu']['nice']])
        cpu_system.append([date, data['cpu']['system']])
        cpu_idle.append([date, data['cpu']['idle']])
        cpu_irq.append([date, data['cpu']['irq']])

    return {
            'disk_root_free': disk_root_free,
            'phymem_free': phymem_free,
            'cpu_user': cpu_user,
            'cpu_irq': cpu_irq,
            'cpu_system': cpu_system,
            'cpu_nice': cpu_nice,
            'cpu_idle': cpu_idle,
            }

if __name__ == '__main__':
    # ---
    try:
        conn = MongoClient(host="10.0.36.5", port=27017)   # aqui coloque o IP e Porta do seu servidor MongoDB.
    except ConnectionFailure, e:
        sys.stderr.write("Falha ao conectar no MongoDB: %s" % e)
        sys.exit(1)

    # abre o banco logserver
    dbh = conn["logserver"]

    if dbh.authenticate('neviim', 'logserver'):     # no mongoDB.

        print get_loaddata("neviim")