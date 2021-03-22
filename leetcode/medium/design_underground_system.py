"""
https://leetcode.com/problems/design-underground-system/
"""


def roundTo5Digits(number: float) -> float:
    return round(number, 5)


class UndergroundSystem:

    def __init__(self):
        self.customers = dict()  # [start, t_start, end, t_end]
        self.stations = dict()  # [total_time, total_customers]

    def checkIn(self, customer_id: int, stationName: str, t: int) -> None:
        self.customers[customer_id] = [stationName, t, stationName, t]

    def checkOut(self, customer_id: int, stationName: str, t: int) -> None:
        self.customers[customer_id][2] = stationName  # end stationName
        self.customers[customer_id][3] = t  # end time
        time_combination = (self.customers[customer_id][1], self.customers[customer_id][3])
        station_combination = (self.customers[customer_id][0], self.customers[customer_id][2])
        if station_combination not in self.stations:
            self.stations[station_combination] = [0, 0]
        self.stations[station_combination][0] += time_combination[1] - time_combination[0]
        self.stations[station_combination][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        station_combination = (startStation, endStation)
        average_time = 0
        if station_combination in self.stations:
            station_details = self.stations.get(station_combination)
            average_time = station_details[0] / station_details[1]
        # print(average_time)
        return average_time


# Your UndergroundSystem object will be instantiated and called as such:
undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
undergroundSystem.getAverageTime("Paradise", "Cambridge")
undergroundSystem.getAverageTime("Leyton", "Waterloo")
undergroundSystem.checkIn(10, "Leyton", 24)
undergroundSystem.getAverageTime("Leyton", "Waterloo")
undergroundSystem.checkOut(10, "Waterloo", 38)
undergroundSystem.getAverageTime("Leyton", "Waterloo")

system2 = UndergroundSystem()
system2.checkIn(10, "Leyton", 3)
system2.checkOut(10, "Paradise", 8)
assert roundTo5Digits(system2.getAverageTime("Leyton", "Paradise")) == 5
system2.checkIn(5, "Leyton", 10)
system2.checkOut(5, "Paradise", 16)
assert roundTo5Digits(system2.getAverageTime("Leyton", "Paradise")) == 5.5
system2.checkIn(2, "Leyton", 21)
system2.checkOut(2, "Paradise", 30)
assert roundTo5Digits(system2.getAverageTime("Leyton", "Paradise")) == 6.66667

"""
Example 1:

Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);
undergroundSystem.checkOut(27, "Waterloo", 20);
undergroundSystem.checkOut(32, "Cambridge", 22);
undergroundSystem.getAverageTime("Paradise", "Cambridge");       // return 14.00000. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.00000
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 12.00000


Example 2:

Input
["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
[[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]

Output
[null,null,null,5.00000,null,null,5.50000,null,null,6.66667]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(10, "Leyton", 3);
undergroundSystem.checkOut(10, "Paradise", 8);
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.00000
undergroundSystem.checkIn(5, "Leyton", 10);
undergroundSystem.checkOut(5, "Paradise", 16);
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.50000
undergroundSystem.checkIn(2, "Leyton", 21);
undergroundSystem.checkOut(2, "Paradise", 30);
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 6.66667
"""
