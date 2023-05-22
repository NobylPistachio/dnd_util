#Christopher Marte
#Drew Askins

import random

def present_options_and_pick(list_of_options,question="look at your options and pick one: ",randomOption = True):
    
    # options1 = [a for a in options] #have to copy it so any changes in here wouldn't affect the list outside of here

    if randomOption:
        #I should have random at the begining of every list no matter what  | So that was false, the parameters function doesn't need a random option
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

def choose_auto_parameter():
    parameters = [False,True]
    para = present_options_and_pick(parameters, question = "Auto? ",randomOption=False)
    return parameters[para]

def get_gender(auto):
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
        
    user = present_options_and_pick(races, question = "Race? ")

    if user == 0:
        race_ = random.choice(list(RACES.keys())) #using RACES.keys() because presentoptions changes the list RACES_LIST
    else: 
        race_ = races[user]

    subraces = RACES.get(race_,[])
    subrace_ = random.choice(subraces) if subraces else None
                                        #if ^^^ is empty or [] then it is a falsy and will assign subrace_ as None

    # try: subrace_ = random.choice(RACES[race_])  #IndexError: list index out of range, This is because there are no subraces for Aarakocra,or because "Random" was being selected
    # except IndexError: subrace_ = None


    return race_,subrace_

def roll_dice(diceNum:int=1,diceType:int=20) -> int:
    "This Function rolls the dice for you, by default it rolls 1d20"
    rollTotal = 0
    for roll in range(diceNum):
        rollTotal += random.randint(1,diceType)
    return rollTotal

def Height(baseHeight,heightMod):
    height = baseHeight + heightMod
    return height

def Weight(baseWeight,weightMod,heightMod):
    weight = baseWeight + (weightMod*heightMod)
    return weight

def HeightAndWeight(race,subrace):
    match race:
        case "Aarakocra":
            baseHeight = 50
            baseWeight = 80
            heightMod = roll_dice(2,4)
            weightMod = roll_dice(2,10)
        case "Dragonborn":
            baseHeight = 50
            baseWeight = 80
            heightMod = roll_dice(2,10)
            weightMod = roll_dice(2,6)
        case "Dwarf":
            match subrace:
                case "Mountain Dwarf":
                    baseHeight = 48
                    baseWeight = 115
                    heightMod = roll_dice(2,4)
                    weightMod = roll_dice(2,6)
                case "Hill Dwarf":
                    baseHeight = 44
                    baseWeight = 115
                    heightMod = roll_dice(2,4)
                    weightMod = roll_dice(2,6)
        case "Elf":
            match subrace:
                case "Dark Elf":
                    baseHeight = 44
                    baseWeight = 75
                    heightMod = roll_dice(2,6)
                    weightMod = roll_dice(2,6)
                case "Ground Elf":
                    baseHeight = 60
                    baseWeight = 100
                    heightMod = roll_dice(2,4)
                    weightMod = roll_dice(2,4)
                case "High Elf":
                    baseHeight = 90
                    baseWeight = 100
                    heightMod = roll_dice(2,10)
                    weightMod = roll_dice(2,4)
                case "Wood Elf":
                    baseHeight = 90
                    baseWeight = 100
                    heightMod = roll_dice(2,10)
                    weightMod = roll_dice(2,4)
                case _ : raise Exception("Subrace doesn't exist")
        case "Genasi":
            baseHeight = 56
            baseWeight = 110
            heightMod = roll_dice(2,10)
            weightMod = roll_dice(2,4)
        case "Gnome":
            baseHeight = 31
            baseWeight = 35
            heightMod = roll_dice(2,4)
            weightMod = 1
        case "Goliath":
            baseHeight = 84
            baseWeight = 140
            heightMod = roll_dice(2,6)
            weightMod = roll_dice(2,4)
        case "Half-Elf":
            baseHeight = 57
            baseWeight = 110
            heightMod = roll_dice(2,8)
            weightMod = roll_dice(2,4)
        case "Halfling":
            baseHeight = 28
            baseWeight = 35
            heightMod = roll_dice(2,6)
            weightMod = 1
        case "Half-Orc":
            baseHeight = 58
            baseWeight = 140
            heightMod = roll_dice(2,10)
            weightMod = roll_dice(2,6)
        case "Human":
            baseHeight = 56
            baseWeight = 110
            heightMod = roll_dice(2,10)
            weightMod = roll_dice(2,4)
        case "Tiefling":
            baseHeight = 57
            baseWeight = 110
            heightMod = roll_dice(2,8)
            weightMod = roll_dice(2,4)
    height = Height(baseHeight,heightMod)
    weight = Weight(baseWeight,weightMod,heightMod)
    return height,weight

def get_languages(race,subrace) -> set:

    from DnD_Data import LANGUAGES
    race_languages = LANGUAGES["RACE_LANGUAGES"]

    languages = set() #keeps track of the languages your character knows
    
    #I need to make a dictionary specifically for this, the LANGUAGES dictionary isn't going to cut it

                        #GPT ASSIST

                    # race_languages = LANGUAGES["RACE_LANGUAGES"]

                    # languages = set()  # keeps track of the languages your character knows

                    # race_language_map = {
                    #     "Aarakocra": "Aarakocra",
                    #     "Dragonborn": "Draconic",
                    #     "Dwarf": "Dwarvish",
                    #     "Elf": "Elvish",
                    #     "Genasi": "Primordial",
                    #     "Gnome": "Gnomish",
                    #     "Goliath": "Giant",
                    #     "Half-Elf": "Elvish",
                    #     "Halfling": "Halfling",
                    #     "Half-Orc": "Orcish",
                    #     "Human": None,  # Language of their choosing
                    #     "Tiefling": "Infernal"
                    # }

                    # race_language = race_language_map.get(race)
                    # if race_language is not None:
                    #     languages.add(race_language)

                    # if race == "Elf" and subrace == "High Elf":
                    #     additional_language = random.choice(race_languages)
                    #     while additional_language == "Elvish":
                    #         additional_language = random.choice(race_languages)
                    #     languages.add(additional_language)

                    # return languages
    
    match race:
        case "Aarakocra": raceLanguage = "Aarakocra"
        case "Dragonborn": raceLanguage = "Draconic"
        case "Dwarf": raceLanguage = "Dwarvish"
        case "Elf":
            if subrace == "High Elf":
                raceLanguage2 = random.choice(race_languages) #High Elves get an Extra Language
                while raceLanguage2 == "Elvish": #Make sure the other language isn't Elvish, maybe have an option to only have elvish? 
                    raceLanguage2 = random.choice(race_languages)
                languages.add(raceLanguage2)
            raceLanguage = "Elvish"
        case "Genasi": raceLanguage = "Primordial"
        case "Gnome": raceLanguage = "Gnomish"
        case "Goliath": raceLanguage = "Giant"
        case "Half-Elf": raceLanguage = "Elvish"
        case "Halfling": raceLanguage = "Halfling" 
        case "Half-Orc": raceLanguage = "Orcish"
        case "Human": raceLanguage = random.choice(race_languages) #Language of their choosing
        case "Tiefling": raceLanguage = "Infernal"
    if raceLanguage not in languages:
        languages.add(raceLanguage)
    else:
        print("THIS NOW SHOULDN'T BE POSSIBLE")
        print(languages)
        print(f"{raceLanguage} {raceLanguage2}")
        raise Exception("The race language is already inside current languages")
    return languages

