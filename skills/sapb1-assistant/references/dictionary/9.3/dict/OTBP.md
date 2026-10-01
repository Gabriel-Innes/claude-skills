<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTBP - Target Group Business Partner
Module: Business Partners | 16 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code
  CardName nVarChar(100) BP Name
  CntctPrsn nVarChar(90) Contact Person
  Title nVarChar(10) Title
  Position nVarChar(90) Position
  E_Mail nVarChar(100) E-Mail
  Telephone nVarChar(20) Telephone
  Cellolar nVarChar(50) Mobile Phone
  Fax nVarChar(20) Fax
  Address nVarChar(100) Address
  Street nVarChar(100) Street/PO Box
  Block nVarChar(100) Block
  City nVarChar(100) City
  ZipCode nVarChar(20) Zip Code
  County nVarChar(100) County
  Building nVarChar(100) Building/Floor/Room
