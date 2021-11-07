def palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome
    :param value: A string
    :return: A boolean
    """
    no_spaces = value.replace(" ", "")
    lower_case = no_spaces.lower()
    if lower_case[::-1] == lower_case:
        return True
    else:
        return False