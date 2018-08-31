from error import ParseSMTPError


def TestParse550RCPTError(t):
    err = "550 This mailbox does not exist"
    le = ParseSMTPError(err)
    assert(t == le)


def TestParse550BlockedRCPTError(t):
    err = "550 spamhaus"
    le = ParseSMTPError(err)
    assert.Equal(t == le.Message)
    assert.Equal(t == le.Details)
