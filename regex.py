import re

text = """Offer not valid in conjunction with any other promotions & discounts.
Offer to be best offer for Emirates NBD Cardholders during the promotion duration.
Offers are only valid with payment made using an Emirates NBD Credit or Debit Card.
Offer is subject to availability and advance reservation is required.
Offer cannot be used during public holidays or special occasions.\
Offer is not valid in Q's Bar and Lounge, La Piscina and Champagne brunch at Giardino.
Offer is not applicable on Brunch
F&B Discount is not valid on entrance of La Piscina Pools.
F&B and Spa offer is applicable only valid for the Cardholder plus 3 guests.
http://www.google.com mehuluvs99@gmail.com
Emirate NBD Credit or Debit Card"""

matches = re.finditer(r"Emirate.?", text)
for match in matches:
    print(match)


test = '123abc1254ABC12578.ABC'
pattern = re.compile(r'ABC')
matches = pattern.finditer(test)
matches = re.finditer(r"ABC", test)
for match in matches:
    print(match)

"""<re.Match object; span=(10, 13), match='ABC'>
<re.Match object; span=(18, 21), match='ABC'>"""

matches = re.findall(r"ABC", test)
for match in matches:
    print(match)
    "ABC\
    ABC"

matches = re.match(r"123", test)
print("match search from begenning string ", matches)

matches = re.search(r"ABC", test)
print("find any location ", matches)

for match in re.finditer(r"ABC", test):
    print("start end index result ", match.span(), match.start(), match.end())
    print("start end index result in tuple ", match.span())
    print("group string ", match.group())

for match in re.finditer(r"\.", test):
    print("using \. ", match, end="\t")
    print(match.group())

for match in re.finditer(r"ABC$", test):
    print("using ^ find starting value {}".format(match.group()), match, end="\t")
    print(match.group())
    print("using {} find ending value $".format(match.group()), match, end="\t")
    print(match.group())

test1 = 'hello 123_ heyho heho'

for match in re.finditer(r"\d", test1):
    print("using \d find digits index {}".format(match.group()), match, end="\t")
    print(match.group())

for match in re.finditer(r"\D", test1):
    print("using \D ingore digits  {}".format(match.group()), match, end="\t")
    print(match.group())

for match in re.finditer(r"\s", test1):
    print("using \s find white space {}".format(match.group()), match, end="\t")
    print(match.group())

for match in re.finditer(r"\S", test1):
    print("using \S ingore whitespace {}".format(match.group()), match, end="\t")
    print(match.group())

w = []
for match in re.finditer(r"\w", test1):
    print("using \w ingore whitespace {}".format(match.group()), match, end="\t")
    a = w.append(match.group())
    print(match.group())
print(w)

W = []
for match in re.finditer(r"\W", test1):
    print("using \W find whitespace {}".format(match.group()), match, end="\t")
    a = W.append(match.group())
    print(match.group())
print(W)
print()

test1 = 'hello 123_ heyho hehey'
b = []
for match in re.finditer(r"\bhey", test1):
    print("using \b block of string {}".format(match.group()), match, end="\t")
    a = b.append(match.group())
    print(match.group())
print(b)
print()

test1 = 'hello 123_ heyho hehey'
B = []
for match in re.finditer(r"\Bhey", test1):
    print("using \B ignore block of string {}".format(match.group()), match, end="\t")
    a = B.append(match.group())
    print(match.group())
print(B)
print()

test1 = 'hello 123_ heyho hehey'
st = []
for match in re.finditer(r"[helo]", test1):
    print("using [helo] {}".format(match.group()), match, end="\t")
    a = st.append(match.group())
    print(match.group())
print(st)
print()

test1 = 'hello 123_ heyho hehey'
st = []
for match in re.finditer(r"[12]", test1):
    print("using [12] {}".format(match.group()), match, end="\t")
    a = st.append(match.group())
    print(match.group())
print(st)
print()

test1 = 'hello _123_ heyho hehey'
st = []
for match in re.finditer(r"_?\d{2}", test1):
    print("using _?\d {}".format(match.group()), match, end="\t")
    a = st.append(match.group())
    print(match.group())
print(st)
print()
