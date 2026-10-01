<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCFL - Cash Flow Additional Trans.
Module: Finance | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, UserId
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  DateID Date(8) Date
  Dscription nVarChar(50) Description
  Project nVarChar(20) Project Code
  Credit Num(19,6) Incoming Total
  CredCur nVarChar(3) Entrance Currency
  Debit Num(19,6) Outgoing Amount
  DebCur nVarChar(3) Issue Currency
  SecLevel Int(6) Security Level default=1 [1=Cash Account, 5=Credit, 2=Checks, 3=Customer Liabilities, 6=Bill of Exchange, 4=Payable to Vendors, 7=Customer Forecast, 8=Vendor Forecast]
  UserId Int(6) User ID
  Frequency VarChar(1) Frequency default=O [D=Daily, W=Weekly, M=Monthly, Q=Quarterly, S=Semiannually, A=Annually, O=One Time]
  Remind Int(6) Subfrequency default=-1 [-1=, 1=On Sunday, 2=On Monday, 3=On Tuesday, 4=On Wednesday, 5=On Thursday, 6=On Friday, 7=On Saturday, 101=Every 1, 102=Every 2, 103=Every 3, 104=Every 4, 105=Every 5, 106=Every 6, 107=Every 7, 108=Every 8, 109=Every 9, 110=Every 10, 115=Every 15, 130=Every 30, 145=Every 45, 160=Every 60, 1001=On 1, 1002=On 2, 1003=On 3, 1004=On 4, 1005=On 5, 1006=On 6, 1007=On 7, 1008=On 8, 1009=On 9, 1010=On 10, 1011=On 11, 1012=On 12, 1013=On 13, 1014=On 14, 1015=On 15, 1016=On 16, 1017=On 17, 1018=On 18, 1019=On 19, 1020=On 20, 1021=On 21, 1022=On 22, 1023=On 23, 1024=On 24, 1025=On 25, 1026=On 26, 1027=On 27, 1028=On 28, 1029=On 29, 1030=On 30, 1031=On 31]
  EndDate Date(8) Execution End Date
  OcrCode nVarChar(8) Distribution Rule 1 ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
