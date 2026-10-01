<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RRR17 - A/R Return Request - Import Process
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORRR
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=234000031 ->ADP1
  ImpDocType VarChar(1) Type of Importation Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious]
