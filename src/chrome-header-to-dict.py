#!/usr/bin/env python

import sys
import json
from collections import OrderedDict


headers = OrderedDict()
for line in sys.stdin.readlines():
    line = line.strip()
    if not line:
        continue

    start_col = line.find(':')
    if start_col == -1:
        continue

    key, value = line[:start_col].strip(), line[start_col+1:].strip()
    headers[key] = value


print(json.dumps(headers, indent=4))