#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import types
from marker import marker

def setConfig():
    configPath = 'config.json'
    with open(configPath,'r') as f: data=json.load(f)
    return data

def configToArgs(data):
    args = types.SimpleNamespace()
    args.angle = data["angle"]
    args.color = data["color"]
    args.file = data["file"]
    args.mark = data["mark"]
    args.opacity = data["opacity"]
    args.out = data["out"]
    args.quality = data["quality"]
    args.size = data["size"]
    args.space = data["space"]
    return args

picArr = [];
args=configToArgs(setConfig())
marker(args)
