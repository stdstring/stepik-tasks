from io import StringIO

def main():
    alplabet_size, _encoded_size = map(int, input().split())
    alphabet = {}
    for _ in range(alplabet_size):
        [ch, binary_str] = input().split(': ')
        alphabet[binary_str] = ch
    source = input()
    buffer = StringIO()
    while len(source) > 0:
        index = 1
        while source[0:index] not in alphabet:
            index += 1
        buffer.write(alphabet[source[0:index]])
        source = source[index:]
    print (buffer.getvalue())

if __name__ == "__main__":
    main()