import math

# Main function
def main():
    print("=== CREDIT CARD VALIDATOR ===")
    while True:
        try:
            # Prompting the user
            number = int(input("Enter your credit card number: "))
            break
        # Handle non numeric input
        except ValueError:
            print("Please, enter an integer!\n")

    card_type = verify_card(number)
    print(f"Your card is {card_type}")
    exit()


# The "len" function counts the number of digits in an integer
def len(num):
    return math.floor(math.log10(abs(num)) + 1)


# The "verify_luhn_algo" function verifies if the credit card number is syntactically valid
def verify_luhn_algo(num):
    sum = 0
    temp_num = num // 10

    # Multiply every other digit * 2, and summing the resulting digits
    while temp_num > 0:
        doubled_number = temp_num % 10 * 2
        first_digit = doubled_number
        second_digit = 0

        if doubled_number > 9:
            first_digit = doubled_number // 10
            second_digit = doubled_number % 10
            sum += second_digit

        sum += first_digit
        temp_num //= 100

    temp_num = num

    # Sum the remaining digits
    while temp_num > 0:
        sum += temp_num % 10
        temp_num //= 100

    # Check the last digit of the total sum
    checksum = (10 - (sum % 10)) % 10
    return checksum == 0


# The verify_card checks the credit card type: VISA, AMEX, MASTERCARD or INVALID
def verify_card(num):
    length = len(num)
    card_type = ""
    temp_num = num
    mastercard = [51, 52, 53, 54, 55]

    match length:
        # If the number has 13 digits and starts with 4, the card is VISA
        case 13:
            while temp_num > 9:
                temp_num //= 10
            if temp_num == 4:
                card_type = "VISA"
            else:
                card_type = "INVALID"

        # If the number has 15 digits and starts with 34 or 37, the card is AMEX
        case 15:
            while temp_num > 99:
                temp_num //= 10
            if temp_num == 34 or temp_num == 37:
                card_type = "AMEX"
            else:
                card_type = "INVALID"

        # If the number has 16 digits and starts with 51 or 52 or 53 or 54 or 55, the card is MASTERCARD
        # If it starts with 4, the card is VISA
        case 16:
            while temp_num > 99:
                temp_num //= 10
            if temp_num in mastercard:
                card_type = "MASTERCARD"
            else:
                temp_num //= 10
                if temp_num == 4:
                    card_type = "VISA"
                else:
                    card_type = "INVALID"
        case other:
            card_type = "INVALID"

    # Verify with Luhn Algorithm and printing the result
    if card_type != "INVALID":
        if verify_luhn_algo(num):
            return card_type
        card_type = "INVALID"
    return card_type


main()