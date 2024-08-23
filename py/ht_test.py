from ht import *
from ht_Context import *

def test_ht_delayScene(
) -> str:
    c = ht_createContext()
    c.goto = {
        "goto1": [700, "some", None, None, "yo"]
    }
    c.selectedGoto = "goto1"
    c.recentField = "selectedGoto"
    c = ht_delayScene(c)
    if (
        c.delayScene == "yo"
    ):
        return "OK: ht_delayScene"
    return "ERR: ht_delayScene"

def test_ht_selectComment(
) -> str:
    c = ht_createContext()
    c.comments = {
        "comm1": [700, "some", "yo"],
        "comm2": [700, "another", "wo"],
    }
    c.selectedItem = "some"
    c.recentField = "selectedItem"
    c = ht_selectComment(c)
    if (
        c.selectedComment == "comm1"
    ):
        return "OK: ht_selectComment"
    return "ERR: ht_selectComment"
