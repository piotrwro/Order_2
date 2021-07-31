import random
def get_number():
    '''Get number from user
    Try user of proper number
    rtype: int
    return result'''
    while True:
        try:
            result = int(input("Your number: "))
            break
        except ValueError:
            print("Its not e number")
    return result

def get_numbers():
    """Mad list of  6 user numbers
    rtyp: list
    return numbers"""
    numbers = []
    while len(numbers) < 6:
        number = get_number()
        if not number in numbers and 0 < number <= 49:
            numbers.append(number)
    return numbers

def print_numbers(numbers):
    """Print user numbers"""
    print(",".join(str(number) for number in sorted(numbers)))

def random_numbers():
    """Get 6 random number between 1-49"""
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    return numbers[:6]
def lotto():
    """Compare user numbers to ranodm numbers an said how many user hits"""
    main_numbers = get_numbers()
    print("your numbers:")
    print (main_numbers)
    lotto_numbers = random_numbers()
    print("Lotto numbers: ")
    print(lotto_numbers)
    hits = 0
    for number in main_numbers:
        if number in lotto_numbers:
            hits += 1
    print(f"Your hit {hits}{ 'number' if hits==1 else 'numbers'}!")




if __name__ == '__main__':
    print (lotto())









