import math

def MarvellousEucDistance(P1,P2):
    Ans = ((P1['StudyHours']-P2['StudyHours']**2 + P1['Attendance']-P2['Attendance']**2 ))
    return Ans

def MarvellousKNNClassifier():
    border = "__"*40

    Data = [
        {'StudyHours':2,'Attendance':60,'Result':'Fail'},
        {'StudyHours':5,'Attendance':80,'Result':'Pass'},
        {'StudyHours':6,'Attendance':85,'Result':'Pass'},
        {'StudyHours':1,'Attendance':50,'Result':'Fail'}
    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    print("Dataset is")

    for d in Data:
        print(d)

    print(border)

    #Accept input from user
    study_hours = int(input("Enter study hours:"))
    attendance = int(input("Enter Attendance percentage:"))

    new_students ={'StudyHours':study_hours,'Attendance':attendance}

    print(border)
    print("Distance of all students:")
    print(border)

    #Calculate Distance
    for d in Data:
        d['distance'] = MarvellousEucDistance(d,new_students)

    for d in Data:
        print(d)

    print(border)

    #Sorted Data

    sorted_data = sorted(Data,key = lambda item:item['distance'])

    print("sorted data")
    print(border)

    for d in sorted_data:
        print(d)

    print(border)

    #Select k nearest neighbours 

    k = 3

    nearest = sorted_data[:k]

    print("nearest 3 students are:")
    print(border)

    for d in nearest:
        print(d)

    print(border)

    #Voting
    votes = {}

    for neighbours in nearest:
        result = neighbours['Result']

    votes[result] = votes.get(result,0) + 1

    print("Voting result is")
    print(border)

    for result in votes:
        print("Result:",result,"Number of votes:",votes[result])

    print(border)

    #Find Maximum votes
    iMax = 0
    Name = ""

    for result in votes:
        if votes[result] > iMax:
            iMax = votes[result]
            Name = result

    print("Predicted Result :",Name)

def main():
    MarvellousKNNClassifier()

if __name__ == "__main__":
    main()




