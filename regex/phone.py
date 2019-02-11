import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    else:
        return None

def extract_all_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.findall(input)
    return match

# def is_valid_phone(input):
#     phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
#     match = phone_regex.search(input)
#     if match:
#         return True
#     return False

def is_valid_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False


if __name__ == "__main__":
    print(extract_phone("my name is 432 567-8976"))
    print(extract_all_phone("my name is 564 163-2898 or on 665 892-9287"))
    print(is_valid_phone("my name is 432 567-8976"))
    print(is_valid_phone("564 163-2898"))