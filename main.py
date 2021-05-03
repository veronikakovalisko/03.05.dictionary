"""
Task 1
Make a program that has some sentence (a string) on input
and returns a dict containing all unique words as keys and the number of occurrences as values.
"""
if __name__ == '__main__':
    words = input(" Введіть речення")
    dictionary = {}
    words1 = words.split()
    n = 0
    for i in words1:
        dictionary = {words1[n]:''}
        if words1[n] in dictionary:
            dictionary = {words1[n]: words1.count(words1[n])}
        n += 1
    print(dictionary)

"""
Task 2
Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Create a function which takes as 
input two dicts with structure mentioned above, 
then computes and returns the total price of stock.
"""
if __name__ == '__main__':
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    n = 0
    ac = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    sm = 0
    for i in stock:
        ac[i] = stock[i]*prices[i]
        sm += ac.setdefault(i)
    print(ac)
    print(sm)
"""
Task 3
List comprehension exercise
Use a list comprehension to make a list containing tuples (i, j) 
where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
"""
if __name__ == '__main__':
    i = [n for n in range(1, 11)]
    j = [i**2 for i in i]
    for x in i:
        dictionary = dict.fromkeys(i, j)
    print(dictionary)


