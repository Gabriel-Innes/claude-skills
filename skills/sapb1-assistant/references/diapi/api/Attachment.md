<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Attachment (Object)

The Attachment object represents an external file that is attached to business objects, such as, Contacts, Messages, and ServiceContracts. From DI API version 2005, use the Attachments2 object.

## Properties (1)
- `Public Property FileName() As String` [R/W] Sets or returns the attachment file name.
  - remarks: In SAP Business One, attachments are stored in a file. Use this property to set the file name of the attachment. If you updates an existing record, you can leave this field empty and the specified Attachment item will be deleted in the update process.
