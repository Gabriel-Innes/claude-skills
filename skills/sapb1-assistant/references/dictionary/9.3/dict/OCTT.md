<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCTT - Contract Template
Module: Service | 42 columns | ObjType: 170
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TmpltName
Fields (name type(len) description [values] ->parent table):
  TmpltName nVarChar(20) Template Name
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  Renewal VarChar(1) Renewal default=N [Y=Yes, N=No]
  RemindVal Int(6) Remind Before Renewal
  RemindUnit VarChar(1) Remind Unit default=D [D=Day(s), W=Week(s), M=Month(s)]
  Duration Int(6) Duration of Coverage
  ResponsVal Int(6) Resolution Value
  ResponsUnt VarChar(1) Resolution Unit default=D [D=Day(s), H=Hour(s)]
  Descriptio nVarChar(254) Description
  PriceList Int(6) Price List No.
  CntrctType VarChar(1) Contract Type default=S [C=Customer, G=Item Group, S=Serial Number]
  MonEnabled VarChar(1) Monday Enabled default=Y [Y=Yes, N=No]
  TueEnabled VarChar(1) Tuesday Enabled default=Y [Y=Yes, N=No]
  WedEnabled VarChar(1) Wednesday Enabled default=Y [Y=Yes, N=No]
  ThuEnabled VarChar(1) Thursday Enabled default=Y [Y=Yes, N=No]
  FriEnabled VarChar(1) Friday Enabled default=Y [Y=Yes, N=No]
  SatEnabled VarChar(1) Saturday Enabled default=Y [Y=Yes, N=No]
  SunEnabled VarChar(1) Sunday Enabled default=Y [Y=Yes, N=No]
  MonStart Int(6) Monday Start default=800
  MonEnd Int(6) Monday End default=1700
  TueStart Int(6) Tuesday Start default=800
  TueEnd Int(6) Tuesday End default=1700
  WedStart Int(6) Wednesday Start default=800
  WedEnd Int(6) Wednesday End default=1700
  ThuStart Int(6) Thursday Start default=800
  ThuEnd Int(6) Thursday End default=1700
  FriStart Int(6) Friday Start default=800
  FriEnd Int(6) Friday End default=1700
  SatStart Int(6) Saturday Start default=0
  SatEnd Int(6) Saturday End default=2359
  SunStrart Int(6) Sunday Start default=0
  SunEnd Int(6) Sunday End default=2359
  InclParts VarChar(1) Include Parts default=N [N=No, Y=Yes]
  InclWork VarChar(1) Include Labor default=N [N=No, Y=Yes]
  InclTravel VarChar(1) Include Travel default=N [N=No, Y=Yes]
  Attachment Text(16) Attachments
  CreateDate Date(8) Creation Date
  Remark Text(16) Remarks
  InclHldays VarChar(1) Include Holidays default=N [N=No, Y=Yes]
  ResponseV Int(6) Response Value
  ResponseU VarChar(1) Response Unit default=H [H=Hour(s), D=Day(s)]
  AtcEntry Int(11) Attachment Entry
