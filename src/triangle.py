
def triangle(a: int, b: int, c: int):
    if a==b and a==c:
        print('Tasasivuinen!')
    elif a==b or a==c or b==c:
        print('Tasakylkinen!')
    else:
        print('Erikylkinen...')

def userInput():
    s1 = int(input('Pass one side of a triangle: '))
    s2 = int(input('Pass one side of a triangle: '))
    s3 = int(input('Pass one side of a triangle: '))

    triangle(s1,s2,s3)

newTriangle = userInput()
