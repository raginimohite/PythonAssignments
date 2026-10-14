import math


def MarvellousEucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 +(P1['Y'] - P2['Y'])**2)
    return Ans


def MarvellousKNNClassifier(Data, new_point, k):

    # Calculate distance
    for d in Data:
        d['distance'] = MarvellousEucDistance(d, new_point)

    # Sort according to distance
    sorted_data = sorted(Data,key=lambda item: item['distance'])

    # Select nearest K points
    nearest = sorted_data[:k]

    # Voting
    votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label, 0) + 1

    # Find maximum votes
    iMax = 0
    Name = ""

    for label in votes:
        if votes[label] > iMax:
            iMax = votes[label]
            Name = label

    return Name


def main():

    Data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'}
    ]

    new_point = {'X': 2, 'Y': 2}

    print("------------------------------")
    print("Marvellous KNN Classifier")
    print("------------------------------")

    print("New Point :", new_point)
    print()

    for k in [1, 3, 5]:

        # K should not be greater than dataset size
        actual_k = min(k, len(Data))

        result = MarvellousKNNClassifier(Data,new_point,actual_k)

        print("K =", k, "->", result)

if __name__ == "__main__":
    main()


