<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BoXmlExportTypes (Enumeration)

Defines the type for exporting an object to XML.

| Member | Value | Description |
|---|---|---|
| xet_AllNodes | 0 | Export to XML all fields (both read only and read/write fields) from the database. (XML files exported using this type cannot be read by the ReadXml method.) |
| xet_ValidNodesOnly | 1 | Export to XML only valid fields that support XML import (read/write fields only) from the database. (XML files exported using this type cannot be read by the ReadXml method.) |
| xet_NodesAsProperties | 2 | Export to XML all fields as properties from the database. (XML files exported using this type cannot be read by the ReadXml method.) |
| xet_ExportImportMode | 3 | Export to XML only valid fields that support XML import and export (read/write fields only that do not contain null values) from the database. (XML files exported using this type can be read by the ReadXml method.) |
