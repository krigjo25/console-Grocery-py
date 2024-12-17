def main():
    
    #   initializing a dictionary called items
    items = {}
    
    while True:

        #   Prompting the user to input, case-insensitively
        prompt = str(input("Input a string: ")).upper()

        try:
            if prompt == "":
                raise EOFError("Quiting the program")

            if prompt.isdigit():
                raise Exception("Usage <item> not <number>")
                        
        except EOFError: break
        except Exception as e: print(e)

        #   Ensure the item is already inside the dictionary
        items[f'{prompt}'] = items[f'{prompt}']+1 if prompt in items else 1

    #   Sort the dictionary
    items = dict(sorted(items.items()))

    for key, value in items.items():
        print(f"{value} x {key}")


if __name__ == '__main__':
    main()