class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']

        s = s.lower()
        for i in s:
            if i in number or i in alphabet:
                string += i
        print(string)
        print(string[::-1])
        if string == string[::-1]:
            return True
        return False
  