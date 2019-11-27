def checkIfTheyCanDivide(w):
    if w == 2 :
        return False
    if w % 2 == 0:
        return True
    else:
        return False

def main():

    weight = input()
    weight =eval(weight)
    if( checkIfTheyCanDivide(weight)):
        print("Yes")
    else:
        print("No")
main()