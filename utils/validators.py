import re

phone_validator = re.compile(r'((?:\(?\d{2}\)?\s*)?(?:9\s*)?(?:\d{4}-?\d{4}))')

if __name__ == "__main__":

    phones = """21912341234
    (21)912341234
    21 9 12341234
    (21) 9 12341234
    21912341234
    (21)912341234
    21 9 1234-1234
    (21) 9 1234-1234
    (21) 91234-1234
    (21)9 1234-1234
    """

    for phone in phone_validator.findall(phones):
        print(phone)

        