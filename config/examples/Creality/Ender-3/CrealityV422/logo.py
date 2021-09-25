#!/usr/bin/env python
# Woflang Torres - wolfang.torres@gmail.com
# Convert the output of https://www.dcode.fr/binary-image to something usable on Bootscreen.https
# len of image is 88 charater, 1 is empty, 0 is colored, the height is 58 lines

INPUT = """1111111111111111111111111111111111111111111111111111111111
1111111111111111111111111111111111111111111111111111111111
1111111111111111111111111111111111111111111111111111111111
1111111000000000000000000000000000000000000000000001111111
1111110000000000000000000000000000000000000000000000111111
1111100000000000000000000000000000000000000000000000011111
1111000000000000000000000000000000000000000000000000001111
1110000000000000000000000000000000000000000000000000000111
1110000000000000000000000000000000000000000000000000000111
1110000000111111111111111111111111111111111111110000000111
1110000000111111111111111111111111111111111111110000000111
1110000000111111111111111111111111111111111111110000000111
1110000001111111111111111111111111111111111111111000000111
1110000001111111111111111111111111111111111111111000000111
1110000001111111111111111111111111111111111111111000000111
1110000001111111111111111111111111111111111111111000000111
1110000001111111111111111111111111111111111111111000000111
1110000001111111111111111111111100001111111111111000000111
1110000001111111111000011111111000000000111111111000000111
1110000011111111110000000000000000000000011111111100000111
1110000011111111100000000000000000000100011111111100000111
1110000011111111100000000000000000001110011111111100000111
1110000011111111100000000000000110011111111111111100000111
1110000011111111100000000000001110011111111111111100000111
1110000011111111100000000000111110011111111111111100000111
1110000011111111100000000011111110001111111111111100000111
1110000111111111110000001111111111001111111111111110000111
1110000111111111111000000111111111111111111111111110000111
1110000011111111111100000011111111111111111111111100000111
1110000011111111111110000011111111111111111111111100000111
1110000011111111111110000001111111111111111111111100000111
1110000001111111111110000000111111111111111111111000000111
1110000001111111111110000000011111111111111111111000000111
1110000001111111111111000000000001111111111111111000000111
1110000000111111111111000000000000001111111111110000000111
1110000000111111111111000000000000000111111111110000000111
1110000000011111111110000000000000000111111111100000000111
1110000000001111111110000000000000000111111111000000000111
1110000000001111111110000000000000000111111111000000000111
1110000000000111111110000000000000000111111110000000000111
1110000000000011111110000000000000000111111100000000000111
1110000000000011111111111111111111111111111100000000000111
1110000000000001111111111111111111111111111000000000000111
1110000000000000111111111111111111111111110000000000000111
1110000000000000011111111111111111111111100000000000000111
1110000000000000001111111111111111111111000000000000000111
1110000000000000000011111111111111111100000000000000000111
1110000000000000000001111111111111111000000000000000000111
1110000000000000000000001111111111000000000000000000000111
1110000000000000000000000000000000000000000000000000000111
1110000000000000000000000000000000000000000000000000000111
1111000000000000000000000000000000000000000000000000001111
1111100000000000000000000000000000000000000000000000011111
1111110000000000000000000000000000000000000000000000111111
1111111000000000000000000000000000000000000000000001111111
1111111111111111111111111111111111111111111111111111111111
1111111111111111111111111111111111111111111111111111111111
1111111111111111111111111111111111111111111111111111111111
"""


