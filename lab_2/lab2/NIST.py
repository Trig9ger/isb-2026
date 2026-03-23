from math import sqrt
from scipy.special import gammaincc, erfc

def read_sequence(path_seq: str) -> str:
    sequence = ""
    with open(path_seq, 'r', encoding='utf-8') as file:
        sequence += file.read()
    return sequence

def frequency_test(sequence: str) -> float:
    n = len(sequence)
    s = 0
    for i in sequence:
        if i == '1':
            s += 1
        else:
            s -= 1
    
    p = abs(s)/sqrt(2*n)
    return erfc(p)

def consecutive_test(sequence: str) -> float:
    n = len(sequence)
    s = 0

    for i in sequence:
        if i == '1':
            s += 1
    l = s/n

    if abs(l-0.5) >= 2/sqrt(n):
        return 0

    v = 0
    k = sequence[0]
    for j in sequence:
        if j != k:
            v += 1
        k = j
    
    p = abs(v - (2 * n * l * (1 - l))) / (2 * sqrt(2 * n) * l * (1 - l))
    return erfc(p)

def byte_test(sequence: str) -> float:
    v  = [0, 0, 0, 0]
    n = len(sequence)
    check = 0
    live_counter, max_counter = 0, 0

    for i in sequence:
        if i == '1':
            live_counter += 1
        else:
            max_counter = max(live_counter, max_counter)
            live_counter = 0
        check += 1

        if check == 8:
            max_counter = max(live_counter, max_counter)
            live_counter = 0
            check = 0

            if max_counter <= 1:
                v[0] += 1
            elif max_counter == 2:
                v[1] += 1
            elif max_counter == 3:
                v[2] += 1
            else:
                v[3] += 1
            max_counter = 0

    x2 = 0
    n = [0.2148, 0.3672, 0.2305, 0.1875]
    for j in range(4):
        x2 += ((v[j]-16*n[j])**2)/(16*n[j])

    p = gammaincc(3/2, x2/2)
    return p

def main():
    files = ["cpprand.txt", "crand.txt", "javarand.txt"]

    for path in files:
        sequence = read_sequence(path)
        
        first_test = frequency_test(sequence)
        second_test = consecutive_test(sequence)
        third_test = byte_test(sequence)
        
        if first_test < 0.01:
            print(f'File {path} did not pass first test with p-value = {first_test}')
        
        if second_test < 0.01:
            print(f'File {path} did not pass second test with p-value = {second_test}')
        
        if third_test < 0.01:
            print(f'File {path} did not pass third test with p-value = {third_test}')
            

if __name__ == "__main__": 
    main()
