def listDivide(numbers, divide = 2):
    divisibleCount = 0
    for everyNum in numbers:
        if everyNum % divide == 0:
            divisibleCount += 1

    return divisibleCount

class ListDividedException(Exception):
    pass

def testListDivide(self):
    try:
        if not listDivide([1, 2, 3, 4, 5]) == 2:
            raise ListDividedException
        if not listDivide([2, 4, 6, 8, 10]) == 5:
            raise ListDividedException
        if not listDivide([30, 54, 63, 98, 100], divide=10) == 2:
            raise ListDividedException
        if not listDivide([]) == 0:
            raise ListDividedException
        if not listDivide([1, 2, 3, 4, 5], divide=1) == 5:
            raise ListDividedException
        print("Pass")
    except ListDividedException:
        print("Exception occurred")

testListDivide('self')