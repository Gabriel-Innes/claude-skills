<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WTQ26 - Inventory Transfer Request - E-Way Bill Information
Module: Inventory and Production | 36 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTQ
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=1250000001 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line
