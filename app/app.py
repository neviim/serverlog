#!/usr/bin/env python
# -*- coding: utf-8 -*-

# webserver le a captura

__author__ = 'Neviim JAds'
__versao__ = '0.1'

from flask import Flask, jsonify
from flask import render_template
from flask import make_response
from flask import url_for
from flask import request
from flask import abort

import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

app = Flask(__name__, static_path='/static')

# abre o banco de dados mongodb.
try:
    conn = MongoClient(host="10.0.36.5", port=27017)   # aqui coloque o IP e Porta do seu servidor MongoDB.
except ConnectionFailure, e:
    sys.stderr.write("Falha ao conectar no MongoDB: %s" % e)
    sys.exit(1)

# abre o banco logserver
dbh = conn["logserver"]

# se altenticação for true
if not dbh.authenticate('neviim', 'logserver'):     # aqui coloque seu Usuario e Senha do banco MongoDB.
    sys.stderr.write("Falha de autenticação no banco.")
    sys.exit(1)

def monitor_cpu(server):
    data_cursor = list()
    if server == 'neviim':
      #page=50
      #data_cursor = dbh.neviim.find({ 'server':'srv-oratst' }).sort("date",pymongo.DESCENDING).skip((page-1)*10).limit(5)
        data_cursor = dbh.neviim.find({ 'server':'srv-oratst' }).sort("date",pymongo.DESCENDING).limit(576)
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

    dados = {
            'disk_root_free': disk_root_free,
            'phymem_free': phymem_free,
            'cpu_user': cpu_user,
            'cpu_irq': cpu_irq,
            'cpu_system': cpu_system,
            'cpu_nice': cpu_nice,
            'cpu_idle': cpu_idle,
            }

    return dados

@app.route("/")
def index():
    return  render_template('index.html')

@app.route("/api/get_cpu")
def get_cpu():
    doc = monitor_cpu('neviim')
    return jsonify(results=doc)

@app.route("/ping")
def pong():
    return "pong"

@app.route('/cpu')
def cpu():
  return render_template('cpu.html')

@app.route('/ps')
def ps():
  return render_template('psmonitor.html')

# --- sobe o serviço web.
if __name__ == '__main__':
    app.run(  debug=True,
                    host="0.0.0.0",
                    port=int("4000")
    )