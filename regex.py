import re

myfile = open('stock.txt', 'r')
lines = myfile.readlines()
myfile.close()

for line in lines:
    x = re.findall(
        'Jan.[0-9]+|Feb.[0-9]+|'
        + 'Mar.[0-9]+|Apr.[0-9]+|'
        + 'May.[0-9]+|Jun.[0-9]+|'
        + 'Jul.[0-9]+|Aug.[0-9]+|Sep.[0-9]+|'
        + 'Oct.[0-9]+|'
        + 'Nov.[0-9]+|Dec.[0-9]+|.0-9', line)
    y = re.findall(r'(\d+\.\d+)\D+', line)
    if(len(x[0]) < 6):
        temp = x[0]
        temp = temp[0:4] + "0" + temp[4:]
        x[0] = temp

    z = x[0]+", $" + y[0]
    print(z)

    name2 = 'Trevor Chappell'
toBeReviewed1 = reviewersDict[name1]
toBeReviewed2 = reviewersDict[name2]
lenOfName1 = len(toBeReviewed1)
lenOfName2 = len(toBeReviewed2)

if(lenOfName1 <= lenOfName2):
    rating = 0
    for movie in toBeReviewed1:
        rating = rating + \
            math.pow(float(toBeReviewed1[movie]) -
                     float(toBeReviewed2[movie]), 2)
    print("The similarity score between " + name1 +
          " and "+name2 + " is: ", math.sqrt(rating))
else:
    rating = 0
    for movie in toBeReviewed2:
        rating = rating + \
            math.pow(float(toBeReviewed1[movie]) -
                     float(toBeReviewed2[movie]), 2)
    print("The similarity score between " + name1 +
          " and "+name2 + " is: ", math.sqrt(rating))
