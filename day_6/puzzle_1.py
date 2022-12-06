def puzzle_1():
    with open("C:\dev\script\\avent_of_code\puzzle_6.txt", "r") as f:
        input = ""
        for line in f:
            input += line
    i = 0
    while True:
        try:
            if input[i] == input[i+1] or input[i] == input[i+2] or input[i] == input[i+3] or \
            input[i+1] == input[i+2] or input[i+1] == input[i+3] or input[i+2] == input[i+3]:
                i += 1
            else:
                return i+4
        except IndexError:
            return None
