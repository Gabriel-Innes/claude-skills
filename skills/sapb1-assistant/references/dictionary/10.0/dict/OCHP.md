<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCHP - India Chapter ID
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CHAPTERID U: ChapterID
  CHAPTER: Chapter, Heading, SubHeading
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  Chapter nVarChar(20) Chapter
  Heading nVarChar(20) Tariff Heading
  SubHeading nVarChar(20) Tariff Subheading
  Dscription nVarChar(120) Description for Tariff Heading
  ChapterID nVarChar(64) Chapter ID
