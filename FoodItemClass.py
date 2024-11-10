class FoodItem:
    def __init__(self, name):
        self.name = name # name of the food item
        self.modifiers = {} # modifiers to the food item
        self.modifiergroups = {}

    def addModifiers(self, modifiers, modifier):
        # Takes a food item and modifier as parameter
        # If modifier not in the dictionary, initialize it
        if (modifier not in modifiers.keys()):
            modifiers[modifier] = 1
        else:
            modifiers[modifier] += 1
    def addModifierGroup(self, modifiergroups, modifiergroup):
        # Takes a modifiergroups and modifiergroup
        # If modifiergroup not in modifiergroups, initialize it
        if (modifiergroup not in modifiergroups.keys()):
            modifiergroups[modifiergroup] =1
        else: # increment the frequency of modifier group
            modifiergroups[modifiergroup] += 1
    def output(self):
        print (self.name)
        print (self.modifiers)
        print (self.modifiergroups)