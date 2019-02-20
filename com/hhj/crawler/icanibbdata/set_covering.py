states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
stations["kone"] = set(["id", "nv", "ut"])


final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        print("in loop -- covered:", covered)
        print("in loop -- states_covered:", states_covered)
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
            print("in if -- best_station:", best_station, ", states_covered:", states_covered)

    states_needed -= states_covered
    final_stations.add(best_station)
    print("out loop -- states_needed:", states_needed, ", final_stations:", final_stations)
    print("----------------------------------")

print(final_stations)
