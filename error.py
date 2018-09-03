ErrUnexpectedResponse = "Unexpected response from deliverabler"

#  Standard Errors
ErrTimeout = "The connection to the mail server has timed out"
ErrNoSuchHost = "Mail server does not exist"
ErrServerUnavailable = "Mail server is unavailable"
ErrBlocked = "Blocked by mail server"

#  RCPT Errors
ErrTryAgainLater = "Try again later"
ErrFullInbox = "Recipient out of disk space"
ErrTooManyRCPT = "Too many recipients"
ErrNoRelay = "Not an open relay"
ErrMailboxBusy = "Mailbox busy"
ErrExceededMessagingLimits = "Messaging limits have been exceeded"
ErrNotAllowed = "Not Allowed"
ErrNeedMAILBeforeRCPT = "Need MAIL before RCPT"
ErrRCPTHasMoved = "Recipient has moved"

#  LookupError is an error


class LookupError():
    Message = ""
    Details = ""

#  newLookupError creates a new LookupError reference and
#  returns it


def newLookupError(message, details):
    return LookupError(message, details)
#  Error satisfies the error interface


def Error(e):
    return (e.Message, e.Details)


#  ParseSMTPError receives an MX Servers response message
#  and generates the cooresponding MX error
def ParseSMTPError(err)
    if err == None
        return None

    errStr = err.Error()

    # Verify the length of the error before reading nil indexes
    if len(errStr) < 3
        return parseBasicErr(err)

    # Strips out the status code string and converts to an integer for parsing
    status, convErr = strconv.Atoi(string([]rune(errStr)[0:3]))
    if convErr != None
        return parseBasicErr(err)

    # If the status code is above 400 there was an error and we should return
    # it
    if status > 400:
        #  Don't return an error if the error contains anything about the address
        #  being undeliverable
        if insContains(errStr,
                       "undeliverable",
                       "does not exist",
                       "may not exist",
                       "user unknown",
                       "user not found",
                       "invalid address",
                       "recipient invalid",
                       "recipient rejected",
                       "address rejected",
                       "no mailbox")
            return None

        if status == 421:
            return newLookupError(ErrTryAgainLater, errStr)
        if status == 450:
            return newLookupError(ErrMailboxBusy, errStr)
        if status == 451:
            return newLookupError(ErrExceededMessagingLimits, errStr)
        if status == 452:
            if insContains(errStr,
                           "full",
                           "space",
                           "over quota",
                           "insufficient",
                           )
                return newLookupError(ErrFullInbox, errStr)

            return newLookupError(ErrTooManyRCPT, errStr)
        if status == 503:
            return newLookupError(ErrNeedMAILBeforeRCPT, errStr)
        if status == 550:  # 550 is Mailbox Unavailable - usually undeliverable
            if insContains(errStr,
                           "spamhaus",
                           "proofpoint",
                           "cloudmark",
                           "banned",
                           "blacklisted",
                           "blocked",
                           "block list",
                           "denied")
                return newLookupError(ErrBlocked, errStr)

            return None
        if status == 551:
            return newLookupError(ErrRCPTHasMoved, errStr)
        if status == 552:
            return newLookupError(ErrFullInbox, errStr)
        if status == 553:
            return newLookupError(ErrNoRelay, errStr)
        if status == 554:
            return newLookupError(ErrNotAllowed, errStr)

    return None


#  parseBasicErr parses a basic MX record response and returns
#  a more understandable LookupError
func parseBasicErr(err):
    if err == None
        return None

    errStr:
        = err.Error()

    #  Return a more understandable error

    if insContains(errStr,
                   "spamhaus",
                   "proofpoint",
                   "cloudmark",
                   "banned",
                   "blocked",
                   "denied"):
        return newLookupError(ErrBlocked, errStr)
    if insContains(errStr, "timeout"):
        return newLookupError(ErrTimeout, errStr)
    if insContains(errStr, "no such host"):
        return newLookupError(ErrNoSuchHost, errStr)
    if insContains(errStr, "unavailable"):
        return newLookupError(ErrServerUnavailable, errStr)


#  insContains returns true if any of the substrings
#  are found in the passed string. This method of checking
#  contains is case insensitive
def insContains(str, subStrs):
    for _, subStr in range(len(subStrs)):
        if (str.lower()).contains(subStr.lower())
            return True

    return False
