import re
import smtplib
import dns.resolver

#  Verifier contains all dependencies needed to perform educated email
#  verification lookups


class Verifier():
    hostname = ""
    sourceAddr = ""

#  Lookup contains all output data for an email verification Lookup


class Lookup():
    Address = ""
    ValidFormat = False
    Deliverabl = False
    FullInbox = False
    HostExists = False
    CatchAll = False

#  NewVerifier generates a new Verifier using the passed hostname and
#  source email address


def NewVerifier(hostname, sourceAddr):
    return Verifier(hostname, sourceAddr)


#  Verify performs an email verification on the passed email address
def Verify(v, email, error):
    #  Allocate memory for the Lookup
    l = Lookup()
    l.Address.Address = email

    #  First parse the email address passed
    address = ParseAddress(email)

    l.ValidFormat = True
    l.Address = address

    #  Attempt to form an SMTP Connection
    deli = NewDeliverabler(address.Domain, v.hostname, v.sourceAddr)

    deli.quit()  # // Defer close the SMTP connection

    # Host exists if we've successfully formed a connection
    l.HostExists = True

    # Retrieve the catchall status and check deliverability
    if deli.HasCatchAll(3):
        l.CatchAll = True
        l.Deliverable = True

    return l, None
