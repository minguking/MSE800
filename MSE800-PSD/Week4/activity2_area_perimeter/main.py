from rectangle import Rectangle

def get_user_input(text):
    while True:
        try:
            raw = input(text)
            if raw.strip().lower() == 'q':
                return 'q'
            user_input = float(raw)
            if user_input <= 0:
                print("Input must be a positive number. Please try again.")
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return user_input

def main():
    while True:
        print("=== Measurement Calculator ===")
        width = get_user_input('Enter width (or type "q" to quit): ')
        if width == 'q':
            print("======== BYE! ========\n")
            break

        length = get_user_input('Enter length (or type "q" to quit): ')
        if length == 'q':
            print("======== BYE! ========\n")
            break
        
        rect = Rectangle(width, length)
        rect.display()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\n======== BYE! ========\n\n")
    except Exception as e:
        print(f"An error occurred: {e}")