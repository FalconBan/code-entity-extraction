class read_and_extract:
    def __init__(self):
        pass

    def open_and_read(self, filename):
        code_file = open(filename, "r")
        for line in code_file:
            print(line)
            tokens = line.split()
            print(tokens)
