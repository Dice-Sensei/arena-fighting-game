def request_number_input(input_text, min_number, max_number):
    while True:
        number_input = input(f"{input_text} ")

        try:
            number = int(number_input)

            if number < min_number or number > max_number:
                print(
                    f"Number must be in between {min_number} and {max_number} (included)!"
                )
                continue

            return number
        except ValueError:
            print("Provided input must be a number!")
