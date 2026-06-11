while True:
    filename = input(f'Enter your file name :- ')
    try:
        with open(filename, "r") as file:
            amount = int(file.read().strip())
            print(amount * .5)
            break

    except FileNotFoundError:
        print(f'File is mising bro...')
    
    except ValueError:
        print(f'data is corrupted in file.')
