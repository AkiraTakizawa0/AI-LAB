import string

print("Enter Sample String")
data = input()

print(f"Initial data is {data}")
punctuations = string.punctuation


p, s, c = 0, 0, 0

for elem in data:
    if elem in punctuations:
        data = data.replace(elem, "")
        p = p + 1
    elif elem == " ":
        s = s + 1
    elif elem == "a":
        data = data.replace(elem, "b")
        c += 1

print(f"Final Data {data}")
print(f"Punctuations {p}\nSpaces {s}\nCharacters Replaces {c}")
