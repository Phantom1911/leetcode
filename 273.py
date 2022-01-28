# incomplete solution

def getengforthreedigits(digits):
    m = {
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety',
        100: 'Hundred'
    }
    if digits in m:
        return m[digits]
    if 21 <= digits <= 99:
        return m[(digits // 10) * 10] + " " + m[digits % 10]
    if 101 <= digits <= 999:
        return m[digits // 100] + " " + m[100] + " " + getengforthreedigits(digits % 100)

if __name__=="__main__":
    print(getengforthreedigits(999))