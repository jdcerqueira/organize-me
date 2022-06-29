from configparser import ConfigParser
from encodings import utf_8
import os
from textwrap import indent
from tkinter import image_types
import requests
from flask import request, jsonify
import json

from tenacity import retry_if_not_exception_message

class Properties():
    def __init__(self, section):
        self.properties = {}

        config = ConfigParser()
        config.read(os.path.abspath("config/config.properties"))
        for item in config[section]:
            self.properties[item] = config[section][item]

class Bancos():
    def __init__(self):
        listagem = json.load(open(os.path.abspath("config/listaBancos.json"),"r", encoding="utf-8"))
        self.listaBancos = []
        for item in listagem:
            self.listaBancos.append({"banco":item["value"], "nome":item["label"]})
        

if __name__=="__main__":
    print(json.dumps(Bancos().listaBancos, indent=4, ensure_ascii=False))