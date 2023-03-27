from typing import List, Dict
from operator import itemgetter
import sys
from apiClientClass import apiClientClass


def main_menu(client):
    contracts = client.get_contracts()
    print("\nContrats disponibles :")
    for i, contract in enumerate(contracts, 1):
        print(f"{i}. {contract}")
    print(f"{len(contracts) + 1}. Quitter")

    try:
        choice = int(input("\nSélectionnez un numéro de contrat pour afficher plus d'informations ou quitter : "))
        if choice <= len(contracts):
            selected_contract = contracts[choice - 1]
            while True:
                print(f"\nInformations pour {selected_contract} :")
                print("1. Lister toutes les stations")
                print("2. Classement des villes par nombre de vélos")
                print("3. Pourcentage de vélos mécaniques vs électriques par ville")
                print("4. Stations avec installations bancaires")
                print("5. Stations avec points bonus")
                print("6. Retour au menu principal")
                sub_choice = int(input("\nSélectionnez une option : "))

                if sub_choice == 1:
                    stations = client.get_stations(selected_contract)
                    print("\nListe de toutes les stations :")
                    for station in stations:
                        print(station)
                elif sub_choice == 2:
                    city_ranking = client.get_city_ranking_by_bikes(selected_contract)
                    print("\nClassement des villes par nombre de vélos :")
                    for city, rank in city_ranking.items():
                        print(f"{city}: {rank}")
                elif sub_choice == 3:
                    bike_types_by_city = client.get_bike_types_by_city(selected_contract)
                    print("\nPourcentage de vélos mécaniques vs électriques par ville :")
                    for city, bike_types in bike_types_by_city.items():
                        mechanical_percentage = bike_types['mechanical'] * 100
                        electrical_percentage = bike_types['electrical'] * 100
                        print(f"{city}: {mechanical_percentage:.2f}% mécanique, {electrical_percentage:.2f}% électrique")
                elif sub_choice == 4:
                    banking_stations = client.get_stations_with_banking(selected_contract)
                    print("\nStations avec installations bancaires :")
                    for station in banking_stations:
                        print(station)
                elif sub_choice == 5:
                    bonus_stations = client.get_stations_with_bonus(selected_contract)
                    print("\nStations avec points bonus :")
                    for station in bonus_stations:
                        print(station)
                elif sub_choice == 6:
                    break
                else:
                    print("\nChoix invalide. Veuillez réessayer.")
        elif choice == len(contracts) + 1:
            sys.exit(0)
        else:
            print("\nChoix invalide. Veuillez réessayer.")
    except ValueError:
        print("\nErreur : veuillez entrer un nombre valide.")
        return


# Exemple d'utilisation
def main():
    api_key = "e0a1bf2c844edb9084efc764c089dd748676cc14"
    client = apiClientClass(api_key)

    while True:
        main_menu(client)


if __name__ == "__main__":
    main()
