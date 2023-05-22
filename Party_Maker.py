from Character_maker_legal import Character

def main() -> None:

    AUTO = True
    party = {}
    for player in range(4):
        party[f"Character{player}"] = Character(AUTO)

    for player in party:
        party[player].present_character_info()

if __name__ == "__main__":
    main()