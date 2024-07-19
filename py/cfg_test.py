from cfg import *
from ht_Context import *

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
