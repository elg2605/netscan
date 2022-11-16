""" gen_ips.py - Generate a list of IPs for a few common IPv4 CIDR prefixes.
                 There are no range or sanity checks here. I assume the 
                 user understands what an octet is and what the limits are.
                 This is very basic. There are much better programs for this. """

import sys
import time

USAGE_CIDR = "CIDR_Prefix should be 8, 16, 19, 20, 21, 22, 23 or 24.\n"
USAGE1 = "usage(1): python gen_ips.py CIDR_Prefix\n"
USAGE2 = "usage(2): python gen_ips.py CIDR_Prefix <OCTECT> <OCTECT> <OCTECT>\n"
USAGE = USAGE_CIDR + USAGE1 + USAGE2

def stroke8(octet1, fp):
    """ generate a /8 list of IPs"""
    for octet2 in range(256):
        for octet3 in range(256):
            for octet4 in range(256):
                print(octet1 + "." + str(octet2) + "." + str(octet3) + "." + str(octet4), file=fp)

def stroke16(octet1, octet2, fp):
    """ generate a /16 list of IPs"""
    for octet3 in range(256):
        for octet4 in range(256):
            print(octet1 + "." + octet2 + "." + str(octet3) + "." + str(octet4), file=fp)

def stroke19(octet1, octet2, octet3, fp):
    """ generate a /19 list of IPs"""
    for octet4 in range(256):
        print(octet1 + "." + octet2 + "." + octet3 + "." + str(octet4), file=fp)
    x = 0
    while x < 31:
        x = x + 1
        octet3 = int(octet3) + 1
        for octet4 in range(256):
            print(octet1 + "." + octet2 + "." + str(octet3) + "." + str(octet4), file=fp)

def stroke20(octet1, octet2, octet3, fp):
    """ generate a /20 list of IPs"""
    for octet4 in range(256):
        print(octet1 + "." + octet2 + "." + octet3 + "." + str(octet4), file=fp)
    x = 0
    while x < 15:
        x = x + 1
        octet3 = int(octet3) + 1
        for octet4 in range(256):
            print(octet1 + "." + octet2 + "." + str(octet3) + "." + str(octet4), file=fp)

def stroke21(octet1, octet2, octet3, fp):
    """ generate a /21 list of IPs"""
    for octet4 in range(256):
        print(octet1 + "." + octet2 + "." + octet3 + "." + str(octet4), file=fp)
    x = 0
    while x < 7:
        x = x + 1
        octet3 = int(octet3) + 1
        for octet4 in range(256):
            print(octet1 + "." + octet2 + "." + str(octet3) + "." + str(octet4), file=fp)

def stroke22(octet1, octet2, octet3, fp):
    """ generate a /22 list of IPs"""
    for octet4 in range(256):
        print(octet1 + "." + octet2 + "." + octet3 + "." + str(octet4), file=fp)
    x = 0
    while x < 3:
        x = x + 1
        octet3 = int(octet3) + 1
        for octet4 in range(256):
            print(octet1 + "." + octet2 + "." + str(octet3) + "." + str(octet4), file=fp)

def stroke23(octet1, octet2, octet3, fp):
    """ generate a /23 list of IPs"""
    for octet4 in range(256):
        print(octet1 + "." + octet2 + "." + octet3 + "." + str(octet4), file=fp)
    octet3 = int(octet3) + 1
    for octet4 in range(256):
        print(octet1 + "." + octet2 + "." + str(octet3) + "." + str(octet4), file=fp)

def stroke24(octet1, octet2, octet3, fp):
    """ generate a /24 list of IPs"""
    for octet4 in range(256):
        print(octet1 + "." + octet2 + "." + octet3 + "." + str(octet4), file=fp)

# main

if len(sys.argv) < 2:
    sys.exit(USAGE)

filename = 'ips_%s.txt' %time.time()
FP = open(filename, 'w')

if len(sys.argv) == 2:
    if sys.argv[1] == '8':
        stroke8(input("Enter the first octect: "), FP)
        print(filename)
        sys.exit()

    elif sys.argv[1] == '16':
        stroke16(input("Enter the first octect: "),
                input("Enter the second octect: "), FP)
        print(filename)
        sys.exit()

    elif sys.argv[1] == '19':
        stroke19(input("Enter the first octect: "),
                input("Enter the second octect: "),
                input("Enter the third octect: "), FP)
        print(filename)
        sys.exit()

    elif sys.argv[1] == '20':
        stroke20(input("Enter the first octect: "),
                input("Enter the second octect: "),
                input("Enter the third octect: "), FP)
        print(filename)
        sys.exit()

    elif sys.argv[1] == '21':
        stroke21(input("Enter the first octect: "),
                input("Enter the second octect: "),
                input("Enter the third octect: "), FP)
        print(filename)
        sys.exit()

    elif sys.argv[1] == '22':
        stroke22(input("Enter the first octect: "),
                input("Enter the second octect: "),
                input("Enter the third octect: "), FP)
        print(filename)
        sys.exit()

    elif sys.argv[1] == '23':
        stroke23(input("Enter the first octect: "),
                input("Enter the second octect: "),
                input("Enter the third octect: "), FP)
        print(filename)
        sys.exit()

    elif sys.argv[1] == '24':
        stroke24(input("Enter the first octect: "),
                input("Enter the second octect: "),
                input("Enter the third octect: "), FP)
        print(filename)
        sys.exit()
    else:
        print("%s is not a supported CIDR prefix." %sys.argv[1])
        sys.exit(USAGE)

elif len(sys.argv) > 2 and len(sys.argv) < 7:
    # first arg is MASK
    # second would be first octect
    # third would be the second octect
    # fourth would be the third octect
    if sys.argv[1] == '8':
        stroke8(sys.argv[2], FP)
        print(filename)
        sys.exit()
    elif sys.argv[1] == '16':
        stroke16(sys.argv[2], sys.argv[3], FP)
        print(filename)
        sys.exit()
    elif sys.argv[1] == '19':
        stroke19(sys.argv[2], sys.argv[3], sys.argv[4], FP)
        print(filename)
        sys.exit()
    elif sys.argv[1] == '20':
        stroke20(sys.argv[2], sys.argv[3], sys.argv[4], FP)
        print(filename)
        sys.exit()
    elif sys.argv[1] == '21':
        stroke21(sys.argv[2], sys.argv[3], sys.argv[4], FP)
        print(filename)
        sys.exit()
    elif sys.argv[1] == '22':
        stroke22(sys.argv[2], sys.argv[3], sys.argv[4], FP)
        print(filename)
        sys.exit()
    elif sys.argv[1] == '23':
        stroke23(sys.argv[2], sys.argv[3], sys.argv[4], FP)
        print(filename)
        sys.exit()
    elif sys.argv[1] == '24':
        stroke24(sys.argv[2], sys.argv[3], sys.argv[4], FP)
        print(filename)
        sys.exit()
    else:
        print("%s is not a supported CIDR prefix." %sys.argv[1])
        sys.exit(USAGE)
else:
    print("invalid arguments")
    sys.exit(USAGE)

FP.close()

