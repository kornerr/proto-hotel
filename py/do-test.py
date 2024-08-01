#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
sys.path.append(f"{SCRIPT_DIR}/../../cross-language-dialect/lib")

from cfg_aux_test import *
from cfg_test import *
from desc_aux_test import *
from ht_aux_test import *

functions = [
    test_cfg_parseComments,
    test_cfg_parseConfigTree,
    test_cfg_aux_subsectionName,
    test_cfg_aux_tree,
    test_cfg_aux_treeCreateSection,
    test_cfg_aux_treeSetKeyValue,
    test_desc_aux_isVisible,
    test_ht_aux_itemComment,
]

for f in functions:
    print(f())
