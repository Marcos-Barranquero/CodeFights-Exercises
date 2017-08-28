# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
"""

# Code


def evenDigitsOnly(n):
    n = str(n)
    return not("1" in n or "3" in n or "5" in n or "7" in n or "9" in n)
