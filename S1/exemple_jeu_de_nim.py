def display_matches(matches):
    print("Allumettes restantes:")
    print(" " + " I " * matches)
    print("")

def main():
    total_matches = 20  # Nombre total d'allumettes
    current_player = 1  # Joueur courant (1 ou 2)

    while total_matches > 0:
        display_matches(total_matches)
        matches_to_take = int(input(f"Joueur {current_player}, choisissez un nombre d'allumettes (1-3): "))
        
        if matches_to_take < 1 or matches_to_take > 3:
            print("Choisissez un nombre d'allumettes valide (1-3).")
            continue
        
        if matches_to_take > total_matches:
            print("Il n'y a pas assez d'allumettes restantes.")
            continue
        
        total_matches -= matches_to_take

        # Changer de joueur
        current_player = 3 - current_player  # Alterner entre 1 et 2

    # Le joueur qui prend la dernière allumette perd
    print(f"Joueur {current_player} a gagné!")

if __name__ == "__main__":
    main()
