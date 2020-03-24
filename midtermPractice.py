# midtermPractice.py - practice problems for midter
'''
Disclaimer: this is not intended to be a comprehensive
review for the exam.  It is intended to give you practice
solving problems similar to those that will be covered.

I recommend that you solve these without IDLE then go back
to IDLE and make sure you understand the answers
'''

############   short answer ############   


'''
What is the resulting type of each of the
following expressions?   To check, use the type
function, e.g.,

>>> type( 19%3 )

'''

19%3

'X' in 'banana'

3*3.1

4*'33'

["apple","pear","orange"][1]




'''
What is the output of each of the
following code snippets?
'''

x = [1,2,99,66][1:3]*2
print( x ) 


x = 0
for i in range(2,8):
    if i%3 != 0:
        x += i
print(x )


x = 5
y = 12
print( x>5 or y<=12)


a= 12
b = 4
while( a!=0 and b!=0):
    if (a>b):
        a = a-b
    else:
        b = b-a
print(a,b)



def f(s,t):
    ans = []
    for i in range(len(s)):
        if s[i]==t:
            ans.append(i)
    return ans
print( f('banana','a') )



############ programming ############   

'''
Write a function letterGrade that accepts your hw, midterm,
and final grades, each out of 100 points, and returns your
letter grade for this course.

Example interaction:

>>> letterGrade(90.2,87.5,83.1)
'B'
>>> letterGrade(90.2,57.5,83.1)
'C'
>>> letterGrade(94.2,77.5,99.1)
'A'
'''
def letterGrade(hw,mt,fg):
    #fg=100-(hw+mt)
    


'''
Write a function numCapitalized() that accepts a sentence
consisting of words and spaces (no punctuation) and returns
the number of words in the sentence that are capitalized.
**Note that this is NOT the total number of capitals in the string.**

>>> numCapitalized('This sentence has one such')
1
>>> numCapitalized('This sentence has ONE more ')
2
>>> numCapitalized('ALL THESE ARE')
3

'''
#referene for str.isalpha()==>https://stackoverflow.com/questions/33883512/check-if-any-character-of-a-string-is-uppercase-python
def numCapitalized(s):
    s=s.split()
    for i in s:#iterates per word
        if i[0]==i[0].upper():
            cap.append(i)
    print(len(cap))

'''
Write a function doubleVowel() that, given a word,
returns either True or False indicating whether
the word contains two adjacent vowels.
A vowel is one of the letters: a,e,i,o,u.

>>> doubleVowel('banana')
False
>>> doubleVowel('snail')
True
>>> doubleVowel('Eel')
True
>>> doubleVowel('aArdvark')
True
'''
def doubleVowel(wi):
    for i in range(len(wi)):
        if wi[i] in 'aeiouAEIOU':#checks characters for vowels
            return True
    
############ programming answers ############   


def letterGrade(hw,midterm,final):
    avg = .3*hw+.35*midterm+.35*final
    # letter grade - multiway if
    if avg>=90:
        return 'A'
    elif avg>=80:
        return 'B'
    elif avg>=70:
        return 'C'
    elif avg>=60:
        return 'D'
    else:
        return 'F'
    

def numCapitalized(sentence):
    words = sentence.split()
    cnt = 0
    for word in words:
        if 'A'<=word[0]<='Z':
            cnt+=1
    return cnt

            
#a - this solution is CORRECT but works in Python
#    and not in other common langages
#    note that the else belongs to the for, not to the if
def doubleVowel(w):
    v = 'aeiouAEIOU'
    for i in range( len(w)-1):
        if w[i]in v and w[i+1] in v:
            return True
    else:
        return False


#b  - this is INCORRECT, you do not want if/else returning True/False
#     inside a loop.  It will only iterate once
def doubleVowel(w):
    v = 'aeiouAEIOU'
    for i in range( len(w)-1):
        if w[i]in v and w[i+1] in v:
            return True
        else:
            return False

#c - this is the CORRECT and PREFERRED solution
def doubleVowel(w):
    v = 'aeiouAEIOU'
    for i in range( len(w)-1):
        if w[i]in v and w[i+1] in v:
            return True
    return False





