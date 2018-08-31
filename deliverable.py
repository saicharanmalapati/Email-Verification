import verifier
import os
import sys
import re
import smtplib
import time
import dns
import datetime
import dns.resolver
from datetime import timedelta

# Deliverabler contains the context and smtp.Client needed to check
# email address deliverability


class Deliverabler():
    domain = ""
    hostname = ""
    sourceAddr = ""
    server = smtplib.SMTP()

# NewDeliverabler generates a new Deliverabler reference


def NewDeliverabler(domain, hostname, sourceAddr):
        # Dial any SMTP server that will accept a connection

    server = mailDialTimeout(domain, timedelta.min)

    # Sets the HELO/EHLO hostname
    if server.helo(server.local_hostname):
        return err
        # Sets a source address
    if err = server.mail(sourceAddr)
        return err
       # Return the deliverabler if successful
    return Deliverabler(client, domain, hostname, sourceAddr)

# // dialSMTP receives a domain and attempts to dial the mail server having
# // retrieved one or more MX records


def mailDialTimeout(domain, timeout):
        #// Convert any internationalized domain names to ascii

    asciiDomain = domain.encode("idna")

   # Retrieve all MX records
    records = dns.resolver.query(asciidomain, 'MX').all()

   # Verify that at least 1 MX record is found
    if len(records) == 0:
        raise ValueError('No MX records found')

    # // Create a channel for receiving responses from
    chan = range(0)
    ch = chan[::1]

    # // Done indicates if we're still waiting on dial responses
    bool = False
    # // Attempt to connect to all SMTP servers concurrently
    for record in records:
        addr:
            = record.Host + ":25"

        def func():
            c = smtpDialTimeout(addr, timeout)

            # // Place the client on the channel or close it

            if !done:
                done = true
                ch = c
            # there's no channel in python to close
    errSlice = []
    for:
        res = ch
            if res.(type):
                smtp.server
                return res.(type)

            else:
                raise ValueError("Unexpected response dialing SMTP server")


# // smtpDialTimeout is a timeout wrapper for smtp.Dial. It attempts to dial an
# // SMTP server and fails with a timeout if the passed timeout is reached while
# // attempting to establish a new connection

def smtpDialTimeout(addr, timeout):
        # // Channel holding the new smtp.Client or error
    ch = make(chan interface{}, 1)

    # // Dial the new smtp connection
    def():
        client = server.connect(addr)

        ch = client


# // IsDeliverable takes an email address and performs the operation of adding
# // the email to the envelope. It also receives a number of retries to reconnect
# // to the MX server before erring out. If a 250 is received the email is valid
def IsDeliverable(email, retry):
    if err = d.client.Rcpt(email)
    err is not None:
        # // If we determine a retry should take place
        if shouldRetry(err) & & retry > 0
        # Close the previous Deliverabler
            d.Close()
            # Generate a new Deliverabler
            d = NewDeliverabler(d.domain, d.hostname, d.sourceAddr)

            # Retry deliverability check
            return d.IsDeliverable(email, retry - 1)

        return err

    return None

# // HasCatchAll checks the deliverability of a randomly generated address in
# // order to verify the existence of a catch-all


def HasCatchAll(d):
    return d.IsDeliverable(randomEmail(d.domain), retry) == None


# // Close closes the Deliverablers SMTP client connection
def Close(d):
    d.server.quit()

# // shouldRetry determines whether or not we should retry connecting to the
# // smtp server based on the response received


def shouldRetry(err):
    if err == None:
        return false

    return insContains(err.Error(),
                       "i/o timeout",
                       "broken pipe",
                       "exceeded the maximum number of connections",
                       "use of closed network connection",
                       "connection reset by peer",
                       "connection declined",
                       "connection refused",
                       "multiple regions",
                       "server busy",
                       "eof")
# / randomEmail generates a random email address using the domain passed. Used
# // primarily for checking the existence of a catch-all address


def randomEmail(domain):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    result:
        = make([]byte, 20)
    for i in range(20):
        result[i] = chars[random.randint(len(chars))]

    return (str(result), domain)
