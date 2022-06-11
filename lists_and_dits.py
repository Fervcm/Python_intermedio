from multiprocessing import Value


def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Fernando', 'lastname': 'Vacca'}
    
    super_list = [
        {'firstname': 'Fernando', 'lastname': 'Vacca'},
        {'firstname': 'Natalia', 'lastname': 'Vacca'},
        {'firstname': 'Liliana', 'lastname': 'Gomez'},
        {'firstname': 'Sneider', 'lastname': 'Roble'}
    ]

    super_dict= {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43]
    }
     
    for key, value in super_list.items():
       print(key, '-', value)
        
    # for value in super_list:
    #     print(value)
        
        
if __name__ == '__main__':
    run()