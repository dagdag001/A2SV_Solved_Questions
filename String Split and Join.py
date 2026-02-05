def split_and_join(line):
    List = line.split()
    return "-".join(List)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)