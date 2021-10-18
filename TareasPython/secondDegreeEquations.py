import random

def run():
    
    print('')
    print('PROGRAM THAT RESOLVE SECOND DEGREE EQUATIONS')
    print('')
    print('LIKE ax² + bx + c = 0')
    print('')
    
    # Var 'a' can't have value equal to '0'
    a = random.randint(1, 99)
    print('Number a =', a)
    print('')
    b = random.randint(0, 99)
    print('Number b =', b)
    print('')
    c = random.randint(0, 99)
    print('Number c =', c)
    print('')
    
    # This operation its made to know if the equation is REAL or COMPLEX.
    quadratic = ((b**2) - (4*a*c))
    
    # if result from quadratic operation is more than cero its a REAL equation'
    if quadratic > 0:
        
        x1 = (-b + (quadratic **0.5)) / (2*a)
        x2 = (-b - (quadratic **0.5)) / (2*a)
        
        print('x1 =', x1, 'its a REAL equation')
        print('')
        print('x2 =', x2, 'its a REAL equation')
        print('')
        
        print('THE REALRESULTS ARE SAVED IN A PYTHON DICCTIONARY')
        realResult = { 'result1' : x1, 
                   'result2' : x2 }
        print('')
        print(realResult)
        print('')
        
    else:
    # if result from quadratic operation is less than cero its a COMPLEX equation'
        x1 = complex(-b + (quadratic **0.5)) / (2*a)
        x2 = complex(-b - (quadratic **0.5)) / (2*a)
        
        print('x1 =', x1, 'its COMPLEX equation')
        print('')
        print('x2 =', x2, 'its a COMPLEX equation')
        print('')
        
        print('THE COMPLEXRESULTS ARE SAVED IN A PYTHON DICCTIONARY')
        complexResult = { 'result1' : x1, 
                   'result2' : x2 }
        print('')
        print(complexResult)
        print('')
    
if __name__ == '__main__':
    run()