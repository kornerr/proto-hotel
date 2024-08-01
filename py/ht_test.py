from ht import *
from ht_Context import *

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
