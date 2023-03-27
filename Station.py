class Station:
    """
    Class representing a bike-sharing station
    """

    def __init__(self, station_data: dict):
        self.number = station_data["number"]
        self.contract_name = station_data["contractName"]
        self.name = station_data["name"]
        self.address = station_data["address"]
        self.latitude = station_data["position"]["latitude"]
        self.longitude = station_data["position"]["longitude"]
        self.banking = station_data["banking"]
        self.bonus = station_data["bonus"]
        self.status = station_data["status"]
        self.last_update = station_data["lastUpdate"]
        self.connected = station_data["connected"]
        self.overflow = station_data["overflow"]
        self.shape = station_data["shape"]
        self.total_capacity = station_data["totalStands"]["capacity"]
        self.main_capacity = station_data["mainStands"]["capacity"]
        self.overflow_capacity = station_data["overflowStands"]["capacity"] if station_data["overflowStands"] else None
        self.available_bikes = station_data["totalStands"]["availabilities"]["bikes"]
        self.available_bike_stands = station_data["totalStands"]["availabilities"]["stands"]
        self.available_mechanical_bikes = station_data["totalStands"]["availabilities"]["mechanicalBikes"]
        self.available_electrical_bikes = station_data["totalStands"]["availabilities"]["electricalBikes"]
        self.available_internal_battery_bikes = station_data["totalStands"]["availabilities"]["electricalInternalBatteryBikes"]
        self.available_removable_battery_bikes = station_data["totalStands"]["availabilities"]["electricalRemovableBatteryBikes"]

    def __str__(self):
        return f"Station {self.name} ({self.number}) - {self.address} ({self.contract_name}): {self.available_bikes}/{self.total_capacity} bikes available"



    