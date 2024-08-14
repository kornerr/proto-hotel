class ht_Context:
    def __init__(self):
        self.cfgContents = []
        self.cfgDir = None
        self.cfgPath = None
        self.cfgTree = {}
        self.comments = {}
        self.didClickMouse = []
        self.didCreateConfigItemSprites = False
        self.didCreateConfigPlayerSprites = False
        self.didCreateConfigStaticSprites = False
        self.didLaunch = False
        self.didLoadConfigTextures = False
        self.hideStaticComment = None
        self.recentField = "none"
        self.scene = None
        self.sceneCfgContents = {}
        self.sceneCfgTrees = {}
        self.scenes = {}
        self.selectedComment = None
        self.selectedItem = None
        self.windowAntialiasing = False
        self.windowBackgroundColor = "#000000"
        self.windowHeight: float  = 0
        self.windowTitle = ""
        self.windowWidth: float = 0

    def field(self, fieldName):
        return getattr(self, fieldName)

    def setField(self, fieldName, value):
        setattr(self, fieldName, value)

def ht_createContext():
    return ht_Context()
