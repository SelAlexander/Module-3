calls = 0

def count_calls () :

    if count_calls:
        global calls
        calls += 1



def string_info (string) :
    count_calls()
    result = len(string)
    result_up = string.upper()
    result_low = string.lower()
    print(result, result_up, result_low)





def is_contains (string, list_to_serch) :
    count_calls()
    result_string = string.lower()

    for elem in list_to_serch :
        result_list = elem.lower()


    if result_string in result_list :
        print(True)
    elif result_string not in result_list :
        print(False)










string_info('Capybara')

string_info('Armageddon')

is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN

is_contains('cycle', ['recycling', 'cyclic']) # No matches

print(calls)
