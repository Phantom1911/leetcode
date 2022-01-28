def getmaxmsg():
    filepath = "/Users/aastik.koshta/logfile.txt"
    with open(filepath) as file:
        lines = file.readlines()
        print(lines)
        lines = [line.rstrip() for line in lines]
        


if __name__=="__main__":
    print(getmaxmsg())

