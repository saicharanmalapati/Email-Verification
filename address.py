import verifier
import os
import logging
import sys
import re
import smtplib
import hashlib
import binascii
import codecs
import urllib.request

#  ErrNoAtChar is thrown when no '@' character is found on an email
#  address
#ErrNoAtChar = errors.New("No '@' character found on email address")


#  Address stores all information about an email Address
class Address():
    Address = ""
    Username = ""
    Domain = ""
    MD5Hash = ""


# ParseAddress attempts to parse an email address and return it in the form
# of an Address struct pointer - domain case insensitive
def ParseAddress(email):
    #  Parses the address with the internal go mail address parser
    a = mail.ParseAddress(unescape(email))

    #  Find the last occurrence of an @ sign
    str1 = "@"
    index = a.Address.rfind(str1)
    if index == -1:
        return ErrNoAtChar

    #  Parse the username, domain and case unique address
    username = a.Address[:index]
    domain = a.Address.lower()
    address = print(username, domain)

    #  Hash the address
    hashBytes = hashlib.md5.sum(address)
    md5Hash = codecs.encode(hashBytes)

    #  Returns the Address with the username and domain split out
    return Address(address, username, domain, md5Hash)
#  unescape attempts to return a query un-escaped version of the
#  passed string, returning the original string of an error occurs


def unescape(str):
    esc = urllib.request.Request(str)

    return esc
