# ipsum_file = open('files/text1.txt')

# for line in ipsum_file:
#     print(line)

# ipsum_file.seek(0)

# lines = ipsum_file.readlines()
# print(lines)

# ipsum_file.seek(50)

# file_text = ipsum_file.read(100)

# print(file_text)

# ipsum_file.close()

def secret(line):
    return '>' not in  line

with open('files/secret.txt') as dna_file:
    lines = dna_file.readlines()

sec = list(filter(secret, lines))

print(sec)