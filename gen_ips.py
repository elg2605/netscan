""" gen_ips.py - Generate a list of IPs for a few common IPv4 CIDR prefixes.
                 There are no range or sanity checks here. I assume the 
                 user understands what an octet is and what the limits are.
                 This is very basic. There are much better programs for this. """

import sys
import time

USAGE = "usage: python gen_ips.py CIDR_Prefix\nCIDR_Prefix should be 8, 16, 21, 22, 23 or 24."

def stroke8(octet1, fp):
    """ generate a /8 list of IPs"""
    for octet2 in xrange(256):
        for octet3 in xrange(256):
            for octet4 in xrange(256):
                print >> fp, octet1 + "." + str(octet2) + "." + str(octet3) + "." + str(octet4)

def stroke16(octet1, octet2, fp):
    """ generate a /16 list of IPs"""
    for octet3 in xrange(256):
        for octet4 in xrange(256):
            print >> fp, octet1 + "." + octet2 + "." + str(octet3) + "." + str(octet4)

def stroke21(octet1, octet2, octet3, fp):
    """ generate a /21 list of IPs"""
    for octet4 in xrange(256):
        print >> fp, octet1 + "." + octet2 + "." + octet3 + "." + str(octet4)
    x = 0
    while x < 7:
        x = x + 1
        octet3 = int(octet3) + 1
        for octet4 in xrange(256):
            print >> fp, octet1 + "." + octet2 + "." + str(octet3) + "." + str(octet4)

def stroke22(octet1, octet2, octet3, fp):
    """ generate a /22 list of IPs"""
    for octet4 in xrange(256):
        print >> fp, octet1 + "." + octet2 + "." + octet3 + "." + str(octet4)
    x = 0
    while x < 3:
        x = x + 1
        octet3 = int(octet3) + 1
        for octet4 in xrange(256):
            print >> fp, octet1 + "." + octet2 + "." + str(octet3) + "." + str(octet4)

def stroke23(octet1, octet2, octet3, fp):
    """ generate a /23 list of IPs"""
    for octet4 in xrange(256):
        print >> fp, octet1 + "." + octet2 + "." + octet3 + "." + str(octet4)
    octet3 = int(octet3) + 1
    for octet4 in xrange(256):
        print >> fp, octet1 + "." + octet2 + "." + str(octet3) + "." + str(octet4)

def stroke24(octet1, octet2, octet3, fp):
    """ generate a /24 list of IPs"""
    for octet4 in xrange(256):
        print >> fp, octet1 + "." + octet2 + "." + octet3 + "." + str(octet4)

# main
if len(sys.argv) != 2:
    sys.exit(USAGE)

FP = open('ips_%s.txt' %time.time(), 'w')

if sys.argv[1] == '8':
    stroke8(raw_input("Enter the first octect: "), FP)

elif sys.argv[1] == '16':
    stroke16(raw_input("Enter the first octect: "),
             raw_input("Enter the second octect: "), FP)

elif sys.argv[1] == '21':
    stroke21(raw_input("Enter the first octect: "),
             raw_input("Enter the second octect: "),
             raw_input("Enter the third octect: "), FP)

elif sys.argv[1] == '22':
    stroke22(raw_input("Enter the first octect: "),
             raw_input("Enter the second octect: "),
             raw_input("Enter the third octect: "), FP)

elif sys.argv[1] == '23':
    stroke23(raw_input("Enter the first octect: "),
             raw_input("Enter the second octect: "),
             raw_input("Enter the third octect: "), FP)

elif sys.argv[1] == '24':
    stroke24(raw_input("Enter the first octect: "),
             raw_input("Enter the second octect: "),
             raw_input("Enter the third octect: "), FP)

else:
    print "%s is not a supported CIDR prefix." %sys.argv[1]

FP.close()

