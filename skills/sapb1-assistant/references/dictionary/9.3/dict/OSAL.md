<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSAL - Outgoing
Module: Marketing Documents | 40 columns | ObjType: 89
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  NUM: DocNum
  BASE_DOC: BaseDocObj, BaseDocNum
  OBJECT: ObjType
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  BaseDocNum Int(11) Base Document Number
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original]
  ObjType nVarChar(20) Object Type ->ADP1
  DocDate Date(8) Posting Date
  DocDueDate Date(8) Due Date
  CardCode nVarChar(15) BP Code ->OCRD
  CardName nVarChar(100) BP Name
  FreZoneNum nVarChar(8) ID Number
  Shiper nVarChar(100) Sender
  Address nVarChar(254) Address
  FromCntry nVarChar(100) Country - Origin
  ToCntry nVarChar(100) Country - Destination
  FromPort nVarChar(100) Origin Port
  ToPort nVarChar(100) Destination Port
  AirPlane nVarChar(50) Ship/Aircraft
  AirPlanNum nVarChar(40) No. of Ships/Aircraft
  TotalFob Num(19,6) Total
  Taxes Num(19,6) Taxes
  Insurance Num(19,6) Insurance
  Others Num(19,6) Other
  TotalCif Num(19,6) Document Total
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  Comments nVarChar(254) Remarks
  GroupNum Int(6) Payment Terms Code ->OCTG
  DocTime Int(6) Document Time
  SlpCode Int(11) Sales Employee default=-1 ->OSLP
  TrnspCode Int(6) Delivery Code default=-1 ->OSHP
  PartSupply VarChar(1) Delivery of Goods default=Y [Y=Yes, N=No]
  ImportEnt Int(11) Landed Costs ->OIPF
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  NumForPrn nVarChar(16) Base Doc. No. for Printing
  PurPackMsr nVarChar(8) Packaging UoM Name
  Series Int(11) Series
  BaseDocObj Int(6) Base Document Object Type
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
