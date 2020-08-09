def Word_finder ( string, i):
    n = 0
    q = 0
    a=string.split()
    leng = len(a)
    for n in range (0, leng) :
        if i == len(a[n]):
            q = q+1
    return q

string = input("Enter your string:  ")
for i in range(1, 10):
    print('The name of words with length of ', i,'is ', Word_finder(string, i))

