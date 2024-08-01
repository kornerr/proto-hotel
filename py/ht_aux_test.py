from ht_aux import *

def test_ht_aux_itemComment(
) -> str:
    comments = {
        "comm1": [700, "some", "yo"],
        "comm2": [700, "another", "wo"],
    }
    r1 = ht_aux_itemComment(comments, "another")
    r2 = ht_aux_itemComment(comments, "absent")

    if (
        r1 == "comm2" and
        r2 is None
    ):
        return "OK: ht_aux_itemComment"
    return "ERR: ht_aux_itemComment"
