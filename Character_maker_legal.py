#Christopher Marte
#Drew Askins

import random

def present_options_and_pick(list_of_options,question="look at your options and pick one: ",randomOption = True):

    if randomOption:
        #I should have random at the begining of every list no matter what | So that was false, the parameters function doesn't need a random option
        list_of_options.insert(0,"Random")
    
    #SHOW ME THE OPTIONS
    print("------------------------------------------")
    for index,option in enumerate(list_of_options):
        print(f"{index} - {option}")
    print("------------------------------------------")

    while True:
        #Pick an Option
        user = int(input(f"{question}"))

        #Check if it is a valid option
        if 0 <= user < len(list_of_options):
            break
        print(f"Error: please input a correct option\n{question}")

    
    #Return User response
    return user

def choose_auto_parameter() -> bool:
    parameters = [False,True]
    para = present_options_and_pick(parameters, question = "Auto? ",randomOption=False)
    return parameters[para]

def get_gender(auto) -> str:
    gender_list = ["Male", "Female"]

    if auto: 
        return random.choice(gender_list)
    
    user = present_options_and_pick(gender_list, question = "Gender? ")

    if user == 0:
        return random.choice(gender_list)
    else:
        return gender_list[user]

def get_race(auto) -> tuple:
    from DnD_Data import RACES
    races = list(RACES.keys())

    if auto:
        race_ = random.choice(races)
    
    if auto == False:
        user = present_options_and_pick(races, question = "Race? ")

        if user == 0:
            race_ = random.choice(list(RACES.keys())) #using RACES.keys() because presentoptions changes the list RACES_LIST
        else: 
            race_ = races[user]

    subraces = RACES.get(race_,[])
    subrace_ = random.choice(subraces) if subraces else None
                                        #if ^^^ is empty or [] then it is a falsy and will assign subrace_ as None
    return race_,subrace_

def roll_dice(diceNum:int=1,diceType:int=20) -> int:
    "This Function rolls the dice for you, by default it rolls 1d20"
    rollTotal = 0
    for roll in range(diceNum):
        rollTotal += random.randint(1,diceType)
    return rollTotal

def get_height_and_weight(race,subrace) -> tuple:
    from DnD_Data import HEIGHT_WEIGHT

    #get info
    if race not in HEIGHT_WEIGHT:
        raise Exception("No data available for selected race")
    if subrace in HEIGHT_WEIGHT[race]:
        base_height = HEIGHT_WEIGHT[race][subrace]["base_height"]
        base_weight = HEIGHT_WEIGHT[race][subrace]["base_weight"]
        height_mod = roll_dice(*HEIGHT_WEIGHT[race][subrace]["height_mod"])
        weight_mod = roll_dice(*HEIGHT_WEIGHT[race][subrace]["weight_mod"])
    else:
        base_height = HEIGHT_WEIGHT[race]["base_height"]
        base_weight = HEIGHT_WEIGHT[race]["base_weight"]
        height_mod = roll_dice(*HEIGHT_WEIGHT[race]["height_mod"])
        weight_mod = roll_dice(*HEIGHT_WEIGHT[race]["weight_mod"])


    HEIGHT_FORMULA = lambda baseHeight,heightModifier: baseHeight+heightModifier
    WEIGHT_FORMULA = lambda baseWeight,weightModifier,heightModifier: baseWeight+(weightModifier*heightModifier)

    height = HEIGHT_FORMULA(base_height,height_mod)
    weight = WEIGHT_FORMULA(base_weight,weight_mod,height_mod)

    return height,weight

def get_languages(race,subrace) -> list:

    from DnD_Data import LANGUAGES
    race_languages = LANGUAGES["RACE_LANGUAGES"]
    languages = LANGUAGES["FULL_LIST"]

    languages_ = [] #keeps track of the languages your character knows

    race_language = race_languages[race]
    if race_language == None: #This is for Humans
        race_language = random.choice(languages)
    
    languages_.append(race_language)

    if subrace == "High Elf":
        while True:
            race_language2 = random.choice(languages)
            if race_language2 not in languages_:
                languages_.append(race_language2)
                break

    return languages_

def get_name(race,sex,subrace):
    from DnD_Data import NAMES
    if race == "Genasi":
        last_name = random.choice(NAMES[race]["last_names"][subrace])
    else:
        last_name = random.choice(NAMES[race]["last_names"])
    first_name = random.choice(NAMES[race]["first_names"][sex])

    return last_name,first_name
        
