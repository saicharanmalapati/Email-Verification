import verifier
import hashlib
from address import ParseAddress


class addressSuite():

_ = check.Suite(addressSuite)


def TestParseAddress(s, c):
    email = "email_username@domain.com"
    address, err = ParseAddress(email)

    assert(err == None)
    assert(address.Username == "email_username")
    assert(address.Domain == "domain.com")
    assert(address.Address == "email_username@domain.com")
    assert(address.hashlib.md5 == "629b2a45027be2158761fecb17eb79d6")


def TestParseAddress2(s, c):
	email = "email_username@DoMAIn.CoM"
	address, err = ParseAddress(email)

	assert(err == None)
    assert(address.Username == "email_username")
    assert(address.Domain == "domain.com")
    assert(address.Address == "email_username@domain.com")
    assert(address.hashlib.md5 == "629b2a45027be2158761fecb17eb79d6")


def TestParseAddressForUpperCaseEmails(s,c):
	email = "EMAIL_USERNAME@DOMAIN.COM"
	address, err = ParseAddress(email)

	assert(err == None)
	assert(address.Username == "EMAIL_USERNAME")
	assert(address.Domain == "domain.com")
	assert(address.Address == "EMAIL_USERNAME@domain.com")
	assert(address.hashlib.md5 =="94d8a553082c902d086c47bd40ccf3c1")

def TestParseAddressInvalidEmail(s ,c):
	email = "email_username@"
	address, err = ParseAddress(email)

	assert(err == None )
	assert(address == None)




