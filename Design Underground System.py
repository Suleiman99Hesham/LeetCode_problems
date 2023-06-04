class UndergroundSystem:

    def __init__(self):
        self.open_trips = {}
        self.trips_avg = {}        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.open_trips[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        starting = self.open_trips.pop(id)
        found = self.trips_avg.get((starting[0], stationName), 0)
        if found != 0:
            avg = (found[0] + (t - starting[1]))
            cnt = found[1] + 1
        else:
            avg = t - starting[1]
            cnt = 1
        self.trips_avg[(starting[0], stationName)] = (avg, cnt) 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.trips_avg.get((startStation, endStation),[0, 1])[0] / self.trips_avg.get((startStation, endStation),[0, 1])[1]

def test(l1: list, l2: list):
    Test = UndergroundSystem()
    for i in range(len(l1)):
        if l1[i] == "checkIn":
            Test.checkIn(l2[i][0], l2[i][1], l2[i][2])
        elif l1[i] == "checkOut":
            Test.checkOut(l2[i][0], l2[i][1], l2[i][2])
        elif l1[i] == "getAverageTime":
            print(Test.getAverageTime(l2[i][0], l2[i][1]))
        
# Test Case
l1 = ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
l2 = [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
test(l1, l2)