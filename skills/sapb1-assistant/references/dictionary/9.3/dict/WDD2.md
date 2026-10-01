<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WDD2 - Documents for Approval - Terms
Module: Marketing Documents | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CondId, WddCode
Fields (name type(len) description [values] ->parent table):
  WddCode Int(11) Internal ID
  CondId Int(11) Condition No. [1=Deviation from Credit Limit, 2=Deviation from Commitment, 3=Gross Profit %, 4=Discount %, 5=Deviation from Budget, 6=Total Document]
  opCode Int(6) Ratio [1=Greater than, 2=Greater or Equal, 3=Less than, 4=Less or Equal, 5=Equal, 6=Does not Equal]
  opValue nVarChar(40) Value
