from cfg import *
from ht_Context import *

def test_cfg_parseComments(
) -> str:
    c = ht_createContext()
    c.cfgTree = {
        "comment \"do-smth\"": {
            "delay": "1000",
            "item": "door",
            "static": "warning"
        }
    }
    c.recentField = "cfgTree"
    c = cfg_parseComments(c)
    if (
        cld_len(c.comments) == 1 and
        c.comments["do-smth"][0] == 1000
    ):
        return "OK: cfg_parseComments"
    return "ERR: cfg_parseComments"

def test_cfg_parseConfigTree(
) -> str:
    c = ht_createContext()
    c.cfgContents = [
        "[abc]",
        "width = 100",
        "wrongSep=another",
        "[def]",
        "anotherWrongSep -> whatever",
        "title = yo",
        "subtitle = whoa",
    ]
    c.recentField = "cfgContents"
    c = cfg_parseConfigTree(c)
    if (
        cld_len(c.cfgTree) == 2
    ):
        return "OK: cfg_parseConfigTree"
    return "ERR: cfg_parseConfigTree"

def test_cfg_parseScenes(
) -> str:
    c = ht_createContext()
    c.cfgTree = {
        "scene \"floor-1\"": {
            "file": "scn/floor-1.config"
        }
    }
    c.recentField = "cfgTree"
    c = cfg_parseScenes(c)
    if (
        cld_len(c.scenes) == 1 and
        c.scenes["floor-1"] == "scn/floor-1.config"
    ):
        return "OK: cfg_parseScenes"
    return "ERR: cfg_parseScenes"
