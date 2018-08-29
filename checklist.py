checklist = list()
passed = 0
failed = 0


def create(item):
    checklist.append(item)


def read(index):
    index = int(index)
    item = checklist[index]
    return item


def update(index, item):
    index = int(index)
    checklist[index] = item


def destroy(index):
    index = int(index)
    checklist.pop(index)


def mark_completed(index):
    index = int(index)
    update(index, "{}{}".format('√', checklist[index]))


def list_items(start=0, end=-1):
    return_list = list()
    index = 0
    for list_item in checklist:
        if index >= start:
            return_list.append(list_item)

        if index == end:
            break
        else:
            index += 1
    return return_list


def user_input(prompt):
    user_input = input(prompt)
    return user_input


def select(function_code):
    function_code = function_code.lower()

    if function_code == "create" or function_code == "c":
        input_item = user_input("Input item: ")
        if input_item:
            create(input_item)
            
            new_item = True
            print("(Leave blank to confirm.)")
            while new_item:
                input_item = user_input("Input another item: ")
                if input_item:
                    create(input_item)
                else:
                    new_item = False

    elif function_code == "delete" or function_code == "dl":
        item_index = user_input("Delete item index: ")
        destroy(item_index)

    elif function_code == "get" or function_code == "g":
        item_index = user_input("Get item index: ")
        read(item_index)

    elif function_code == "mark" or function_code == "m":
        item_index = user_input("Mark item index: ")
        mark_completed(item_index)

    elif function_code == "display" or function_code == "d":
        print(list_items())

    elif function_code == "quit" or function_code == "q":
        return False

    elif function_code == "test" or function_code == "t":
        test()

    elif function_code == "help" or function_code == "h":
        print("    c | create  - adds item to list.")
        print("   dl | delete  - deletes an item.")
        print("    g | get     - reads a specific item.")
        print("    m | mark    - marks an item as complete.")
        print("    d | display - displays list.")
        print("    t | test    - tests the program.")
        print("    q | quit    - exits program.")

    else:
        print("Unknown Option, use 'help' for a list of commands.")

    return True


# MAIN LOOP -----------------------------------------

running = True
while running:
    selection = user_input(
        "Enter command: ")
    running = select(selection)


# TESTS ---------------------------------------------


def check_test(res, exp, msg):
    global passed
    global failed
    if res == exp:
        passed += 1
        print('passed {}'.format(msg))
    else:
        failed += 1
        print('!failed {}!'.format(msg))
    print('----------------')


def test():
    global checklist
    checklist = list()
    print('initializing list...')
    check_test(checklist, [], 'initialization')

    print('adding 2 items...')
    create('hi')
    create('ho')
    check_test(checklist, ['hi', 'ho'], 'adding items')

    print('reading single item...')
    reading = read(1)
    check_test(reading, 'ho', 'reading item')

    print('updating item...')
    update(1, 'hey')
    check_test(checklist, ['hi', 'hey'], 'updating item')

    print('destroying item...')
    destroy(1)
    check_test(checklist, ['hi'], 'destroying item')

    print('marking complete...')
    checklist = ['a chore', 'another chore']
    mark_completed(1)
    check_test(checklist, ['a chore', '√another chore'], 'marking complete')

    print('listing items...')
    checklist = ['what', 'the', 'balls', 'this',
                 'is', 'making', 'a', 'ton', 'of', 'sense']
    gotten_list = list_items()
    check_test(gotten_list, checklist, 'listing items no args')
    gotten_list = list_items(1, 5)
    check_test(gotten_list, ['the', 'balls', 'this',
                             'is', 'making'], 'listing items with args')

    print('test finished')
    print('passed: {}'.format(passed))
    print('failed: {}'.format(failed))
