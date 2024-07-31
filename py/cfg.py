import os
from cfg_aux import *
from cld import *
from ht_Context import *

# Construct comment -> [delay, item, static] from config tree
#
# Conditions:
# 1. Config tree has just become available
@cld_by_value
def cfg_parseComments(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField != "cfgTree"
    ):
        c.recentField = "none"
        return c

    comms = {}
    for key in c.cfgTree:
        if (
            cld_startswith(key, "comment ")
        ):
            name = cfg_aux_subsectionName(key)
            item = c.cfgTree[key]
            comms[name] = [
                float(item["delay"]),
                item["item"],
                item["static"]
            ]
    c.comments = comms
    c.recentField = "comments"
    return c

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
