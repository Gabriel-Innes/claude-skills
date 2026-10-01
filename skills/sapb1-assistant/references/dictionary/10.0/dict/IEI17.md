<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# IEI17 - Incoming Excise Invoice - Import Process
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIEI
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=140000010 ->ADP1
  ImpDocType VarChar(1) Type of Importation Document ->OBSI
  ImpDocNum nVarChar(10) Importation Document Number
  DateOfReg Date(8) Date of Registry DI/DSI/DA
  CustClrDat Date(8) Date of Customs Clearance
  ConcActNum nVarChar(30) Drawback Concession Acct No.
  AdditNum nVarChar(30) Additional Number
  AddItmDV Num(19,6) Additional Item Discount Value
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number
