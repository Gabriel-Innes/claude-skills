<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCHP - India Chapter ID
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CHAPTERID U: ChapterID
  CHAPTER: SubHeading, Heading, Chapter
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  Chapter nVarChar(20) Chapter
  Heading nVarChar(20) Tariff Heading
  SubHeading nVarChar(20) Tariff Subheading
  Dscription nVarChar(120) Description for Tariff Heading
  ChapterID nVarChar(64) Chapter ID
