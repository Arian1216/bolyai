red = '\033[1;31;49m'
green = '\033[1;32;49m'


# Any '\033' is a color code that changes the color of the text that follows.


# the definition convert: converts a number (0-255) to a binary octet. any number above 255 will return as 255 in binary

def convert(number):
    binary = [128, 64, 32, 16, 8, 4, 2, 1]
    final = ''
    for a in binary:
        if number >= a:
            final = final + '\033[1;32;49m' + '1'
            number = number - a
        else:
            final = final + '\033[1;31;49m' + '0'
    return final


# User inputs the ip address.
ipv4 = raw_input('\033[1;33;49m' + 'Enter IP Address: ' + '\033[1;32;49m')

# IP address is separated into a list.
ipv4_2 = list(ipv4)

ipv4_3 = []
ipv4_4 = []
ipv4_5 = []
ipv4_6 = []

num = 3
log = True

# This loop goes through the IP address, removes the decimal point, and separates the IP address into four lists.
while log:
    for a in ipv4_2:
        if num == 3:
            if a == '.':
                num += 1
            else:
                ipv4_3.append(a)
        elif num == 4:
            if a == '.':
                num += 1
            else:
                ipv4_4.append(a)
        elif num == 5:
            if a == '.':
                num += 1
            else:
                ipv4_5.append(a)
        elif num == 6:
            if a == '.':
                num += 1
            else:
                ipv4_6.append(a)
    num = 3
    log = False

ipv4_2_2 = ''
ipv4_3_3 = ''
ipv4_4_4 = ''
ipv4_5_5 = ''
ipv4_6_6 = ''

# this section joins each list together into a string. example: [1,9,8] now equals '198'
for i in ipv4_3:
    ipv4_3_3 = ipv4_3_3 + i

for i in ipv4_4:
    ipv4_4_4 = ipv4_4_4 + i

for i in ipv4_5:
    ipv4_5_5 = ipv4_5_5 + i

for i in ipv4_6:
    ipv4_6_6 = ipv4_6_6 + i

# this section takes the string and makes it an Integer
ipv4_3_3 = int(ipv4_3_3)
ipv4_4_4 = int(ipv4_4_4)
ipv4_5_5 = int(ipv4_5_5)
ipv4_6_6 = int(ipv4_6_6)

# now that we have four seprate numbers, we use the 'convert' definition to change the number into a binary octet.
ipv41 = convert(ipv4_3_3)
ipv42 = convert(ipv4_4_4)
ipv43 = convert(ipv4_5_5)
ipv44 = convert(ipv4_6_6)

print('\n')