def organizing_name_dict(race,sex,subrace):
    match race:

        # case "":
        #     _LASTNAMES = []
        #     _FIRSTNAMES_MALE = []
        #     _FIRSTNAMES_FEMALE = []

        #     lastName = random.choice(_LASTNAMES)
        #     match sex:
        #         case "Male": firstName = random.choice(_FIRSTNAMES_MALE)
        #         case "Female": firstName = random.choice(_FIRSTNAMES_FEMALE)

        #I have to make the dictionary for names of the races
        case "Aarakocra":

            AARAKOCRA_LASTNAMES = ["Air", "Airborn", "Airman", "Breeze", "Cloud", "Current", "Cyclone", "DeAera", "DeAerag", "DeAerk","DeAerka", "DeAial", "DeAialro", "DeAldug", "DeAldugek", "DeAur", "DeAurin", "DeDeekek", "DeDeelek", "DeErrk","DeErrok", "DeHeehk", "DeHelehk", "DeIkki", "DeIkkit", "DeIleak", "DeIlek", "DeKilco", "DeKilcop", "DeKleeck","DeKloock", "DeLagin", "DeLugin", "DeOerett", "DeOorr", "DeOusl", "DeOust", "DeQuaf","DeQuet", "DeQuierk" ,"DeQuilet", "DeQuizik", "DeQuko", "DeRani", "DeRenzu", "DeSalleek", "DeSazel", "DeSejlik", "DeSileg", "DeUnok","DeUrreek", "DeZeed", "DeZelid", "DeZelip", "DeZiko", "DeZygic", "DeZylex", "Flow", "Fly", "Gale","Galeborn", "Galeman", "Glide", "Gust", "Lift", "Sky", "Skybirch", "Skyborn", "Skybranch", "Skyelm","Skyfield", "Skygarden", "Skygrove", "Skylily", "Skymaple", "Skymeadow", "Skyoak", "Skyorchid", "Skypine", "Skyrose","Skyspurce", "Skywood", "Soar", "Storm", "Sunbirch", "Sunborn", "Sunbranch", "Sunelm", "Sunfield", "Sunling","Sungarden", "Windgarden", "Sungrove", "Windgrove", "Whirlwind", "Wind", "Windborn", "Windman", "Windson", "Zephyr"]
                #aren't these the same??? v
            AARAKOCRA_FIRSTNAMES_MALE = ["Aera", "Aerag", "Aerk", "Aerka", "Aial", "Aialro", "Aldug", "Aldugek", "Aur", "Aurin","Deekek", "Deelek", "Errk", "Errok", "Heehk", "Helehk", "Ikki", "Ikkit", "Ileak", "Ilek", "Kilco", "Kilcop", "Kleeck", "Kloock", "Lagin", "Lugin", "Oerett", "Oorr", "Ousl", "Oust", "Quaf", "Quet", "Quierk", "Quilet", "Quizik", "Quko", "Rani", "Renzu", "Salleek", "Sazel", "Sejlik", "Sileg", "Unok", "Urreek", "Zeed", "Zelid", "Zelip", "Ziko", "Zygic", "Zylex"]
            AARAKOCRA_FIRSTNAMES_FEMALE = ["Aera", "Aerag", "Aerk", "Aerka", "Aial", "Aialro", "Aldug", "Aldugek", "Aur", "Aurin", "Deekek", "Deelek", "Errk", "Errok", "Heehk", "Helehk", "Ikki", "Ikkit", "Ileak", "Ilek", "Kilco", "Kilcop", "Kleeck", "Kloock", "Lagin", "Lugin", "Oerett", "Oorr", "Ousl", "Oust", "Quaf", "Quet", "Quierk", "Quilet", "Quizik", "Quko", "Rani", "Renzu", "Salleek","Sazel", "Sejlik", "Sileg", "Unok", "Urreek", "Zeed", "Zelid", "Zelip", "Ziko", "Zygic", "Zylex"]
            
            lastName = random.choice(AARAKOCRA_LASTNAMES)

            match sex:
                case "Male": firstName = random.choice(AARAKOCRA_FIRSTNAMES_MALE)
                case "Female": firstName = random.choice(AARAKOCRA_FIRSTNAMES_FEMALE)
                #what is Mtfns?
            
        case "Dragonborn":

            DRAGONBORNS_LASTNAMES = ["Achebe", "Ademola", "Adeoye", "Adesida", "Adesina", "Adeyemi", "Aguda", "Akenzua", "Akerele", "Akiloye", "Akinjide", "Akintola", "Akinyemi", "Akpabio", "Akunyili", "Alakija", "Alamieyeseigha", "Amaechi", "Anenih", "Anikulapokuti", "Asaridokubo", "Attah", "Awolowo", "Ayim", "Azikiwe", "Babangida", "Balewa", "Balogun", "Bamgboshe", "Bankole", "Bello", "Biobaku", "Boro", "Buhari", "Chukwumereije", "Danjuma", "Dimka", "Diya", "Effiong", "Egwu", "Ekwensi", "Eze", "Ezekwesili", "Fagbure", "Falana", "Gbadamosi", "Gowon", "Ibori", "Igbinedion", "Igwe", "Ironsi", "Iweala", "Iwu", "Jaja", "Jakande", "Jang", "Jomogbomo", "Kalejaiye", "Kalu", "Madaki", "Magoro", "Mbadinuju", "Mbanefo", "Ngige", "Nnamani", "Nzeogwu", "Obasanjo", "Obi", "Odili", "Ohakim", "Ojukwu", "Okadigbo", "Okafor", "Okar", "Okeke", "Okereke", "Okilo", "Okiro", "Okonjo", "Okonkwo", "Okorie", "Okotieboh", "Okoye", "Okpara", "Olanrewaju", "Omehia", "Onobanjo", "Onwuatuegwu", "Onwudiwe", "Onyejekwe", "Orji", "Oyenusi", "Oyinlola", "Sarowiwa", "Sekibo", "Solarin", "Soyinka", "Tinibu", "Uba", "Yaradua"]
            DRAGONBORNS_FIRSTNAMES_MALE = ["Abdoul", "Abdkarim", "Abdoulaye", "Aboubacar", "Adama", "Ahmed", "Ali", "Alou", "Baba", "Bakary", "Bouba", "Boubacar", "Boureima", "Celestin", "Cheick", "Dango", "Daniel", "Daouda", "Djeïdy", "Djibril", "Drissa", "Felicien", "Fode", "Ibrahim", "Ibrahima", "Issa", "Jacob", "Karim", "Khadafi", "Konaté", "Lassine", "Louis", "Mahamadou", "Mamadou", "Moctar", "Modibo", "Mohamed", "Moussa", "Naly", "Oumar", "Ousmane", "Salif", "Seydou", "Siaka", "Souleymane", "Soumaila", "Yahirou", "Yaya", "Youba", "Youssouf"]
            DRAGONBORNS_FIRSTNAMES_FEMALE = ["Abibatou", "Agna", "Aicha", "Aiicha", "Aissata", "Anita", "Armande", "Assitan", "Binette", "Bintou", "Chloe", "Christiane", "Deni", "Diahara", "Diarra", "Djello", "Djeneba", "Djenebou", "Djilla", "Estou", "Fanta ", "Fatim", "Fatou", "Kanouta", "Germaine", "Haoua", "Hawa", "Hawam", "Jeanne", "Kadidia", "Kady", "Korotoumou ", "Lea", "Leila", "Mariam", "Mary", "Mathi", "Meryam", "Micheline", "Mounaissa", "Nene", "Oumou", "Oumouba", "Oumouk", "Pauline", "Rama", "Soumba", "Stephanie", "Tall", "Zahra"]

            lastName = random.choice(DRAGONBORNS_LASTNAMES)
            match sex:
                case "Male": firstName = random.choice(DRAGONBORNS_FIRSTNAMES_MALE)
                case "Female": firstName = random.choice(DRAGONBORNS_FIRSTNAMES_FEMALE)
                #WHAT IS Ellns

        case "Dwarf":
            DWARVES_LASTNAMES = ["Amber", "Amethyst", "Anvil", "Blacksmith", "Boulder", "Boulderbreak", "Boulderman", "Boulderson", "Clay", "Cliff", "Coal", "Coalman", "Coalson", "Cobalt", "Cobblestone", "Copper", "Copper", "Darkrock", "Darkstone", "Deeprock" , "Deepstone", "Diamond", "Dirt", "Dune", "Earth", "Earthrock", "Earthstone", "Emerald", "Forge", "Forgeman" , "Forgeson", "Gold", "Goldforge", "Goldhammer", "Goldsmith", "Gravel", "Ground", "Hammer", "Hammerman", "Hammerson" , "Highrock", "Highstone", "Hill", "Hillson", "Hillrock", "Hillstone", "Ingot",  "Iron", "Ironforge", "Ironhammer" , "Ironsmith", "Ironson", "Jade", "Lead", "Marble", "Marblebreak", "Marbleson", "Mesa", "Metal", "Mineral" , "Mineshaft", "Mossrock", "Mosstone", "Mountain", "Mountainrock", "Moutainstone", "Mythril", "Nickel", "Onyx", "Opal", "Ore", "Orichalcum", "Pebble", "Quartz", "Quarry", "Rock", "Rockbreak", "Rockhammer", "Rockman", "Rockson" , "Salt", "Sand", "Sapphire", "Silver", "Silverforge", "Silversmith", "Smith", "Smithson", "Soil", "Steelsmith", "Stone", "Stonebreak", "Stoneman", "Stonesmith", "Stoneson", "Tin", "Topaz", "Tunnel", "Tunnelsmith", "Zicron"]
            DWARVES_FIRSTNAMES_MALE = ["Aaron", "Alexander", "Anton", "Ben", "David", "Elias", "Emil", "Erik", "Fabian", "Felix", "Fynn", "Hannes", "Henry", "Jakob", "Jan", "Jannis", "Jonah", "Jonas", "Jonathan", "Julian", "Karl", "Leo", "Leonard", "Levi", "Liam", "Linus", "Luca", "Luis", "Lukas", "Mads", "Matteo", "Max", "Maximilian", "Mika", "Milan", "Moritz", "Niklas", "Noah", "Oskar", "Paul", "Philipp", "Raphael", "Samuel", "Simon", "Theo","Tim", "Tom", "Vincent", "Yannic", "Leon"]
            DWARVES_FIRSTNAMES_FEMALE = ["Alina", "Amelie", "Anna", "Charlotte", "Clara", "Elena", "Elisa", "Ella", "Emilia", "Emily", "Emma", "Frieda", "Greta", "Hannah", "Helena", "Ida", "Isabella", "Johanna", "Julia", "Lara" , "Laura", "Lea", "Lena", "Leni", "Leonie", "Lia", "Lilly",  "Lina", "Lisa", "Lotta", "Luisa", "Maja", "Maria", "Marie", "Marlene", "Mathilda", "Melina", "Mia", "Mila", "Mira", "Nele", "Nora", "Paula", "Pauline", "Pia", "Sarah", "Sofia", "Sophie", "Viktoria", "Yuna" ]

            lastName = random.choice(DWARVES_LASTNAMES)
            match sex:
                case "Male": firstName = random.choice(DWARVES_FIRSTNAMES_MALE)
                case "Female": firstName = random.choice(DWARVES_FIRSTNAMES_FEMALE)        

        case "Elf":
            ELVES_LASTNAMES = ["Brightbranch", "Brightform", "Brightgarden", "Brightgroove", "Brightmeadow", "Feybirch", "Feyborn", "Feybranch", "Feyelm", "Feyfield", "Feyform", "Feygarden", "Feygrove", "Feylily", "Feyling", "Feyman", "Feymaple", "Feymeadow", "Feyoak", "Feyorchid", "Feypine", "Feyrose", "Feyson", "Feyspurce", "Feywood", "Goldbirch", "Goldbranch", "Goldelm", "Goldfield", "Goldgrove", "Goldlily", "Goldmaple", "Goldoak", "Goldorchid", "Goldpine", "Goldrose", "Goldspurce", "Goldwood", "Silverbirch", "Silverbranch", "Silverelm", "Silverfield", "Silvergarden", "Silvergrove", "Silverlily", "Silvermaple", "Silvermeadow", "Silveroak", "Silverorchid", "Silverpine", "Silverrose", "Silverspurce", "Silverwood", "Skybirch", "Skybranch", "Skyelm", "Skyfield", "Skygarden", "Skygrove", "Skylily", "Skymaple", "Skymeadow", "Skyoak", "Skyorchid", "Skypine", "Skyrose", "Skyspurce", "Skywood", "Starbirch", "Starborn", "Starelm", "Starform", "Stargarden", "Starlily", "Starling", "Starman", "Starmaple", "Starmeadow", "Staroak", "Starorchid", "Starpine", "Starrose", "Starson", "Starspurce", "Starwood", "Sunbirch", "Sunbranch", "Sunelm", "Sunfield", "Sungarden", "Sungrove", "Sunlily", "Sunmaple", "Sunmeadow", "Sunoak", "Sunorchid", "Sunpine", "Sunrose", "Sunspurce", "Sunwood"]
            ELVES_FIRSTNAMES_MALE = ["Francesco", "Alessandro", "Lorenzo", "Andrea", "Leonardo", "Mattia", "Matteo", "Gabriele", "Riccardo", "Tommaso" , "Davide", "Giuseppe", "Antonio", "Federico", "Edoardo", "Marco", "Samuele", "Diego", "Giovanni", "Luca", "Christian", "Pietro", "Simone", "Nicolo", "Filippo", "Alessio", "Gabriel", "Michele", "Emanuele", "Jacopo", "Daniele", "Cristian", "Giacomo", "Vincenzo", "Salvatore", "Manuel", "Gioele", "Thomas", "Stefano", "Giulio", "Samuel", "Nicola", "Giorgio", "Luigi", "Daniel", "Elia", "Angelo", "Domenico", "Paolo", "Raffaele"]
            ELVES_FIRSTNAMES_FEMALE = ["Sofia", "Giulia", "Aurora", "Giorgia", "Martina", "Emma", "Greta", "Chiara", "Sara", "Alice" , "Gaia", "Anna", "Francesca", "Ginevra", "Noemi", "Alessia", "Matilde", "Vittoria", "Viola", "Beatrice", "Nicole", "Giada", "Elisa", "Rebecca", "Elena", "Arianna", "Mia", "Camilla", "Ludovica", "Maria", "Marta", "Melissa", "Bianca", "Gioia", "Asia", "Adele", "Eleonora", "Miriam", "Serena", "Benedetta", "Irene", "Angelica", "Ilaria", "Carlotta", "Caterina", "Margherita", "Alessandra", "Valentina", "Emily", "Laura"]

            lastName = random.choice(ELVES_LASTNAMES)
            match sex:
                case "Male": firstName = random.choice(ELVES_FIRSTNAMES_MALE)
                case "Female": firstName = random.choice(ELVES_FIRSTNAMES_FEMALE)

        case "Genasi":
            GENASI_FIRE_LASTNAMES = ["Flame", "Fire", "Burn", "Furnace", "Ember", "Heat", "Inferno", "Blaze", "Pyre", "Glow", "Sear", "Spark", "Hearth", "Sun", "Lava", "Volcano", "Flare", "Ignite", "Kindle", "Torch", "Light", "Lamp", "Lantern", "Flameborn", "Fireson"]
            GENASI_EARTH_LASTNAMES = ["Amethyst", "Boulder", "Clay", "Coal", "Cobblestone", "Darkboulder", "Darkrock", "Darkstone", "Deeprock", "Deepstone", "Diamond", "Dune", "Earth", "Emerald", "Gravel", "Ground", "Jade", "Mossrock", "Mosstone", "Mountain", "Mountainrock", "Moutainstone", "Opal", "Sapphire", "Stone"]
            GENASI_WATER_LASTNAMES = ["Water", "Ocean", "Sea", "Lake", "Creek", "River", "Stream", "Deepwater", "Rain", "Iceman", "Iceberg", "Tide", "Wave", "Gulf", "Geyser", "Rapid", "Bay", "Brook", "Canal", "Channel", "Cove", "Cape", "Delta", "Estuary", "Harbor"]
            GENASI_AIR_LASTNAMES = ["Air", "Airborn", "Airman", "Breeze", "Cloud", "Current", "Cyclone", "Flow", "Fly", "Gale", "Galeborn", "Galeman", "Glide", "Gust", "Lift", "Sky", "Skyborn", "Soar", "Storm", "Whirlwind", "Wind", "Windborn", "Windman", "Windson", "Zephyr"]
            GENASI_FIRSTNAMES_MALE = ["An", "AnDung", "Bao", "Bay", "Buu", "Ca", "Chien", "Cong", "Cuong", "Danh", "Duc", "Ha", "Hien", "Hieu", "Hieú", "Hoang", "Hung", "Huu", "Huy", "Huynh", "Kim", "Lap", "Le", "Long", "Minh", "Nam", "Nghi", "Nghia", "Ngu", "Nguyen", "Nien", "Phuoc", "Quan", "Quy", "Tai", "Tam", "Teo", "Teo", "Thien", "Tin", "Toan", "Trai", "Trang", "Trong", "Trung", "Truuc", "Tuan", "Van", "Vien", "Viet"]
            GENASI_FIRSTNAMES_FEMALE = ["Am", "Anh", "Be", "Bian", "Ca", "Cai", "Cam", "Chau", "Cuc", "Ha", "Hai", "Hanh", "Hao", "Hoa", "Hòng", "Huong", "Hwa", "Hyunh", "KimCuc", "Kimly", "Lang", "Le", "Lien", "Linh", "Mai", "My", "Ngoc", "Ngocbich", "Ngon", "Nguyen", "Nguyet", "Nhung", "Nu", "Phoung", "Phuong", "Sang", "Tai", "Thanh", "Thao", "Thi", "Thu", "Thuy", "Trang", "Truc", "Tu", "Tuyen", "Tuyet", "Ut", "Xuan", "Yen"]

            match subrace:
                case "Fire Genasi": lastName = random.choice(GENASI_FIRE_LASTNAMES)
                case "Earth Genasi": lastName = random.choice(GENASI_EARTH_LASTNAMES)
                case "Water Genasi": lastName = random.choice(GENASI_WATER_LASTNAMES)
                case "Air Genasi": lastName = random.choice(GENASI_AIR_LASTNAMES)
            match sex:
                case "Male": firstName = random.choice(GENASI_FIRSTNAMES_MALE)
                case "Female": firstName = random.choice(GENASI_FIRSTNAMES_FEMALE)

        case "Gnome":
            GNOMES_LASTNAMES = ["Archer", "Bader", "Bailer", "Bailey", "Baker", "Bannister", "Barber", "Bard", "Barker", "Baxter", "Becker", "Boatman", "Boatwright", "Brewer", "Builder", "Carpenter", "Carter", "Cartwright", "Chaffer", "Chandler", "Chaplin", "Clark", "Cleric", "Cobbler", "Collier", "Cook", "Cookie", "Cooper", "Courier", "Craft", "Decker", "Dempster", "Draper", "Driver", "Dyer", "Farmer", "Fisher", "Fletcher", "Forester", "Foster", "Fowler", "Fuller", "Gage", "Gardener", "Garner", "Glover", "Guard", "Hayward", "Healer", "Hunt", "Hunter", "Judge", "Judge", "Kelner", "Key", "Knight", "Lawman", "Lawson", "Mage", "Mason", "Mayer", "Mercer", "Miller", "Painter", "Palmer", "Parker", "Piper", "Plummer", "Porter", "Potter", "Reeve", "Rhyder", "Sawyer", "Scribe", "Sealer", "Sexton", "Sheppard", "Shipwright", "Slater", "Slaughter", "Smith", "Stringer", "Tamer", "Thatcher", "Tinker", "Todd", "Toller", "Trainer", "Tuner", "Turner", "Wainwright", "Waker", "Walker", "Waller", "Warf", "Webb", "Woodman", "Wright", "Writer", "Zaiger"]
            GNOMES_FIRSTNAMES_MALE = ["Adam",  "Alexander",  "Allen",  "Anderson",  "Bailey",  "Baker",  "Barnes",  "Bell",  "Bennett",  "Brooks", "Aguilar", "Alonso", "Alvarez", "Andres", "Arias", "Blanco", "Bravo", "Caballero", "Cabrera", "Calvo", "Campos", "Cano", "Carmona", "Carrasco", "Castillo", "Castro", "Cortes", "Crespo", "Cruz", "Delgado", "Ibanez", "Iglesias", "Izquierdo", "Jimenez", "Leon", "Lopez", "Lorenzo", "Lozano", "Marcos", "Marin", "Rodriguez", "Roman", "Romero", "Rubio", "Ruiz", "Saez", "Sanchez", "Santos"]
            GNOMES_FIRSTNAMES_FEMALE = ["Abril", "Adriana", "Agustina", "Alejandra", "Amanda", "Ana Sofia", "Andrea", "Antonella", "Antonia", "Ariana", "Bianca", "Camila", "Carolina", "Catalina", "Daniela", "Elena", "Emilia", "Emily", "Emma", "Florencia", "Gabriela", "Guadalupe", "Isabella", "Ivanna", "Juana", "Julieta", "Lucia", "Luciana", "Maite", "Manuela", "María", "Fernanda", "Estefani", "Mariana", "Martina", "Mía", "Natalia", "Nicole", "Paula", "Rafaela", "Regina", "Renata", "Samantha", "Sanz", "Sara", "Serrano", "Sofia", "Soler", "Soto", "Suarez"]

            lastName = random.choice(GNOMES_LASTNAMES)
            match sex:
                case "Male": firstName = random.choice(GNOMES_FIRSTNAMES_MALE)
                case "Female": firstName = random.choice(GNOMES_FIRSTNAMES_FEMALE)

        case "Goliath":
            GOLIATHS_LASTNAMES = ["Aimeilagian", "Aimeilakanu", "Aimeilakiv", "Aimeilathai", "Aimeilathi", "Aimeiliaga", "Aimeiliana", "Aimeiliano", "Aimeillago", "Aimeilolavi", "Anakalagian", "Anakalakanu", "Anakalakiv", "Anakalathai", "Anakalathi", "Anakaliaga", "Anakaliana", "Anakaliano", "Anakallago", "Anakalolavi", "Elaniagian", "Elaniakanu", "Elaniakiv", "Elaniathai", "Elaniathi", "Elaniiaga", "Elaniiana", "Elaniiano", "Elanilago", "Elaniolavi", "Gathakagian", "Gathakakanu", "Gathakakiv", "Gathakathai", "Gathakathi", "Gathakiaga","Gathakiana", "Gathakiano", "Gathaklaga", "Gathakolavi", "Kalagagian", "Kalagakanu", "Kalagakiv", "Kalagathai", "Kalagathi", "Kalagiaga", "Kalagiana", "Kalagiano", "Kalaglaga", "Kalagolavi", "Lithmoragian", "Lithmorakanu", "Lithmorakiv", "Lithmorathai", "Lithmorathi", "Lithmoriaga", "Lithmoriana", "Lithmoriano", "Lithmorlaga", "Lithmorolavi", "Mithagagian", "Mithagakanu", "Mithagakiv", "Mithagathai", "Mithagathi", "Mithagiaga", "Mithagiana", "Mithagiano", "Mithaglaga", "Mithagolavi", "Ogolakagian", "Ogolakakanu", "Ogolakakiv", "Ogolakathai", "Ogolakathi", "Ogolakiaga", "Ogolakiana", "Ogolakiano", "Ogolaklaga", "Ogolakolavi", "Thulagian", "Thulakanu", "Thulakiv", "Thulathai", "Thulathi", "Thuliaga", "Thuliana", "Thuliano", "Thullaga", "Thulolavi", "Zekatuagian", "Zekatuakanu", "Zekatuakiv", "Zekatuathai", "Zekatuathi", "Zekatuiaga", "Zekatuiana", "Zekatuiano", "Zekatulaga", "Zekatuolavi"]
            GOLIATHS_FIRSTNAMES_MALE = ["Aukan", "Aukned", "Belzed", "Bienzo", "Bogdo", "Cenhen", "Delvu", "Dirgag", "Dondid", "Eglath", "Egned", "Fengi", "Fondin", "Fopgun", "Fuldo", "Gaeal", "Ganden", "Gauthak", "Hogfin", "Ilikan", "Jondid", "Keothi", "Kuori", "Lokag", "Lukeg", "Magned", "Manneo", "Maveith", "Nalla", "Orilo", "Orvin", "Paavu", "Padin", "Pethani", "Qubig", "Sarzin", "Shonben", "Shontai", "Thalai", "Thotham", "Uthal", "Vamto", "Vaunea", "Venko", "Ventik", "Vimak", "Wagfor", "Waldu", "Zaxfor", "Zendu"]
            GOLIATHS_FIRSTNAMES_FEMALE = ["Aukan", "Aukned", "Belzed", "Bienzo", "Bogdo", "Cenhen", "Delvu", "Dirgag", "Dondid", "Eglath", "Egned", "Fengi", "Fondin", "Fopgun", "Fuldo", "Gaeal", "Ganden", "Gauthak", "Hogfin", "Ilikan", "Jondid", "Keothi", "Kuori", "Lokag", "Lukeg", "Magned", "Manneo", "Maveith", "Nalla", "Orilo", "Orvin", "Paavu", "Padin", "Pethani", "Qubig", "Sarzin", "Shonben", "Shontai", "Thalai", "Thotham", "Uthal", "Vamto", "Vaunea", "Venko", "Ventik", "Vimak", "Wagfor", "Waldu", "Zaxfor", "Zendu"]

            lastName = random.choice(GOLIATHS_LASTNAMES)
            match sex:
                case "Male": firstName = random.choice(GOLIATHS_FIRSTNAMES_MALE)
                case "Female": firstName = random.choice(GOLIATHS_FIRSTNAMES_FEMALE)

        case "Half-Elf":
            HALF_ELVES_LASTNAMES = ["Skyoak", "Skyrose", "Skybirch", "Skyspurce", "Skypine", "Skyelm", "Skymaple", "Skywood", "Skyorchid","Skylily", "Skygrove", "Skybranch", "Skyfield", "Skymeadow", "Skygarden", "Staroak", "Starrose", "Starbirch","Starspurce", "Starpine", "Starelm", "Starmaple", "Starwood", "Starorchid", "Starlily", "Starmeadow", "Stargarden", "Sungrove","Sunbranch", "Sunfield", "Sunoak", "Sunrose", "Sunbirch", "Sunspurce", "Sunpine", "Sunelm", "Sunmaple", "Sunwood", "Sunorchid","Sunlily", "Sungrove", "Sunbranch", "Sunfield", "Sunmeadow", "Sungarden", "Goldoak", "Goldrose", "Goldbirch","Goldspurce", "Goldpine", "Goldelm", "Goldmaple", "Goldwood", "Goldorchid", "Goldlily", "Goldgrove", "Goldbranch", "Goldfield","Sunmeadow", "Sungarden", "Silveroak", "Silverrose", "Silverbirch", "Silverspurce", "Silverpine", "Silverelm", "Silvermaple","Silverwood", "Silverorchid", "Silverlily", "Silvergrove", "Silverbranch", "Silverfield", "Silvermeadow", "Silvergarden", "Feyoak", "Feyrose","Feybirch", "Feyspurce", "Feypine", "Feyelm", "Feymaple", "Feywood", "Feyorchid", "Feylily", "Feygrove", "Feybranch", "Feyfield", "Feymeadow","Feygarden", "Starborn", "Starman", "Starson", "Starling", "Starform", "Feyborn", "Feyman", "Feyson", "Feyling","Feyform"]
            HALF_ELVES_FIRSTNAMES_MALE = ["George", "Nick", "John", "Kostas", "Stelios", "Alex", "Chris", "Thanos", "konstantinos", "Jim" , "Dimitris", "Christos", "Angelo", "Marios", "Apostolis", "Aris", "Panagiotis", "Manos", "Bill", "Peter", "Giannis", "Alexandros", "Lefteris", "Giorgos", "Andrew", "Alexander", "Steven", "Evangelos", "Billy", "Manolis", "Nicolas", "Gregory", "Pantelis", "Spiros", "Aggelos", "Antonis", "Sotiris", "Con", "Petros", "Constantine", "Alkinoos", "Achilleas", "Vasilhs", "Agim", "Stavros", "Christopher", "Vassilis", "Panos", "Vaggelis", "Michael"]
            HALF_ELVES_FIRSTNAMES_FEMALE = ["Maria", "Katerina", "Anna", "Anastasia", "Christina", "Georgia", "Mary", "Helen", "Dimitra", "Elena", "Irene", "Konstantina", "Alexandra", "Eva", "Marianna", "Sofia", "Eleni", "Christine", "Zoe", "Joanna", "Theodora", "Angela", "Katherine", "Danae", "Catherine", "Nicole", "Olga", "Myrto", "Vasiliki", "Eleftheria", "Kate", "Efi", "Artemis", "Evi", "Fotini", "Agnes", "Loanna", "Nefeli", "Chrysa", "Marina", "Melina", "Sophia", "Stella", "Athina", "Despina", "Rafaela", "Dora", "Giota", "Alice", "Lydia"]

            lastName = random.choice(HALF_ELVES_LASTNAMES)
            match sex:
                case "Male": firstName = random.choice(HALF_ELVES_FIRSTNAMES_MALE)
                case "Female": firstName = random.choice(HALF_ELVES_FIRSTNAMES_FEMALE)

        case "Halfling":
            HALFLINGS_LASTNAMES = ["Aftor", "Alnig", "Argurra", "Barren", "Bregold", "Clearfarm", "Curun", "DeAlnig", "DeCurun", "DeEast", "Deepcoal", "Deepwood", "DeGalle", "DeHibran", "DeNorth", "DePanip", "DeRudra", "DeShore", "DeSkenin", "DeSouth", "DeWest", "DeWillow", "Dwarfgate", "Dwarfland", "Eastbrook", "Eastsea", "Eastshore",  "Eastson", "Elfgate", "Elfland" , "Elfport", "Elvcove", "Everdeep", "Farborn", "Farill", "Farsea", "Farson", "Fincoed", "Firstland", "Forest", "Forestedge", "Galle", "Ghenpoe", "Giantland", "Gnomeland", "Goldshore", "Goldtrust", "Greathill", "Gypte", "Hanan", "Hibran", "Hilltop", "Huland", "Impance", "Irongate", "Ishro", "Moruk", "Mountain", "Movet", "Nickletown" , "Northbrook", "Northsea", "Oakgrove", "Orcland", "Panip", "Pronson", "Ravenshore", "Redcreek", "Rosemeadow", "Rudra" , "Salan", "Seaborn", "Season", "Shipman", "Silvercrown", "Silverwood", "Skenin", "Soland", "Southbrook", "Southsea", "Southson", "Stangate","Stanland", "Steelburg", "Tiefland", "Traveller", "Westbrook", "Westdale", "Westsea", "Westshore", "Westson", "Wheatland", "Willowsbrook", "Wintergate", "Wood", "Woodedge", "Woodland", "Xena", "Yulin", "Zincton"]
            HALFLINGS_FIRSTNAMES_MALE = ["George", "Nick", "John", "Kostas", "Stelios", "Alex", "Chris", "Thanos", "konstantinos", "Jim" , "Dimitris", "Christos", "Angelo", "Marios", "Apostolis", "Aris", "Panagiotis", "Manos", "Bill", "Peter", "Giannis", "Alexandros", "Lefteris", "Giorgos", "Andrew", "Alexander", "Steven", "Evangelos", "Billy", "Manolis", "Nicolas", "Gregory", "Pantelis", "Spiros", "Aggelos", "Antonis", "Sotiris", "Con", "Petros", "Constantine", "Alkinoos", "Achilleas", "Vasilhs", "Agim", "Stavros", "Christopher", "Vassilis", "Panos", "Vaggelis", "Michael"]
            HALFLINGS_FIRSTNAMES_FEMALE = ["Maria", "Katerina", "Anna", "Anastasia", "Christina", "Georgia", "Mary", "Helen", "Dimitra", "Elena", "Irene", "Konstantina", "Alexandra", "Eva", "Marianna", "Sofia", "Eleni", "Christine", "Zoe", "Joanna", "Theodora", "Angela", "Katherine", "Danae", "Catherine", "Nicole", "Olga", "Myrto", "Vasiliki", "Eleftheria", "Kate", "Efi", "Artemis", "Evi", "Fotini", "Agnes", "Loanna", "Nefeli", "Chrysa", "Marina", "Melina", "Sophia", "Stella", "Athina", "Despina", "Rafaela", "Dora", "Giota", "Alice", "Lydia"]

            lastName = random.choice(HALFLINGS_LASTNAMES)
            match sex:
                case "Male": firstName = random.choice(HALFLINGS_FIRSTNAMES_MALE)
                case "Female": firstName = random.choice(HALFLINGS_FIRSTNAMES_FEMALE)

        case "Half-Orc":
            HALF_ORCS_LASTNAMES = ["Emilson",  "Mathiasson",  "Magnusson",  "Jonasson",  "Williamson",  "Oliverson",  "Noahson",  "Adrianson",  "Tobiasson",  "Eliasson", "Danielson",  "Henrikson",  "Sebastianson",  "Lucasson",  "Martinson",  "Andreasson",  "Benjaminson",  "Leonson",  "Sanderson",  "Alexanderson", "Liamson",  "Isakson",  "Jakobson",  "Kristianson",  "Akselson",  "Julianson",  "Fredrikson",  "Sondreson",  "Johannesson",  "Erikson", "Jonathanson",  "Mariusson",  "Filipson",  "Lukasson",  "Sigurdson",  "Markusson",  "Hakonson",  "Eirikson",  "Theoson",  "Oscarson", "Mikkelson",  "Theodorson",  "Davidson",  "Gabrielson",  "Oskarson",  "Kasperson",  "Marcusson",  "Olavson",  "Evenson",  "Hermanson", "Aaronson ",  "Aidenson",  "Alexanderson",  "Andrewson",  "Anthonyson",   "Benjaminson",   "Calebson",   "Carterson",   "Charlesson",   "Christopherson", "Danielson",   "Davidson",   "Dylanson",   "Elijahson",   "Ethanson",  "Gabrielson",   "McGrayson",   "Henryson",   "Isaacson",   "Isaiahson", "Jackson",  "McJackson",   "Jacobson",   "Jamesson",   "McJaxon",   "Jaydenson",   "Johnson",   "Josephson",   "Joshuason",   "Julianson", "Levison",   "Liamson",   "Lincolnson",   "Loganson",   "Lucasson",   "Lukeson",   "McMason",   "Mateoson",   "Matthewson",   "Michaelson", "Nathanson",  "Noahson",   "Oliverson",   "Owenson",   "Ryanson",   "Samuelson",   "Sebastianson",   "Thomasson",   "Williamson",   "Wyattson"]
            HALF_ORCS_FIRSTNAMES_MALE = ["Emil",  "Mathias",  "Magnus",  "Jonas",  "William",  "Oliver",  "Noah",  "Adrian",  "Tobias",  "Elias", "Daniel",  "Henrik",  "Sebastian",  "Lucas",  "Martin",  "Andreas",  "Benjamin",  "Leon",  "Sander",  "Alexander", "Liam",  "Isak",  "Jakob",  "Kristian",  "Aksel",  "Julian",  "Fredrik",  "Sondre",  "Johannes",  "Erik", "Jonathan",  "Marius",  "Filip",  "Lukas",  "Sigurd",  "Markus",  "Hakon",  "Eirik",  "Theo",  "Oscar", "Mikkel",  "Theodor",  "David",  "Gabriel",  "Oskar",  "Kasper",  "Marcus",  "Olav",  "Even",  "Herman"]
            HALF_ORCS_FIRSTNAMES_FEMALE = ["Emma",  "Nora",  "Sofie",  "Thea",  "Ingrid",  "Emilie",  "Mia",  "Julie",  "Anna",  "Ida", "Linnea",  "Amalie",  "Maria",  "Sara",  "Ella",  "Maja",  "Leah",  "Tuva",  "Sofia",  "Frida", "Vilde",  "Mathilde",  "Marie",  "Olivia",  "Jenny",  "Hanna",  "Aurora",  "Elise",  "Malin",  "Victoria", "Oda",  "Selma",  "Hedda",  "Julia",  "Mari",  "Eline",  "Martine",  "Mina",  "Alma",  "Andrea", "Pernille",  "Amanda",  "Mathea",  "Celine",  "Tiril",  "Isabella",  "Sarah",  "Mille",  "Synne",  "Hannah"]

            lastName = random.choice(HALF_ORCS_LASTNAMES)
            match sex:
                case "Male": firstName = random.choice(HALF_ORCS_FIRSTNAMES_MALE)
                case "Female": firstName = random.choice(HALF_ORCS_FIRSTNAMES_FEMALE)

        case "Human":
            HUMANS_LASTNAMES = ["Adams",  "Alexander",  "Allen",  "Anderson",  "Bailey",  "Baker",  "Barnes",  "Bell",  "Bennett",  "Brooks", "Brown",  "Bryant",   "Butler",  "Campbell",  "Carter",  "Clark", "Coleman",  "Collins" , "Cook",  "Cooper" , "Cox", "Davis",  "Diaz",  "Edwards",  "Evans",  "Flores",  "Foster",  "Garcia",  "Gonzales",  "Gonzalez", "Gray",  "Green",  "Griffin",   "Hall",  "Harris",  "Hayes","Henderson",  "Hernandez",  "Hill",  "Howard" , "Hughes",  "Jackson",  "James",  "Jenkins",  "Johnson",  "Jones",  "Kelly",  "King",  "Lee",  "Lewis" , "Long",  "Lopez",  "Martin",  "Martinez",  "Miller",  "Mitchell",  "Moore",  "Morgan",  "Morris",  "Murphy" , "Nelson",  "Parker",  "Patterson",  "Perez",  "Perry",  "Peterson",  "Phillips",  "Powell",  "Price",  "Ramirez", "Reed",  "Richardson",  "Rivera",  "Roberts", "Robinson",  "Rodriguez",  "Rogers", "Ross", "Russell", "Sanchez", "Sanders",  "Scott",  "Simmons",  "Smith",  "Stewart",  "Taylor",  "Thomas",  "Thompson",  "Torres",  "Turner", "Walker",  "Ward",  "Washington",  "Watson",  "White",  "Williams",  "Wilson",  "Wood",  "Wright",  "Young"]
            HUMANS_FIRSTNAMES_MALE = ["Aaron", "Aiden", "Alexander", "Andrew", "Anthony", "Benjamin", "Caleb", "Carter", "Charles", "Christopher", "Daniel", "David", "Dylan", "Elijah", "Ethan", "Gabriel", "Grayson", "Henry", "Isaac", "Isaiah", "Jack", "Jackson", "Jacob", "James", "Jaxon", "Jayden", "John", "Joseph", "Joshua", "Julian", "Levi", "Liam", "Lincoln", "Logan", "Lucas", "Luke", "Mason", "Mateo", "Matthew", "Michael", "Nathan", "Noah", "Oliver", "Owen", "Ryan", "Samuel", "Sebastian", "Thomas", "William", "Wyatt"]
            HUMANS_FIRSTNAMES_FEMALE = ["Abigail", "Addison", "Amelia", "Aria", "Aubrey", "Audrey", "Ava", "Avery", "Bedegraine", "Bella" , "Brooklyn", "Camila", "Charlotte", "Chloe", "Claire", "Eleanor", "Elizabeth", "Ella", "Ellie", "Emily", "Evelyn", "Grace", "Hannah", "Harper", "Hazel", "Isabella", "Layla", "Leah", "Lillian", "Lily", "Luna", "Madison", "Mia", "Mila", "Natalie", "Nora", "Olivia", "Paisley", "Penelope", "Riley", "Savannah", "Scarlett", "Skylar", "Sofia", "Sophia", "Stella", "Victoria", "Violet", "Zoe", "Zoey" ]

            lastName = random.choice(HUMANS_LASTNAMES)
            match sex:
                case "Male": firstName = random.choice(HUMANS_FIRSTNAMES_MALE)
                case "Female": firstName = random.choice(HUMANS_FIRSTNAMES_FEMALE)

        case "Tiefling":
            TIEFLINGS_LASTNAMES = ["Abadi", "Abboud", "Almasi", "Amari", "Antar", "Antoun", "Arian", "Asfour", "Asghar", "Asker", "Aswad", "Aswad", "Atiyeh", "Attia", "Awad", "Ba", "Baba", "Bahar", "Bahar", "Basara", "Baz", "Bishara", "Bitar", "Botros", "Boulos", "Boutros", "Cham", "Dagher", "Daher", "Deeb", "Essa", "Fakhoury", "Ganem", "Ganim", "Gerges", "Ghannam", "Guirguis", "Hadad", "Haddad", "Haik", "Hajjar", "Hakimi", "Halabi", "Hanania", "Handal", "Harb", "Isa", "Issa", "Kalb", "Kanaan", "Kassab", "Kassis", "Kattan","Khouri", "Khoury", "Kouri", "Koury", "Maalouf", "Maloof", "Malouf", "Maroun", "Masih", "Mifsud", "Mikhail", "Moghadam", "Morcos", "Nader", "Nahas", "Naifeh", "Najjar", "Naser", "Nassar", "Nazari", "Quraishi", "Qureshi", "Rahal", "Rahal", "Sabbag", "Sabbagh", "Safar", "Said", "Salib", "Saliba", "Samaha", "Sarraf", "Sayegh", "Seif", "Shadid", "Shalhoub", "Shammas", "Shamon", "Shamoon", "Shammas", "Shamon", "Shamoon", "Shamoun", "Sleiman", "Tahan", "Tannous", "Toma"]
            TIEFLINGS_FIRSTNAMES_MALE = ["Abad", "Ahirm", "Akmen", "Amnon", "Andram", "Astar", "Balam", "Barakas", "Bathin", "Caim", "Chem", "Cimer", "Cressel", "Damakos", "Ekemon", "Euron", "Fenriez", "Forcas", "Habor", "Iados", "Kairon", "Leucis", "Mamnen", "Mantus", "Marbas", "Melech", "Merihim", "Modean", "Mordai", "Mormo", "Morthos", "Nicor", "Nirgel", "Oriax", "Painmon", "Pelaios", "Purson", "Qemuel", "Raam", "Rimmon", "Thamuz", "Therai","Sammal", "Skamos", "Tethren", "Valifar", "Vassago", "Xappan", "Xepar", "Zephan"]
            TIEFLINGS_FIRSTNAMES_FEMALE = ["Akta", "Anakis", "Armara", "Astaro", "Aym", "Azza", "Beleth", "Bryseis", "Bune", "Criella", "Damaia", "Decarabia", "Ea", "Gadreek", "Gomory", "Hecat", "Ishte", "Jezebeth", "Kali", "Kalista", "Kasdeya", "Lerssa", "Lilith", "Makaria", "Manea", "Markosian", "Mastema", "Naamah", "Nemja", "Nija", "Orianna", "Osah", "Phelaia", "Prosperine", "Purah", "Pyra", "Rieta", "Ronobe", "Ronwe", "Seddit", "Seere", "Sekhmet", "Semyaza", "Shava", "Shax", "Sorath", "Uzza", "Vapula", "Vepar", "Verin"]

            lastName = random.choice(TIEFLINGS_LASTNAMES)
            match sex:
                case "Male": firstName = random.choice(TIEFLINGS_FIRSTNAMES_MALE)
                case "Female": firstName = random.choice(TIEFLINGS_FIRSTNAMES_FEMALE)
        
        case _ : 
            print(f"{race} {subrace} {sex}")
            print(f"{type(race)} {type(subrace)} {type(sex)}")
            raise Exception("Unable to match Race")
        
        
    
    
