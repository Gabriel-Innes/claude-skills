<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OINS - Customer Equipment Card
Module: Service | 55 columns | ObjType: 176
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: insID
  C_ITM_SN_S: status, internalSN, itemCode, customer
  ITM_MNFSN: manufSN, itemCode
  ITM_INTSN: internalSN, itemCode
Fields (name type(len) description [values] ->parent table):
  insID Int(11) Equipment Card No.
  customer nVarChar(15) Business Partner Code ->OCRD
  custmrName nVarChar(100) Business Partner Name
  contactCod Int(11) Contact Person Code ->OCPR
  directCsmr nVarChar(15) Direct Customer
  drctCsmNam nVarChar(100) Direct Customer Name
  manufSN nVarChar(36) Mfr Serial No.
  internalSN nVarChar(36) Serial Number
  warranty VarChar(1) Warranty default=N [Y=Yes, N=No]
  wrrntyStrt Date(8) Warranty Start Date
  wrrntyEnd Date(8) Warranty End Date
  responsVal Int(6) Time Required for Response
  responsUnt VarChar(1) Time Unit default=D [H=Hour(s), D=Day(s)]
  itemCode nVarChar(50) Item No. ->OITM
  itemName nVarChar(100) Item Description
  itemGroup Int(6) Item Group ->OITB
  manufDate Date(8) Manufacture Date
  delivery Int(11) Delivery Key ->ODLN
  deliveryNo Int(11) Delivery Number
  invoice Int(11) Invoice Key ->OINV
  invoiceNum Int(11) Invoice Number
  dlvryDate Date(8) Delivery Date
  cntctPhone nVarChar(20) Contact Phone
  street nVarChar(100) Street
  block nVarChar(100) Block
  zip nVarChar(20) Zip Code
  city nVarChar(100) City
  county nVarChar(100) County
  country nVarChar(3) Country ->OCRY
  state nVarChar(3) State ->OCST
  instLction nVarChar(254) Installation Location
  contract Int(11) Contract ->OCTR
  cntrctStrt Date(8) Contract Start Date
  cntrctEnd Date(8) Contract End Date
  attachment Text(16) Attachments
  objType nVarChar(20) Object Type default=176
  logInstanc Int(11) Log Instance
  userSign Int(6) Creating User ->OUSR
  createDate Date(8) Creation Date
  userSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
  Building Text(16) Building/Floor/Room
  status VarChar(1) Status default=A [A=Active, R=Returned, T=Terminated, L=Loaned, I=In Repair Lab]
  replcIns Int(11) The CEC this replaced ->OINS
  repByIns Int(11) The CEC this is replaced by ->OINS
  technician Int(11) Default Technician ->OHEM
  territory Int(11) Default Territory ->OTER
  AtcEntry Int(11) Attachment Entry ->OATC
  Transfered VarChar(1) Year Transfer default=N
  AddrType nVarChar(100) Address Type
  Instance Int(6) Instance default=0
  StreetNo nVarChar(100) Street No.
  BPType VarChar(1) BP Type default=R [R=Sales, P=Purchasing]
  OwnerCode Int(11) Equipment Card Owner ->OHEM
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
