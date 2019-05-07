def least_stations(states, stations):
    final_stations = set()
    while states:
        covered = set()
        best_station = None
        for station, covered_states in stations.items():
            most_uncovered_states = covered_states & states
            if len(most_uncovered_states) > len(covered):
                covered = most_uncovered_states
                best_station = station

        states -= covered
        final_stations.add(best_station)
    return final_stations


some_states = set(['xj', 'xz', 'qh', 'gd', 'gx', 'bj', 'sh', 'gs', 'hlj'])
some_stations = {
    'kone': set(['xj', 'xz', 'qh', 'gs']),
    'ktwo': set(['gd', 'gx', 'sh']),
    'kthree': set(['bj', 'sh']),
    'kfour': set(['hlj', 'bj'])
}
print(least_stations(some_states, some_stations))