"""Logo Original
const unsigned char custom_start_bmp[] PROGMEM = {
    B11111111, B11111111, B11111111, B11111111, B11101111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11101111, B11101111, B11111111, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11100111, B11011111, B11111111, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11100111, B11011111, B11111111, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11100011, B11011111, B11111111, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11110011, B11001111, B11111111, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11100001, B11100001, B11001111, B11111111, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111110, B01111000, B00000000, B00000000, B00000011, B11011101, B11111111, B11111111, B11111111, B11111111,
    B11111110, B11111111, B10000000, B01111110, B00000000, B00000001, B11101110, B11111111, B11111111, B11111111, B11111111,
    B11111110, B01111101, B11001111, B11111100, B00000000, B00000000, B11110111, B01111111, B11111111, B11111111, B11111111,
    B11111111, B10001110, B00000110, B00000000, B00000000, B00000000, B01111011, B10111111, B11111111, B11111111, B11111111,
    B11111111, B11000000, B00000000, B00000000, B00000000, B00000000, B01111101, B11011111, B11111111, B11111111, B11111111,
    B11111111, B11111100, B00000001, B11111110, B00000000, B00000000, B00111110, B11100111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111100, B00000000, B00000011, B00011111, B01110011, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111000, B00000000, B00000001, B10001111, B10000001, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11100000, B00000000, B00000000, B10000011, B11111001, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B00000000, B11111100, B00000000, B00000000, B11110000, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11100000, B00001111, B11111111, B11000000, B00000000, B00000000, B11111111, B11111111, B11111111,
    B11111111, B11111110, B00000011, B11111111, B11111111, B11000000, B00000000, B00000000, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111001, B00000000, B00000000, B00000000, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111100, B00000000, B00000111, B11000000, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B00000000, B00000111, B11100000, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B11100000, B00000111, B11110001, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B11111100, B00000111, B11111001, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B00000011, B11111001, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B10000011, B11111001, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11000011, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11100001, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11110000, B10111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B11111011, B11111000, B00111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B11111001, B11111000, B00111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B01111110, B11110000, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B10001110, B00000011, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B11100000, B00011111, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B11111111, B01111111, B11111111, B11111111, B11111111,
    B11111111, B00000000, B00000000, B01111111, B11111111, B11111111, B11111000, B01111111, B11111111, B11111111, B11111111,
    B11111111, B10000000, B00000000, B01111111, B11111111, B11111111, B11100000, B01111111, B11111111, B11111111, B11111111,
    B11111111, B11000011, B11111100, B11111111, B11111111, B11111111, B11111000, B11111111, B11111111, B11111111, B11111111,
    B11111111, B11000011, B11111100, B11111111, B11111111, B11111111, B11111000, B11111111, B11111111, B11111111, B11111111,
    B11111111, B10000111, B11111101, B11111111, B11111111, B11111111, B11110001, B11111111, B11111111, B11111111, B11111111,
    B11111111, B10000111, B11111111, B11111111, B11111111, B11111111, B11110001, B11111111, B11111111, B11111111, B11111111,
    B11111111, B00001111, B11100111, B11110011, B00001111, B11111100, B00100011, B11111100, B00111111, B11111111, B11111111,
    B11111111, B00001111, B11101111, B10000000, B00000111, B11110000, B00000011, B11110000, B00011110, B00000000, B01111111,
    B11111110, B00011111, B11001111, B10000001, B10000111, B11000111, B10000111, B11000111, B00001100, B00000000, B01111111,
    B11111110, B00000000, B00011111, B11000111, B11000111, B10001111, B11000111, B10011111, B00001111, B00001100, B11111111,
    B11111110, B00000000, B00011111, B10000111, B10001111, B00011111, B10001111, B00011111, B00001111, B00011111, B11111111,
    B11111100, B00111111, B10011111, B10001111, B10001111, B00011111, B10001110, B00000000, B00011110, B00111111, B11111111,
    B11111100, B01111111, B00111111, B00001111, B00011110, B00111111, B00011110, B00111111, B11111110, B00111111, B11111111,
    B11111000, B01111111, B11111111, B00011111, B00011100, B00111111, B00011100, B01111111, B11111100, B01111111, B11111111,
    B11111000, B11111111, B11111111, B00011110, B00011100, B01111110, B00011100, B01111111, B11111100, B01111111, B11111111,
    B11110000, B11111111, B11001110, B00111110, B00111100, B01111110, B00111100, B01111111, B10111000, B11111111, B11111111,
    B11110000, B11111111, B10011110, B00111100, B00111000, B01111100, B00111000, B01111110, B01111000, B11111111, B11111111,
    B11100001, B11111111, B00111100, B01111100, B01111000, B01111100, B01111000, B00111100, B11110001, B11111111, B11111111,
    B11100001, B11111000, B00111000, B01111000, B01111000, B00010000, B00011000, B00000001, B11110001, B11111111, B11111111,
    B00000000, B00000000, B01100000, B00100000, B00111100, B00000000, B01111100, B00000111, B10000000, B01111111, B11111111,
    B11111111, B11111111, B11111111, B11111111, B11111110, B00011111, B11111110, B00011111, B11111111, B11111111, B11111111};
"""


def main():
    print("""const unsigned char custom_start_bmp[] PROGMEM = {""")
    lines = INPUT.splitlines()
    while len(lines) < 58:
        lines.append("1" * 8 * 11)
    for l in range(58):
        line = lines[l]
        if len(line) < 8 * 11:
            diff = (8 * 11) - len(line)
            if diff % 2 == 0:
                space_a = space_b = diff // 2
            else:
                space_a = diff // 2
                space_b = space_a + 1
            line = ("1" * space_a) + line + ("1" * space_b)
        print("    ", end="")
        for i in range(11):
            code = line[(i * 8) : (i * 8) + 8]
            if l == 57 and i == 10:
                end = ""
            elif i == 10:
                end = ",\n"
            else:
                end = ", "
            print(f"B{code}", end=end)
    print("""};""")


if __name__ == "__main__":
    main()
