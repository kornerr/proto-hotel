from cld import *

# Extract subsection name from config section
def cfg_aux_subsectionName(
    section: str
) -> str:
    # Find the first ' "'.
    quotePos = cld_find(section, " \"")
    start = quotePos + 2
    return section[start:-1]

# Convert config contents to tree: sections -> keys -> values
def cfg_aux_tree(
    cfgContents: [str]
) -> dict[str, dict[str, str]]:
    tree: dict[str, dict[str, str]] = {}
    currentSection = None
    n = cld_len(cfgContents)
    for i in range(0, n):
        line = cfgContents[i]
        # Section.
        if (
            cld_startswith(line, "[")
        ):
            currentSection = cfg_aux_treeCreateSection(tree, line)
        # Key = Value.
        else:
            cfg_aux_treeSetKeyValue(tree, currentSection, line)
    return tree

# Create new section in the tree
def cfg_aux_treeCreateSection(
    tree: dict[str, dict[str, str]],
    line: str
) -> str:
    # Strip characters `[` and `]` at both ends.
    sectionName = line[1:-1]
    tree[sectionName] = {}
    return sectionName

# Register key-value pair in the tree
def cfg_aux_treeSetKeyValue(
    tree: dict[str, dict[str, str]],
    sectionName: str,
    line: str
):
    parts = line.split(" = ")
    # Ignore invalid key-value pairs.
    if (
        cld_len(parts) != 2
    ):
        return

    key = parts[0]
    value = parts[1]
    tree[sectionName][key] = value
