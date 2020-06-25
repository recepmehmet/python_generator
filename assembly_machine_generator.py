def _pop(array):
    del array[len(array) -1]

def _addition(array):
    if len(array) <= 1:
        print("Please, firstly enter a number")
        yield array

    total = array[len(array) - 1] + array[len(array) - 2]
    _pop(array)
    _pop(array)
    array.append(total)
    yield array

def _substraction(array):
    if len(array) <= 1:
        print("Please, firstly enter a number")
        yield array

    total = array[len(array) - 1] - array[len(array) - 2]
    _pop(array)
    _pop(array)
    array.append(total)
    yield array

def _division(array):
    if len(array) <= 1:
        print("Please, firstly enter a number")
        yield array

    if array[len(array) - 2] == 0:
        print("Denominator cannot be zero '0' ")
        yield array

    total = array[len(array) - 1] / array[len(array) - 2]
    _pop(array)
    _pop(array)
    array.append(total)
    yield array

def _multiplication(array):
    if len(array) <= 1:
        print("Please, firstly enter a number")
        yield array

    total = array[len(array) - 1] * array[len(array) - 2]
    _pop(array)
    _pop(array)
    array.append(total)
    yield array

def _exponential(array):
    if len(array) <= 1:
        print("Please, firstly enter a number")
        yield array

    total = array[len(array) - 1] ** array[len(array) - 2]
    _pop(array)
    _pop(array)
    array.append(total)
    yield array

def _push(input_numbers_array,number):
    yield input_numbers_array.append(number)

def _increaase(input_numbers_array):
    if len(input_numbers_array) <= 1:
        print("Please, firstly enter a number")
        yield input_numbers_array

    decreased_number = input_numbers_array[len(input_numbers_array) - 1] + 1
    input_numbers_array.pop()
    input_numbers_array.append(decreased_number)
    yield input_numbers_array

def _decrease(input_numbers_array):
    if len(input_numbers_array) <= 1:
        print("Please, firstly enter a number")
        yield input_numbers_array

    decreased_number = input_numbers_array[len(input_numbers_array) - 1] - 1
    print(decreased_number)
    input_numbers_array.pop()
    input_numbers_array.append(decreased_number)
    yield input_numbers_array

def _duplicate(input_numbers_array):
    if len(input_numbers_array) <= 1:
        print("Please, firstly enter a number")
        yield input_numbers_array
    copied_list = input_numbers_array
    for element_number in range(len(copied_list)):
        input_numbers_array.append(copied_list[element_number])

    yield input_numbers_array

def is_number(_string):
    if _string.isnumeric():
        yield float(_string)
    else:
        while(156578451684156348): # as you think heheh
            number = input("Number : ")
            if number.isnumeric():
                yield float(number)

def is_number_range_array(_string, range, array):
    if _string.isnumeric():
        yield float(_string)
    else:
        while (156578451684156348):  # as you think heheh
            number = input("Number : ")
            if number.isnumeric() and range <= len(array):
                yield float(number)

def _jump(function_input_number_keeper, past_commands, list_of_funtions, jump_range):
    input_functional_number = 0
    _pop(past_commands)
    if jump_range > len(past_commands):
        print("You don't have {} command history".format(jump_range))
        number = input("Number : ")
        is_number_range_array(number)

    for command_index in range(len(past_commands) - int(jump_range), len(past_commands)):
        text_splited_elements = past_commands[command_index].split(" ")
        function_command = text_splited_elements[0]

        if len(text_splited_elements) != 1:
            input_functional_number = next(is_number(text_splited_elements[1]))

        command_functions(function_input_number_keeper, function_command, list_of_funtions, input_functional_number )
    yield function_input_number_keeper


def command_functions(function_input_number_keeper, function_command, list_of_funtions, input_functional_number):
    if function_command == list_of_funtions[0]:  # ADD
        next(_addition(function_input_number_keeper))

    elif function_command == list_of_funtions[1]:  # SUB
        next(_substraction(function_input_number_keeper))

    elif function_command == list_of_funtions[2]:  # MUL
        next(_multiplication(function_input_number_keeper))

    elif function_command == list_of_funtions[3]:  # DIV
        next(_division(function_input_number_keeper))

    elif function_command == list_of_funtions[4]:  # EXP
        next(_exponential(function_input_number_keeper))

    elif function_command == list_of_funtions[5]:  # INCR
        next(_increaase(function_input_number_keeper))

    elif function_command == list_of_funtions[6]:  # DECR
        next(_decrease(function_input_number_keeper))

    elif function_command == list_of_funtions[7]:  # PUSH
        next(_push(function_input_number_keeper, input_functional_number))

    elif function_command == list_of_funtions[9]:  # DUP
        next(_duplicate(function_input_number_keeper))

    elif function_command == list_of_funtions[10]:  # JMP
        next(_jump(function_input_number_keeper, past_commands, list_of_funtions, input_functional_number))

    elif function_command == list_of_funtions[8]:  # POP
        print(function_input_number_keeper[len(function_input_number_keeper) - 1])
        function_input_number_keeper.clear()

    elif function_command == list_of_funtions[11]:
        print(function_input_number_keeper)

    else:
        print("Pleas, enter proper input")

function_input_number_keeper = []
past_commands = []
list_of_funtions = ["ADD", "SUB", "MUL", "DIV", "EXP", "INCR", "DECR", "PUSH", "POP", "DUP", "JMP", "SHW"]
print("You have these commands : {}".format(list_of_funtions))

while(12315484984613112548): #This is just for ipnelik. It means True. No any meaning
    input_text = input(" -> ")
    past_commands.append(input_text)
    text_splited_elements = input_text.split(" ")
    function_command = text_splited_elements[0]

    if len(text_splited_elements) != 1:
        input_functional_number = next(is_number(text_splited_elements[1]))

    command_functions(function_input_number_keeper, function_command, list_of_funtions, input_functional_number)