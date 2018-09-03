import os
import logging
import sys
import re
import smtplib
from dns import reversename, resolver
# port defines the port used by the api server
port = os.getenv("PORT", "8080")
sourceAddr = os.getenv("SOURCE_ADDR", "admin@gmail.com")

# RetrievePTR attempts to retrieve the PTR record for the IP
# address retrieved via an API call on api.ipify.org


def retrievePTR():
    # Request the IP from ipify
    ip = get('https://api.ipify.org').text

    # Retrieve the PTR record for our IP and return without a trailing dot

    names = reversename.from_address(ip)
    if err != None:
        return ip

    return names[0].strip(".")


# getEnv retrieves variables from the environment and falls back
# to a passed fallback variable if it isn't set
def getEnv(key, fallback):
    if value is os.environ[key]:
        return value

    return fallback
