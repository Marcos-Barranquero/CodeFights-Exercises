# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Correct variable names consist only of Latin letters, digits and underscores
and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
variableName(name) = true;
For name = "qq-q", the output should be
variableName(name) = false;
For name = "2w2", the output should be
variableName(name) = false.
"""

# Code


def variableName(name):
    acceptableChars = set(
        'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890_')
    if name[0] in "1234567890":
        return False

    for letter in name:
        if letter not in acceptableChars:
            return False

    return True


if __name__ == "__main__":
    print(variableName("var_1__Int"))
    "var_1__Int".isidentifier()
