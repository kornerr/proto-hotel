from desc_aux import *

def test_desc_aux_isVisible(
) -> str:
    desc1 = {}
    desc2 = {"visible": "true"}
    result1 = desc_aux_isVisible(desc1)
    result2 = desc_aux_isVisible(desc2)
    if (
        result1 == False and
        result2 == True
    ):
        return "OK: desc_aux_isVisible"
    return "ERR: desc_aux_isVisible"
