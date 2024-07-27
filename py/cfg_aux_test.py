from cfg_aux import *

def test_cfg_aux_subsectionName(
) -> str:
    section1 = f"static \"s-floor1\""
    section2 = f"texture \"t-floor1\""
    name1 = cfg_aux_subsectionName(section1)
    name2 = cfg_aux_subsectionName(section2)
    if (
        name1 == "s-floor1" and
        name2 == "t-floor1"
    ):
        return "OK: cfg_aux_subsectionName"
    return "ERR: cfg_aux_subsectionName"

def test_cfg_aux_tree(
) -> str:
    lines = [
        "[abc]",
        "width = 100",
        "wrongSep=another",
        "[def]",
        "anotherWrongSep -> whatever",
        "title = yo",
        "subtitle = whoa",
    ]
    tree = cfg_aux_tree(lines)
    if (
        cld_len(tree) == 2 and
        cld_len(tree["abc"]) == 1 and
        cld_len(tree["def"]) == 2
    ):
        return "OK: cfg_aux_tree"
    return "ERR: cfg_aux_tree"

def test_cfg_aux_treeCreateSection(
) -> str:
    tree: dict[str, dict[str, str]] = {}
    line = "[abc]"
    sectionName = cfg_aux_treeCreateSection(tree, line)
    if (
        sectionName == "abc" and
        cld_len(tree) == 1
    ):
        return "OK: cfg_aux_treeCreateSection"
    return "ERR: cfg_aux_treeCreateSection"

def test_cfg_aux_treeSetKeyValue(
) -> str:
    tree: dict[str, dict[str, str]] = {}
    line = "[abc]"
    sectionName = cfg_aux_treeCreateSection(tree, line)
    line = "title = wazup"
    cfg_aux_treeSetKeyValue(tree, sectionName, line)
    if (
        cld_len(tree[sectionName]) == 1 and
        tree[sectionName]["title"] == "wazup"
    ):
        return "OK: cfg_aux_treeSetKeyValue"
    return "ERR: cfg_aux_treeSetKeyValue"
