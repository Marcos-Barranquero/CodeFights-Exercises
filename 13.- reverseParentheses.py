# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
You have a string s that consists of English letters, punctuation marks,
whitespace characters, and brackets. It is guaranteed that the parentheses
in s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching parentheses,
 starting from the innermost pair. The results string should not contain any parentheses.

Example

For string s = "a(bc)de", the output should be
reverseParentheses(s) = "acbde".

"""

# Code


def reverseString(String):
    return String[::-1]


def reverseParentheses(s):
    veces = s.count(")")
    for i in range(veces):

        # Busco la posición donde se cierra el primer paréntesis:
        for j in range(len(s)):
            if s[j] == ")":
                cierraparentesis = j
                break

        # Busco la posición donde se abre el primer paréntesis:
        for k in range(cierraparentesis, -1, -1):
            if s[k] == "(":
                abreparentesis = k
                break

        # Primer trozo hasta el parentesis de apertura:
        principio = s[:abreparentesis]
        # Parte entre paréntesis
        medio = s[abreparentesis + 1:cierraparentesis]
        # Le damos la vuelta:
        medio = reverseString(medio)
        # Segundo trozo desde el paréntesis de cerradura:
        resto = s[cierraparentesis + 1:]
        s = principio + medio + resto
    return s
