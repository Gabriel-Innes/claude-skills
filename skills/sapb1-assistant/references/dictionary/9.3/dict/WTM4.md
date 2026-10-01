<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WTM4 - Approval Templates - Terms
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CondId, WtmCode
Fields (name type(len) description [values] ->parent table):
  WtmCode Int(11) Code ->OWTM
  CondId Int(11) Condition No. default=0 [1=Deviation from Credit Limit, 2=Deviation from Commitment, 3=Gross Profit %, 4=Discount %, 5=Deviation from Budget, 7=Quantity, 8=Item Code, 9=Total, 6=Total Document, 10=Counted Quantity, 11=Variance, 12=Variance %, 0=Undefined Type]
  opCode Int(6) Ratio default=0 [1=Greater Than, 2=Greater or Equal, 3=Less Than, 4=Less or Equal, 5=Equal, 6=Does not Equal, 7=In Range, 8=Not in Range, 0=Undefined Type]
  opValue nVarChar(90) Value
