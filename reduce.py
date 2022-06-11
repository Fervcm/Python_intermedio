from cgi import print_environ
from functools import reduce
from signal import alarm

def run():
    
    
    """Multiplica todos lo datos de la lista con lambda reduce"""

    my_list = [2, 2, 2, 2, 2]
    
    all_multiplied = reduce(lambda a, b: a * b, my_list)
    
    print(all_multiplied)
    
if __name__ == "__main__":
    run()