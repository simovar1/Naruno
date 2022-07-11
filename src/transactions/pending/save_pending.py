#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import json
import os
from hashlib import sha256

from config import PENDING_TRANSACTIONS_PATH
from lib.config_system import get_config

def SavePending(tx):
    file_name = sha256((tx.signature).encode('utf-8')).hexdigest()
    the_path = PENDING_TRANSACTIONS_PATH + f"{file_name}.json"
    os.chdir(get_config()["main_folder"])
    with open(the_path, "w") as my_transaction_file:
        json.dump(tx.dump_json(), my_transaction_file)