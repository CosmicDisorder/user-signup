def main():
    valid_email = True
    email = input("Type email here:\n")
    email_error = "yes"
    if not email == '':
        print("doing length test")
        if len(email) < 3 or len(email) > 20:
            email_error = "That is not a valid email"
        print("is valid? " + email_error)

        num_at = 0
        num_dot = 0
        
        print("checking for number of @ and .\n")
        for char in email:
            if char == '@':
                num_at += 1
                print(num_at)
            
            if char == 'num_dot':
                num_dot += 1
                print(num_dot)

            if num_at > 1 or num_dot > 1:
                email_error = "too many @ or ."

            if char == ' ':
                email_error = "email contains spaces"

        print("is valid? " + email_error)
        print("checking for order of @ then .")
        if num_at != 1 and num_dot != 1:
            email_error = "wrong numer of @ and ."
        else:
            char_position = 0
            characters_since_at = 0
            at_exists = False
            characters_since_dot = 0
            dot_exists = False
            for i in email:
                if at_exists:
                    characters_since_at += 1
                if dot_exists:
                    characters_since_dot += 1
                if i == '@':
                    at_exists = True
                if i == '.':
                    dot_exists = True
                if dot_exists and at_exists:
                    if characters_since_at < 2:
                        email_error = "That is not a valid email"
                if i == '.' and char_position == len(email):
                    email_error = "That is not a valid email"
                char_position += 1
    print("is valid? " + email_error)
if __name__ == "__main__":
    main()