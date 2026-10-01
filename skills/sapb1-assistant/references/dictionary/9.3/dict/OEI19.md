<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OEI19 - Outgoing Excise Invoice - Bin Allocation Data
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BinAllocSe, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OOEI
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=140000009 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]
