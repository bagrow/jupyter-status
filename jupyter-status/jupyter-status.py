#!/usr/bin/env python
# -*- coding: utf-8 -*-

# jupyter-status.py
# Jim Bagrow
# Last Modified: 2020-08-19

import sys, os
import subprocess
import json
from operator import itemgetter
from datetime import datetime

import requests
from tabulate import tabulate


def main():
    try:
        tablefmt = sys.argv[1]
    except IndexError:
        tablefmt = None

    # first list all running notebooks to get all running servers:
    result = subprocess.check_output(['jupyter', 'notebook', 'list'])
    result = result.decode()
    R = result.strip().split("\n")
    if not R:
        print("No Jupyter servers running")
        sys.exit(0)
    if len(R) == 1:
        print("No Jupyter servers running")
        sys.exit(0)
    R = R[1:]

    # make a table of kernels for each server:
    for res in sorted(R):
        fullURL,path = res.strip().split("::")
        fullURL = fullURL.strip()
        path = path.strip()

        server,token = fullURL.split("?token=")
        server = server.replace("http://","").replace("/","")

        url = f"http://{server}/api/sessions"
        r = requests.get(url, params={"token" : token})
        D = r.json()
        L = []
        for d in D:
            name = d['name']
            kind = d['type']
            kernel_name = d['kernel']['name']
            last_active = d['kernel']['last_activity']
            status = d['kernel']['execution_state']

            last_active = datetime.strptime(last_active, "%Y-%m-%dT%H:%M:%S.%fZ")
            last_active = last_active.strftime("%Y-%m-%d %H:%M")

            L.append([name, kind, kernel_name, last_active, status])

        print(server, path)
        if L:
            h = ['Name', 'Type', 'Kernel', "Last active", "Status"]
            print(tabulate(sorted(L, key=itemgetter(1,2,0,4)), headers=h, tablefmt=tablefmt))
        else:
            print("No kernels running")
        print()
