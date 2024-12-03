import time

def write_to_file(filename):
    for i in range(25):
        print(f"Write Line: {i} {time.time()}")
        with open(filename, 'w') as fp:
            fp.write(f"Write Line: {i} {time.time()}\n")
        #time.sleep(1)

def append_to_file(filename):
    for i in range(25):
        print(f"Append line {i} {time.time()}")
        with open(filename, 'a') as fp:
            fp.write(f"Write Line: {i} {time.time()}\n")
        #time.sleep(1)

def read_from_file(filename):
    num = 0
    with open(filename) as fp:
        num = len(fp.readlines())
    for i in range(0,num):
        print(i)

def main():
    write_to_file("file1.txt")
    append_to_file("file2.txt")
    read_from_file("file1.txt")
    read_from_file("file2.txt")


if __name__ == "__main__":
    main()