def c_class(auto):
    from DnD_Data import CLASSES
    CLASSES_LIST = [CLASS for CLASS in CLASSES.keys()]

    if auto == True:
        char_class = random.choice(CLASSES_LIST)
        char_subclass = random.choice(CLASSES[char_class])
    else:
        question = "Class? "
        user = present_options_and_pick(CLASSES_LIST)

        if user == 0:
            char_class = random.choice(CLASSES_LIST)
            char_subclass = random.choice(CLASSES[char_class])
            return char_class,char_subclass
        else:
            char_class = CLASSES_LIST[user]
            char_subclass = random.choice(CLASSES[char_class])

    return char_class,char_subclass

        # match user:
        #     case 0:
        #         general_class = random.choice(Classes)
        #         specific_class = random.choice(general_class)
        #         return general_class,specific_class
            

        #     case 1: return "Artificer",random.choice(Artificer)
        #     case 2: return "Barbarian",random.choice(Barbarian)
        #     case 3: return "Bard",random.choice(Bard)
        #     case 4: return "Cleric",random.choice(Cleric)
        #     case 5: return "Druid",random.choice(Druid)
        #     case 6: return "Fighter",random.choice(Fighter)
        #     case 7: return "Monk",random.choice(Monk)
        #     case 8: return "Paladin",random.choice(Paladin)
        #     case 9: return "Ranger",random.choice(Ranger)
        #     case 10: return "Rogue",random.choice(Rogue)
        #     case 11: return "Sorcerer",random.choice(Sorcerer)
        #     case 12: return "Warlock",random.choice(Warlock)
        #     case 13: return "Wizard",random.choice(Wizard)
        #     case _: raise Exception("input not allowed, Please use numbers 0 through 13")

