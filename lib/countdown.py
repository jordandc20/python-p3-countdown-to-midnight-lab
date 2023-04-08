def countdown(integer):
    number=integer
    while number >0:
        print( f'{number} SECOND(S)!')
        number-=1
    print('HAPPY NEW YEAR!')

import time    
def countdown_with_sleep(integer):
    number=integer
    while number >0:
        print( f'{number} SECOND(S)!')
        number-=1
        time.sleep(1)
    print('HAPPY NEW YEAR!')    
    
countdown(15)