import os
import logging
import sys
import re
import requests
import smtplib
import dns.resolver


from dns import reversename, resolver
# port defines the port used by the api server

# getEnv retrieves variables from the environment and falls back
# to a passed fallback variable if it isn't set


port = 8080
# sourceAddr defines the address used on verifier


# RetrievePTR attempts to retrieve the PTR record for the IP
# address retrieved via an API call on api.ipify.org


def retrievePTR():
    # Request the IP from ipify
    ip = requests.get('https://api.ipify.org').text

    # Retrieve the PTR record for our IP and return without a trailing dot
    print(ip)
    names = reversename.from_address(ip)
    # if err != None:
    #     return ip

    return str(names[0]).strip(".")

    return fallback

# Address used for SMTP MAIL FROM command
fromAddress = 'admin@btc.com'

# Simple Regex for syntax checking
regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

# Email address to verify
inputAddress = input('Please enter the emailAddress to verify:')

addressToVerify = str(inputAddress.lower())

# Syntax check
match = re.match(regex, addressToVerify)
if match == None:
    print('Bad Syntax')
    raise ValueError('Bad Syntax')

# Get domain for DNS lookup
splitAddress = addressToVerify.split('@')
domain = str(splitAddress[1])
print('Domain:', domain)

# MX record lookup
records = dns.resolver.query(domain, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)


# SMTP lib setup (use debug level for full output)
server = smtplib.SMTP()
server.set_debuglevel(0)

# SMTP Conversation
server.connect(mxRecord)
# server.local_hostname(Get local server hostname)
server.helo(server.local_hostname)
server.mail(fromAddress)
code, message = server.rcpt(str(addressToVerify))


# # Assume SMTP response 250 is success
if code == 250:
    print('Email is valid')
else:
    print('Email is invalid ')
