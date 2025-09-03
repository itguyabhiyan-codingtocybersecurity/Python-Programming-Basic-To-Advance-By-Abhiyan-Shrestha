# Data Types

# String (Text Data)

# ''
# ""
# """ """

############################################################

a = 'hello world !'
print(a)

#############################################################

a = '"hello world"'
print(a)

##############################################################

a = ''' "hello" world" '''
print(a)

###############################################################

# Number

# Integer (without decimal)
# float (with decimal)

# Group

# List (Mutable)

a = ['hello','world','25','new world'] # List Data With Multiple Entry
a = ['hello','world','25','new world',[10,11,12,13,14]] # List data with multiple entry

# Tuple (Inmutable)

b = ['hello','world', 23,4,5]
b = ['hello','world', 23,4,5,(1,2,3,4,5)]

# Set

c = {1,2,3,4,'hello'} # number and string

print(a)
print(b)
print(c)

##########################################################################################

# Dictionary

d = {'a':"World"} # Key (anydata) and value (string only)
d = {'a':{'world'}} # # Key (any data) and value (string only)
d = {'username':'ram','password':'ram12345'} # Key (any data) and value (string only)

print (d)

# Boolen data type (true or false)

# none type (no data is none)

e = None

# Operators ()
# Arithematic Operator (bodmas rule)

# Add Operator

f = 23 + 24
f = 'hello' + 'world'
f = [1,2,3,4,5] + [1,2,3,4,5]
f = 20.5 + 30

print (f)

# Substraction Operators

g = 23 - 1
# g = 'hello' - 'world' # unsupported
# g = [1,2,3,4,5] - [1,2,3,4,5] # Unsupported
g = 23.5 - 5
print (g)

# Multiplicaion Operator

h = 22 * 2
h = 22.5 * 2
h = 'hello' * 2 # other data type also allowed
h = [1,2,3,4,5] * 2
# h = [1,2,3,4,5] * 'hello' # not valid in multiplication
print (h)

# Division Operator

i = 20 / 2 # only number only allowed with demicmal number output
print (i)

# Floor Operator

j = 20 // 2 # as division and output is not in decimal number
print(j) 

# Modulus Operator

k = 13 % 2 # reminder value is generated
print (k)

# Exponential Operator

l = 2 ** 2
print (l)

###########################################################################

# Assignment Operator

# = (assignment operator)

m = 'hello'
n = m
print (n)

#########################################################################

# Add Assignment Operator

o = 23
o += 34
o -= 40
print (o)

# Greater than operator

p = 23
q = 34

r = p > q
print (r)

# Less than Operator

s = 23
t = 34

u = s < t
print (u)

# Equals to operator

v = 40
w = 44

x = v == w
print (x)

# Not Equals to operator

noeqone = 40
noeqtwo = 44

equals = noeqone != noeqtwo
print (equals)

# Greater then or equals to operator

greatereqone = 44
greatereqtwo = 44

equalsgreater = greatereqone >= greatereqtwo
print (equalsgreater)

# Less than or equals to operator

lesseqone = 23
lesseqtwo = 44

equalsless = lesseqone <= lesseqtwo
print (equalsless)

# Logical Operator

# And Operator (both operation must be true to get true result or output is false)

logicone = 34
logictwo = 44
logicthree = 45

logicoperator = logicone > logictwo and logictwo > logicone
print (logicoperator)

# Or Operator (if one of the value is true output is will be true)

orone = 34
ortwo = 44
orthree = 45

oroperator = orone < ortwo and ortwo > orthree
print (oroperator)

# Not Operator (oposite value)

notone = 34
notwo = 44

notoperator = not (notone > notwo)
print (notoperator)

# Membership operator (not arethematic one)
# To check if they are member of the data that is to be checked

# In Operator (number is not allowed)

helloo =  'new   '
worlds = 'new data' #
worldss =  helloo in worlds
print(worldss)

hello =  '23'
world = ['new data',23]
worlds =  hello in world
print(worlds)

# Not in Operator (not in)

jk = "hello"
kj = "hello world"
kl = jk not in kj
print(kl)

# identity operator
# Is Operator (variable data same then true and if not same false is output)
# Ram Location Checking
lk = 'hello'
io = 'hello'
po = lk is io
print(po)

# Is not operator (opposite of Is operator)

nk = 'hello'
kn = 'world'
lm = nk is not kn
print(lm)