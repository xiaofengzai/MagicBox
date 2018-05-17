# -*- coding: UTF-8 -*-
'''
支持对cfg,conf,ini配置文件的读取
'''
import ConfigParser

def readConfig(fileName):
    config=ConfigParser.ConfigParser()
    config.read(fileName)
    return config

def readValues(fileName,section):
    return dict(readConfig(fileName).items(section))

def readValue(fileName,section,key):
    return readConfig(fileName).get(section,key)
