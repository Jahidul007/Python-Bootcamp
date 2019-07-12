import logging
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

                                                  
"""

****************
*              *
*              *
*              *
****************



"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('Width and height must need 2 or higher')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)

    print(symbol * width)


boxPrint('*', 10, 4)

# disable logging module

logging.disable(logging.CRITICAL)

logging.debug('Start of program')
def factorial(n):
    logging.debug('start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total = total * i
        logging.debug('i is %s, total is %s' %(i, total))
    return total

print(factorial(7))

logging.debug('End of program')
