       # program1-To calculate total number of vowels and count of each indivudual

string = "Guvi Geek network private limited"
count = 0
vowels = ["a", "e", "i", "o", "u"]
for i in range(len(string)):
    if string[i] in vowels:
        count += 1
print("Number of vowels in the given string is: ", count)
print(string.count('a',1,34))
print(string.count('e',1,34))
print(string.count('i',1,34))
print(string.count('o',1,34))
print(string.count('u',1,34))
print(len(string))


 # Program2:pyramid of number from 1 to 20

r=10
for k in range(1, r+ 1):
    for n in range(r - k):
        print(" ", end="")
    for n in range(2 * k - 1):
        print(n + 1, end="")
    print()

# Program 3:  string that returns new string after removing vowels


string = "Guvi Geek network private limited"
print(string)
result = string
vowels = ["a", "e", "i", "o", "u"]
for x in string.lower():
    if x in vowels:
        result = result.replace(x, "")

print('After removing vowels :', result)

  #Program 4: string with number of unique characters.


string = "Guvi Geek network private limited"
print(string)

lst = ['Guvi', 'Geek', 'network', 'private', 'limited']
print("The original list is : " + str(lst))
list_tuples = [(s, set(s)) for s in lst]
sorted_list = sorted(list_tuples, key=lambda x: len(x[1]), reverse=True)
result = sorted_list[0][0]

print("The string with most unique characters is : " + str(result))
print(len(str(result)))

#### Program 5: string for palindrome
string = "MAM"
print(string)
if string == string[ :: -1]:
    print("True")
else:
    print("False")

############# Program 6: String that returns frequent character
    string = "Chennai"
    print("The original string is : " + string)
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    max_char = max(freq, key=freq.get)
    print("The maximum of all characters in Chennai is : " + str(max_char))


##########Program 9: String returns the number of words

string = "What is your name"
print("The original string is : " + string)
res = len(string.split())
print("The number of words in string are : " + str(res))


########Program 10: anagram

s1 = "listen"
s2 = "silent"
char_list_1 = list(s1)
char_list_2 = list(s2)

char_count = {}
for char in char_list_1:
    if char not in char_count:
        char_count[char] = 0
    char_count[char] += 1

for char in char_list_2:
    if char not in char_count:
        print("The strings are not anagrams.")
        break
    char_count[char] -= 1
else:
    for count in char_count.values():
        if count != 0:
            print("The strings are not anagrams.")
            break
    else:
        print("The strings are anagrams.")