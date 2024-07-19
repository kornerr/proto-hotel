import os
from cfg_aux import *
from cld import *
from ht_Context import *

# Construct section -> key -> value tree from config contents
#
# Conditions:
# 1. Config contents have just become available
@cld_by_value
def cfg_parseConfigTree(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField == "cfgContents"
    ):
        c.cfgTree = cfg_aux_tree(c.cfgContents)
        c.recentField = "cfgTree"
        return c

    c.recentField = "none"
    return c
