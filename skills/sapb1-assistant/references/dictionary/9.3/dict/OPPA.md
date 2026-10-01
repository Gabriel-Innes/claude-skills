<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPPA - Password Administration
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID default=1
  SecLevel nVarChar(20) Security Level default=Low [Low=Low, Medium=Medium, High=High, Custom=Custom]
  PwdExp Int(11) Password Expiration default=90
  PwdMinLen Int(11) Password Minimum Length default=4
  MinUppers Int(11) Password Min. Uppercase Chars. default=0
  MinLowCase Int(11) Password Min. Lowercase Chars. default=0
  MinDigits Int(11) Password Minimum Digits default=0
  MinNonAlph Int(11) Password Min. Non-alphanumeric Char. default=0
  NumPrevPwd Int(11) Pwd does not match pwd rules default=0
  NumAuthLoc Int(11) No. of Authentications Before Acct is Locked default=100
  PwdExample nVarChar(10) Password Example default=abcd
