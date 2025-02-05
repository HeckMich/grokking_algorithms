states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["reins"] = set(["id", "nv", "ut"])
stations["rzwei"] = set(["id", "wa", "mt"])
stations["rdrei"] = set(["or", "nv", "ca"])
stations["rvier"] = set(["nv", "ut"])
stations["rfuenf"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)

