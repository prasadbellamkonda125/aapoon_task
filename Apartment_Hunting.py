"""Apartment Hunting"""

def search_new_block(blocks, requirements):
    maxDistance = [0] * len(blocks)
    for i in range(len(blocks)):
        for req in requirements:
            closestReqDistance = float('inf')
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, abs(i - j))
            maxDistance[i] = max(maxDistance[i], closestReqDistance)
    return getIndexAtMinValue(maxDistance)


def getIndexAtMinValue(arr):
    return min(range(len(arr)), key=arr.__getitem__)


blocks = [
    {
        "gym": False,
        "school": True,
        "store": False,
    },
    {
        "gym": True,
        "school": False,
        "store": False,
    },
    {
        "gym": True,
        "school": True,
        "store": False,
    },
    {
        "gym": False,
        "school": True,
        "store": False,
    },
    {
        "gym": False,
        "school": True,
        "store": True,
    },
]

requirements = ["gym", "school", "store"]
print(search_new_block(blocks, requirements))