def get_class(auto):
    from DnD_Data import CLASSES
    CLASSES_LIST = [CLASS for CLASS in CLASSES.keys()]

    if auto == True:
        char_class = random.choice(CLASSES_LIST)
        char_subclass = random.choice(CLASSES[char_class])
    else:
        user = present_options_and_pick(CLASSES_LIST,"Class? ")

        if user == 0:
            char_class = random.choice(CLASSES_LIST)
            char_subclass = random.choice(CLASSES[char_class])
            return char_class,char_subclass
        else:
            char_class = CLASSES_LIST[user]
            char_subclass = random.choice(CLASSES[char_class])

    return char_class,char_subclass

def get_background(auto):
    from DnD_Data import BACKGROUND
    backgrounds = list(BACKGROUND.keys())

    if auto: 
        background_ = random.choice(backgrounds)
        
    else:
        user = present_options_and_pick(backgrounds,"Background? ")
        if user == 0:
            background_ = random.choice(list(BACKGROUND.keys()))
        else:
            background_ = backgrounds[user]
    
    return background_

def get_personality(background):
    from DnD_Data import PERSONALITY_TRAITS
    personalities = PERSONALITY_TRAITS[background]
    characterPersonality = {}
    for characteristic in personalities:
        if characteristic not in ["Trait","Ideal","Bond","Flaw"]:
            characterPersonality[f"{characteristic}"] = random.choice(personalities[characteristic])
        match characteristic:
            case "Trait": 
                characterPersonality["Trait"] = random.choice(personalities[characteristic])
            case "Ideal":
                characterPersonality["Ideal"] = random.choice(personalities[characteristic])
            case "Bond":
                characterPersonality["Bond"] = random.choice(personalities[characteristic])
            case "Flaw":
                characterPersonality["Flaw"] = random.choice(personalities[characteristic])

    return characterPersonality

def get_gold(BGL=10):
    Gold = BGL
    return Gold

def get_trinket():
    from DnD_Data import TRINKETS
    Trinket = random.choice(TRINKETS)
    return Trinket

class Character():
    def __init__(self,auto=False) -> None:
        self.sex = get_gender(auto)
        self.race,self.subrace = get_race(auto)
        self.lastName,self.firstName = get_name(self.race,self.sex,self.subrace)
        self.height,self.weight = get_height_and_weight(self.race,self.subrace)
        self.languages = get_languages(self.race,self.subrace)
        self.fullName = f"{self.firstName} {self.lastName}"
        self.char_class = get_class(auto)
        self.background = get_background(auto)
        
        self.personality = get_personality(self.background)
        self.trait = self.personality.pop("Trait")
        self.ideal = self.personality.pop("Ideal")
        self.bond = self.personality.pop("Bond")
        self.flaw = self.personality.pop("Flaw")
        if self.personality:
            self.feature = self.personality
        
        self.gold = get_gold()
        self.trinket = get_trinket()

    def present_character_info(self):
        print("------------------------------------------")
        if self.subrace == None:
            print(f"You are a {self.sex} {self.race}")
        else:
            print(f"You are a {self.sex} {self.subrace}")
        print(f"Your name is {self.fullName}")
        print(f"Your height is {self.height} inches")
        print(f"Your weight is {self.weight} pounds")
        print(f"Your Class is {self.char_class}")
        print(f"Your background is {self.background}")
        if self.personality:
            for feature in self.feature:
                match feature:
                    case "Scam": 
                        print(f"Your favored scam: {self.feature[feature]}")
                    case "Specialty": 
                        print(f"Your {self.background} specialty: {self.feature[feature]}")
                    case "Routine":
                        print(f"Your entertainer routine: {self.feature[feature]}")
                    case "Event": 
                        print(f"Your defining event: {self.feature[feature]}")
                    case "Business":
                        print(f"Your Guild Business: {self.feature[feature]}")
                    case "Seclusion":
                        print(f"Your life of seclusion: {self.feature[feature]}")
                    case "Origin":
                        print(f"Your Outlander origin: {self.feature[feature]}")
        print(f"You personality trait: {self.trait}")
        print(f"Your ideal: {self.ideal}")
        print(f"Your bond: {self.bond}")
        print(f"Your flaw: {self.flaw}")
        print(f"You speak Common, {' '.join(str(x) for x in self.languages)}") #fix this {" ".join(str(x) for x in self.languages)}
        print(f"Your starting gold: {self.gold}")
        print(f"Your trinket: {self.trinket}")
        print("------------------------------------------")

def main():
    AUTO = choose_auto_parameter()
    P1_Character = Character(AUTO)
    P1_Character.present_character_info()

if __name__ == "__main__":
    main()