def background(auto):
    #it has a problem with the varients of the backgrounds
    Acolyte = ["Acolyte"]
    Charlatan = ["Charlatan"]
    Criminal = ["Criminal", "Spy (Criminal Variant)"]
    Entertainer = ["Entertainer", "Gladiator (Entertainer Variant)"]
    Folk_Hero = ["Folk_Hero"]
    Guild = ["Guild Artisan","Guild Merchant (Guild Artisan Variant)"]
    Hermit = ["Hermit"]
    Noble = ["Noble", "Knight (Noble Variant)"]
    Outlander = ["Outlander"]
    Sage = ["Sage"]
    Sailor = ["Sailor", "Pirate (Sailor Variant)"]
    Soldier = ["Soldier"]
    Urchin = ["Urchin"]
    Background = [Acolyte, Charlatan, Criminal, Entertainer, Folk_Hero, Guild, Hermit, Noble, Outlander, Sage, Sailor, Soldier, Urchin]

    if auto == True:
        return random.choice(random.choice(Background))
    else:
        print("0 - random")
        print("1 - Acolyte")
        print("2 - Charlatan")
        print("3 - Criminal")
        print("4 - Entertainer")
        print("5 - Folk Hero")
        print("6 - Guild Artisan")
        print("7 - Hermit")
        print("8 - Noble")
        print("9 - Outlander")
        print("10 - Sage")
        print("11 - Sailor")
        print("12 - Soldier")
        print("13 - Urchin")
        user = int(input("Background? "))
        match user:
            case 0: return random.choice(random.choice(Background))
            case 1: return random.choice(Acolyte)
            case 2: return random.choice(Charlatan)
            case 3: return random.choice(Criminal)
            case 4: return random.choice(Entertainer)
            case 5: return random.choice(Folk_Hero)
            case 6: return random.choice(Guild)
            case 7: return random.choice(Hermit)
            case 8: return random.choice(Noble)
            case 9: return random.choice(Outlander)
            case 10: return random.choice(Sage)
            case 11: return random.choice(Sailor)
            case 12: return random.choice(Soldier)
            case 13: return random.choice(Urchin)
            case _: raise Exception("input not allowed, Please use numbers 0 through 13")

