def get_switcher(arg):
    switcher = {
        0: 'India',
        1: 'UK',
        2: 'US'
    }

    return switcher.get(arg, 'No matches found!!')


print(get_switcher(1))
