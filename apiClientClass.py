import requests
import json
from typing import List, Dict
from operator import itemgetter
from Station import Station


class apiClientClass:
    """
    Classe pour interagir avec l'API de partage de vélos JCDecaux
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.jcdecaux.com/vls/v3"

    def _make_request(self, endpoint: str, params: dict = None) -> dict:
        """
        Méthode interne pour effectuer une requête à l'API JCDecaux
        """
        if not params:
            params = {}
        params["apiKey"] = self.api_key

        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Une erreur s'est produite lors de la requête : {e}")
            return None

        return json.loads(response.content)

    def get_contracts(self) -> List[str]:
        """
        Récupérer la liste des contrats disponibles
        """
        contracts_data = self._make_request("contracts")
        if contracts_data is None:
            print("Impossible de récupérer les contrats.")
            return []
        return [c["name"] for c in contracts_data]

    def get_stations(self, contract_name: str) -> List[Station]:
        """
        Récupérer la liste des stations pour un contrat donné
        """
        stations_data = self._make_request("stations", params={"contract": contract_name})
        stations = [Station(s) for s in stations_data]  
        return stations

    def get_bike_types_by_city(self, contract_name: str) -> Dict[str, Dict[str, float]]:
        """
        Récupérer le pourcentage de vélos mécaniques et électriques dans les villes pour un contrat donné
        """
        stations = self.get_stations(contract_name)
        if not stations:
            print("Impossible de récupérer les types de vélos par ville.")
            return {}        
        bike_types_by_city = {}

        for station in stations:
            if station.name not in bike_types_by_city:
                bike_types_by_city[station.name] = {"mechanical": 0, "electrical": 0}
            bike_types_by_city[station.name]["mechanical"] += station.available_mechanical_bikes
            bike_types_by_city[station.name]["electrical"] += station.available_electrical_bikes

        total_bikes_by_city = {}
        for station in stations:
            if station.name not in total_bikes_by_city:
                total_bikes_by_city[station.name] = 0
            total_bikes_by_city[station.name] += station.available_bikes

        for city in bike_types_by_city:
            for bike_type in bike_types_by_city[city]:
                if total_bikes_by_city[city] != 0:
                    bike_types_by_city[city][bike_type] /= total_bikes_by_city[city]
                else:
                    bike_types_by_city[city][bike_type] = 0

        return bike_types_by_city

    def get_city_ranking_by_bikes(self, contract_name: str) -> Dict[str, int]:
        """
        Récupérer le classement des villes avec le plus grand nombre de vélos pour un contrat donné
        """
        stations = self.get_stations(contract_name)
        if not stations:
            print("Impossible de récupérer le classement des villes par vélos.")
            return {}
        bikes_by_city = {}
        for station in stations:
            if station.name not in bikes_by_city:
                bikes_by_city[station.name] = 0
            bikes_by_city[station.name] += station.available_bikes

        sorted_cities = sorted(bikes_by_city.items(), key=itemgetter(1), reverse=True)

        city_ranking = {}
        for i, (city, num_bikes) in enumerate(sorted_cities):
            city_ranking[city] = i + 1

        return city_ranking

    def get_stations_with_banking(self, contract_name: str) -> List[Station]:
        """
        Récupérer la liste des stations avec des installations bancaires pour un contrat donné
        """
        stations = self.get_stations(contract_name)
        return [station for station in stations if station.banking]

    def get_stations_with_bonus(self, contract_name: str) -> List[Station]:
        """
        Récupérer la liste des stations avec des points bonus pour un contrat donné
        """
        stations = self.get_stations(contract_name)
        return [station for station in stations if station.bonus]

