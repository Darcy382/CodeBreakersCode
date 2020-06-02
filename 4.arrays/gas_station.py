def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    tank = 0
    starting = 0
    for i in range(len(gas)):
        tank += gas[i]
        tank -= cost[i]
        if tank < 0:
            tank = 0
            starting = i + 1
    return starting