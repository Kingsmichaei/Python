
Studentgrade = {"Ade": 40, "Tola": 60, "Shade": 50, "Yinka": 70}

failedResult = {}
passedResult = {}
result = {}

def checkGrade():
    for key, value in Studentgrade.items():
        if value < 50:
            failedResult.update({key: 'failed'})
            result.update({key: 'failed'})
        elif value >= 50:
            passedResult.update({key: 'passed'})
            result.update({key: 'passed'})
    print(result)
    print(passedResult)
    print(failedResult)
    return result

checked = checkGrade(Studentgrade)