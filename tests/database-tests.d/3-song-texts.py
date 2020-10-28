CODE_OK   = 0
CODE_WARN = 1
CODE_ERR  = 2

def testForNoSpacesAroundLines(path, bytes, contents, text, metadata):
  for line in text.splitlines():
    if line.startswith(' ') or line.endswith(' '):
      return CODE_ERR
  return CODE_OK

# More information available here: https://smartquotesforsmartpeople.com/
def testForSmartQuotes(path, bytes, contents, text, metadata):
  unusualChars = ["'", '"']
  for char in unusualChars:
    if char in text:
      return CODE_WARN
  return CODE_OK

def testForProperEllipses(path, bytes, contents, text, metadata):
  if '..' in text:
    return CODE_WARN
  return CODE_OK

def testForNoMinuses(path, bytes, contents, text, metadata):
  if '-' in text:
    return CODE_WARN
  return CODE_OK

def testTheTests(*_):
  def testTheTestForNoSpacesAroundLines():
    passing = testForNoSpacesAroundLines('', b'', '', 'La la la\nLa la\nLa\n', {}) == CODE_OK
    failing = testForNoSpacesAroundLines('', b'', '', 'La la \n La \nLa ', {}) == CODE_ERR
    return passing and failing
  def testTheTestForSmartQuotes():
    passing = testForSmartQuotes('', b'', '', 'La la la\nLa la\nLa\n', {}) == CODE_OK
    failing = testForSmartQuotes('', b'', '', "\"It's such a beautiful day\", she said", {}) == CODE_WARN
    return passing and failing
  def testTheTestForProperEllipses():
    passing = testForProperEllipses('', b'', '', 'La la la\nLa la\nLa…\n', {}) == CODE_OK
    failing = testForProperEllipses('', b'', '', 'She said..\n', {}) == CODE_WARN
    return passing and failing
  def testTheTestForNoMinuses():
    passing = testForNoMinuses('', b'', '', 'La la la…\n', {}) == CODE_OK
    failing = testForNoMinuses('', b'', '', 'She said - he said\n', {}) == CODE_WARN
    return passing and failing
  if not testTheTestForNoSpacesAroundLines() \
  or not testTheTestForSmartQuotes() \
  or not testTheTestForProperEllipses() \
  or not testTheTestForNoMinuses():
    return CODE_ERR
  return CODE_OK
