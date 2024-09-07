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

# Construct comment -> [delay, item, static] from scene config tree
#
# Conditions:
# 1. Scene config tree has just become available
@cld_by_value
def cfg_parseSceneComments(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField == "sceneCfgTrees" or
        (
            c.recentField == "scene" and
            c.selectedItem is not None
        )
    ):
        pass
    else:
        c.recentField = "none"
        return c

    tree = c.sceneCfgTrees[c.scene]
    comms = {}
    for key in tree:
        if (
            cld_startswith(key, "comment ")
        ):
            name = cfg_aux_subsectionName(key)
            item = tree[key]
            comms[name] = [
                float(item["duration"]),
                item["item"],
                item["static"]
            ]
    c.comments = comms
    c.recentField = "comments"
    return c

# Construct name -> key -> value trees from scene config contents
#
# Conditions:
# 1. Scene config contents have just become available
@cld_by_value
def cfg_parseSceneConfigTrees(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField == "sceneCfgContents"
    ):
        trees = {}
        for sceneName in c.sceneCfgContents:
            contents = c.sceneCfgContents[sceneName]
            trees[sceneName] = cfg_aux_tree(contents)
        c.sceneCfgTrees = trees
        c.recentField = "sceneCfgTrees"
        return c

    c.recentField = "none"
    return c

# Construct goto -> [item, scene] from scene config tree
#
# Conditions:
# 1. Scene config tree has just become available or scene changed when item was selected
@cld_by_value
def cfg_parseSceneGoto(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField == "sceneCfgTrees" or
        (
            c.recentField == "scene" and
            c.selectedItem is not None
        )
    ):
        pass
    else:
        c.recentField = "none"
        return c

    tree = c.sceneCfgTrees[c.scene]
    goto = {}
    for key in tree:
        if (
            cld_startswith(key, "goto ")
        ):
            name = cfg_aux_subsectionName(key)
            item = tree[key]
            goto[name] = [
                item["delay"] if "delay" in item else 0,
                item["item"],
                item["playerBase"] if "playerBase" in item else None,
                item["playerLeft"] if "playerLeft" in item else None,
                item["scene"]
            ]
    c.goto = goto
    c.recentField = "goto"
    return c

# Construct scene -> file from config tree
#
# Conditions:
# 1. Config tree has just become available
@cld_by_value
def cfg_parseScenes(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField != "cfgTree"
    ):
        c.recentField = "none"
        return c

    scns = {}
    for key in c.cfgTree:
        if (
            cld_startswith(key, "scene ")
        ):
            name = cfg_aux_subsectionName(key)
            item = c.cfgTree[key]
            scns[name] = item["file"]
    c.scenes = scns
    c.recentField = "scenes"
    return c
