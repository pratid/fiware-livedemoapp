#!/usr/bin/python
# -*- coding: latin-1 -*-
# Copyright 2013 Telefonica Investigación y Desarrollo, S.A.U
#
# This file is part of FI-WARE LiveDemo App
#
# FI-WARE LiveDemo App is free software: you can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# FI-WARE LiveDemo App is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License
# for more details.
#
# You should have received a copy of the GNU Affero General Public License along with FI-WARE LiveDemo App. If not,
# see http://www.gnu.org/licenses/.
#
# For those usages not covered by the GNU Affero General Public License please contact with fermin at tid dot es

__author__ = 'fermin'

import subprocess
from lxml import etree

p = subprocess.Popen(["./query-all.sh"], shell=False, stdout=subprocess.PIPE)
output = p.stdout.read()

doc = etree.fromstring(output)

records = {}
no_time = []
for ce in doc.findall('.//contextElement'):
    id = ce.find('.//id').text
    for ca in ce.findall('.//contextAttribute'):
        if (ca.find('name').text == 'TimeInstant'):
            t = ca.find('contextValue').text
            # Sometimes is an actual None, sometimes is the "None" string
            if t == 'None' or t == None:
                no_time.append(id)
            else:
                records[t] = id

times = records.keys()
times.sort()
times.reverse()
for t in times:
    print repr(records[t]).ljust(35), ': ', str(t)
for i in no_time:
    print repr(i).ljust(35), ': ', "None"