def personality(background):
    from DnD_Data import PERSONALITY_TRAITS
    personalities = PERSONALITY_TRAITS[background]
    characterPersonality = {}
    for characteristic in personalities:
        if characteristic != "Trait" and characteristic != "Ideal" and characteristic != "Bond" and characteristic != "Flaw":
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

def gold(BGL=10):
    Gold = BGL
    return Gold

def trinket():
    from DnD_Data import TRINKETS
    Trinket = random.choice(TRINKETS)
    return Trinket

class Character():
    def __init__(self,auto=False) -> None:
        self.sex = get_gender(auto)
        self.race,self.subrace = get_race(auto)
        self.firstName,self.lastName = name(self.race,self.sex,self.subrace)
        self.height,self.weight = HeightAndWeight(self.race,self.subrace)
        self.languages = get_languages(self.race,self.subrace)
        self.fullName = f"{self.firstName} {self.lastName}"
        self.char_class = c_class(auto)
        self.background = background(auto)
        
        self.personality = personality(self.background)
        self.trait = self.personality.pop("Trait")
        self.ideal = self.personality.pop("Ideal")
        self.bond = self.personality.pop("Bond")
        self.flaw = self.personality.pop("Flaw")
        try: self.feature = self.personality
        except: pass #if there is nothing there then it is fine
        
        self.gold = gold()
        self.trinket = trinket()

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
        try: 
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

        except: pass #it means there is nothin there
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