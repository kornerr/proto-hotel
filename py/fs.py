import os
from cld import *
from fs_aux import *
from ht_Context import *

# Extract directory from config path
#
# Conditions:
# 1. Config path has just been set
@cld_by_value
def fs_locateConfigDir(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField == "cfgPath"
    ):
        c.cfgDir = os.path.dirname(c.cfgPath)
        c.recentField = "cfgDir"
        return c

    c.recentField = "none"
    return c

# Read config file contents
#
# Conditions:
# 1. Config path has just been set
@cld_by_value
def fs_readConfig(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField == "cfgPath"
    ):
        c.cfgContents = fs_aux_readFile(c.cfgPath)
        c.recentField = "cfgContents"
        return c

    c.recentField = "none"
    return c

# Read scene contents for each scene
#
# Conditions:
# 1. Scenes are now known
@cld_by_value
def fs_readSceneConfigs(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField == "scenes"
    ):
        d = {}
        for name in c.scenes:
            file = c.scenes[name]
            path = c.cfgDir + "/" + file
            d[name] = fs_aux_readFile(path)
        c.sceneCfgContents = d
        c.recentField = "sceneCfgContents"
        return c

    c.recentField = "none"
    return c

# Read sound contents for each sound config
#
# Conditions:
# 1. Sounds are now known
@cld_by_value
def fs_readSoundConfigs(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField == "sounds"
    ):
        print("ИГР fs_readSC-1")
        d = {}
        for name in c.sounds:
            file = c.sounds[name]
            path = c.cfgDir + "/" + file
            print(f"ИГР fs_readSC-1 path: '{path}'")
            d[name] = fs_aux_readFile(path)
        c.soundCfgContents = d
        c.recentField = "soundCfgContents"
        return c

    c.recentField = "none"
    return c
