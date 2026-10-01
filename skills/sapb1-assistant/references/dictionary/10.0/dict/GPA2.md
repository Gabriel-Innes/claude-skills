<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GPA2 - Gross Profit Adjustments - Parameters
Module: Marketing Documents | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  Name nVarChar(100) Wizard Parameters Name
  Descript nVarChar(100) Wizard Parameters Description
  PostDateFr Date(8) Sales Doc. Posting Date From
  PostDateTo Date(8) Sales Doc. Posting Date To
  ItemCodeFr nVarChar(50) Item No. From
  ItemCodeTo nVarChar(50) Item No. To
  ItmsGrpCod Int(6) Item Group default=100 ->OITB
  AdditFilt VarChar(1) Additional Filters
  SearchCond VarChar(1) Find Items Search Condition
  PropList nVarChar(100) Item Properties List
  DisplInact VarChar(1) Display Inactive Items
  UseGroups VarChar(1) Find items with only the selected properties
