<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BPFiscalRegistryID (Object)

BPFiscalRegistryID is a data structure related to the BusinessPartnersService. BPFiscalRegistryID describes the type of the company's business activity (this information is required in some Brazilian legal reports). Moreover, government use the information to calculate the percentage of the companies related to a certain economic activity. This object enables you to add the Fiscal Registry ID for companies or business partners. Source table: OCNA.

**Remarks:** - This Object is specific to Cluster 2B (Country specific property for Brazil only). - The Term 4SS refers to the document repository, RDF model and related services. - 4SS stands for 4 Suite Server, appears in some documents and throughout the software.

## Properties (5)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CNAECode() As String` [R/W] Sets or returns the business partner CNAE (Change Notification Agent) Code. Field name: CNAECode. Length: 9 characters.
- `Public Property Description() As String` [R/W] Sets or returns the business partner's fiscal description. Field name: Descrip. Length: 64,000 characters.
- `Public Property Numerator() As Long` [R] Returns the absolute entry of the fiscal registry Id. Field name: AbsId.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a new record to the OCNA table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal lGroupCode As Long) As Boolean` Retrieves the values of the object's properties by the object's absolute key from the Company database.
  - param `lGroupCode`: Specifies the required object's properties according to object's absolute key in Company database.
- `Public Function Remove() As Long` method Remove
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
