# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Last night you had to study, but decided to party instead.
Now there is a black and white photo of you that is about to go viral.
You cannot let this ruin your reputation, so you want to apply box blur
algorithm to the photo to hide its content.

The algorithm works as follows: each pixel x in the resulting image
has a value equal to the average value of the input image pixels' values
from the 3 × 3 square with the center at x. All pixels at the edges are cropped.

As pixel's value is an integer, all fractions should be rounded down.

Example

For

image = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]
the output should be boxBlur(image) = [[1]].

In the given example all boundary pixels were cropped,
and the value of the pixel in the middle was obtained as
(1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) / 9 = 15 / 9 = ~rounded down~ = 1.
"""

# Code


def boxBlur(m):
    r = len(m)
    c = len(m[0])
    ans = []
    for i in range(1, r - 1):
        row = []
        for j in range(1, c - 1):
            row.append(sum([m[i + k][j + l] for k in [-1, 0, 1]
                            for l in [-1, 0, 1]]) // 9)
        ans.append(row)
    return ans
