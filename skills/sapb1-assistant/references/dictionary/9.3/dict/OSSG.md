<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSSG - Service App Setting groups
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Name nVarChar(100) Name
  CustGroup VarChar(1) Customized Group default=N [Y=Yes, N=No]
  EnEditTime VarChar(1) Enable Edit Time default=N [Y=Yes, N=No]
  EnReject VarChar(1) Enable Reject default=N [Y=Yes, N=No]
  EnResign VarChar(1) Enable Resign default=N [Y=Yes, N=No]
  EnFollowup VarChar(1) Enable Follow-up default=N [Y=Yes, N=No]
  EnSign VarChar(1) Enable Signature default=N [Y=Yes, N=No]
  EnStarRat VarChar(1) Enable Star Rating default=N [Y=Yes, N=No]
  EnActDura VarChar(1) Enable Actual Duration default=N [Y=Yes, N=No]
  AdBoardId Int(11) Advanced Dashboard ID ->OXAP
