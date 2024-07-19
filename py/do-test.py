#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
sys.path.append(f"{SCRIPT_DIR}/../../cross-language-dialect/lib")

from cfg_aux_test import *
from cfg_test import *

functions = [
    test_cfg_parseConfigTree,
    test_cfg_aux_staticSpriteName,
    test_cfg_aux_textureName,
    test_cfg_aux_tree,
    test_cfg_aux_treeCreateSection,
    test_cfg_aux_treeSetKeyValue,
]

for f in functions:
    print(f())
