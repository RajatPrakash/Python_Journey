phone = input("phone: ")
number_conversion = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
final = ""
for ch in phone:
    final += number_conversion.get(ch, "Not a Number") + " "
print(final)