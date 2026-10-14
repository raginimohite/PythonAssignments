import math


def MarvellousEucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 +(P1['Y'] - P2['Y'])**2)
    return Ans


def MarvellousKNNClassifier():

    border = "-" * 30

    Data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'}
    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    for i in Data:
        print(i)

    print(border)

    x = int(input("Enter X coordinate: "))
    y = int(input("Enter Y coordinate: "))

    new_point = {'X': x, 'Y': y}

    print("Distances of all points :")
    print(border)

    for d in Data:
        d['distance'] = MarvellousEucDistance(d, new_point)

    for d in Data:
        print(d)

    print(border)

    sorted_data = sorted(
        Data,
        key=lambda item: item['distance']
    )

    print("Sorted Data :")
    print(border)

    for d in sorted_data:
        print(d)

    print(border)

    k = 3

    nearest = sorted_data[:k]

    print("Nearest 3 members are :")
    print(border)

    for d in nearest:
        print(d)

    print(border)

    # Voting
    votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label, 0) + 1

    print("Voting result is :")
    print(border)

    for label in votes:
        print("Name :", label, " Number of votes :", votes[label])

    print(border)

    iMax = 0
    Name = ""

    for label in votes:
        if votes[label] > iMax:
            iMax = votes[label]
            Name = label

    print("Final prediction is :", Name)


def main():
    MarvellousKNNClassifier()

if __name__ == "__main__":
    main()





