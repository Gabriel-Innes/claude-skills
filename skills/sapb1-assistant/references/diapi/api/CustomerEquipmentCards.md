<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CustomerEquipmentCards (Object)

CustomerEquipmentCards is a business object that represents the customer equipment cards in the Services module. This object enables you to: - Add a customer equipment card. - Retrieve a customer equipment card by its key. - Update a customer equipment card. - Remove a customer equipment card. - Save the object in XML format. Source table: OINS.

**Remarks:** Mandatory fields in SAP Business One: ManufacturerSerialNum or InternalSerialNum (according to the definition of Unique Number in the General Settings in SAP Business One - SriUniqFld field in OADM table), ItemCode, and CustomerCode. To display the form in the application: - Select Service --> Customer Equipment Card.

## Properties (37)
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the identification key of the Attachment File as assigned by SAP Business One when adding an attachment file. Field name: AtcEntry. This is a foreign key to the Territories object. Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to alert message. Field name: AtcEntry.
- `Public Property Attachments() As Attachments` [R] Returns the Attachments object.
- `Public Property Block() As String` [R/W] Sets or returns the block name in the address where the service is provided. Field name: block. Length: 100 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property BuildingFloorRoom() As String` [R/W] Sets or returns the additional address details, such as building number, floor number, and room number. Field name: Building. Length: 64,000 characters.
- `Public Property BusinessPartners() As CustomerEquipmentCards_BusinessPartners` [R] property BusinessPartners
- `Public Property City() As String` [R/W] Sets or returns the city name in the address where the service is provided. Field name: city. Length: 100 characters.
- `Public Property ContactEmployeeCode() As Long` [R/W] Sets or returns the code of the contact person. Field name: contactCod. This is a foreign key to the ContactEmployees object.
- `Public Property ContactPhone() As String` [R] Returns the phone number of the contact person. Field name: cntctPhone. Length: 50 characters.
- `Public Property CountryCode() As String` [R/W] Sets or returns the country code in the address where the service is provided. Field name: country. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property County() As String` [R/W] Sets or returns the county name in the address where the service is provided. Field name: county. Length: 100 characters.
- `Public Property CustomerCode() As String` [R/W] Sets or returns the customer code. Field name: customer. Mandatory field in SAP Business One. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property CustomerName() As String` [R/W] Sets or returns the customer name. Field name: custmrName. Length: 100 characters.
- `Public Property DefaultTechnician() As Long` [R/W] Sets or returns the default technician for this customer equipment card as defined in the technicians table. Field name: technician. This is a foreign key to the EmployeesInfo object.
- `Public Property Defaultterritory() As Long` [R/W] Sets or returns the default territory for this customer equipment card as defined in the territories table. Field name: territory. This is a foreign key to the Territories object.
- `Public Property DeliveryCode() As Long` [R/W] Sets or returns the code of the delivery note document. Field name: delivery. This is a foreign key to the Documents object.
- `Public Property DeliveryDate() As Date` [R] Returns the delivery date of the item. Field name: dlvryDate.
- `Public Property DeliveryNumber() As Long` [R] Returns the number of the delivery note document. Field name: deliveryNo.
- `Public Property DirectCustomerCode() As String` [R/W] Sets or returns the code of the customer that bought the item. Field name: directCsmr. Length: 15 characters.
- `Public Property DirectCustomerName() As String` [R/W] Sets or returns the name of the customer that bought the item. Field name: custmrName. Length: 100 characters.
- `Public Property EquipmentCardNum() As Long` [R] Returns the equipment card ID. Field name: insID.
- `Public Property InstallLocation() As String` [R/W] Sets or returns the location where the item is installed. Field name: instLction. Length: 254 characters.
- `Public Property InternalSerialNum() As String` [R/W] Sets or returns the unique internal serial number of the item. Field name: internalSN. Mandatory field in SAP Business One in one of the following cases: - If you do not set the ManufacturerSerialNum property. - From version 2004, if the definition of Unique Number in General Settings in SAP Business One is Serial Number. Length: 32 characters.
- `Public Property InvoiceCode() As Long` [R/W] Sets or returns the invoice code. Field name: invoice. This is a foreign key to the Documents object.
- `Public Property InvoiceNumber() As Long` [R] Returns the invoice number. Field name: invoiceNum.
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code. Field name: itemCode. Mandatory field in SAP Business One. Length: 20 characters.Items
- `Public Property ItemDescription() As String` [R/W] Sets or returns the item description. Field name: itemName. Length: 100 characters.
- `Public Property ManufacturerSerialNum() As String` [R/W] Sets or returns the unique manufacturer serial number of the item. Field name: manufSN. Mandatory field in SAP Business One in one of the following cases: - If you do not set the InternalSerialNum property. - From version 2004, if the definition of Unique Number in General Settings in SAP Business One is Man. Serial No. Length: 32 characters.
- `Public Property ReplacedBySN() As Long` [R/W] Sets or returns the S/N of the replacement equipment (Replaced By S/N) that replaced the equipment of the Replace S/N equipment card. This enables concatenation of replacement equipments. Field name: repByIns. This is a foreign key to the CustomerEquipmentCards object.
- `Public Property ReplaceSN() As Long` [R/W] Sets or returns the S/N of the replacement equipment (Replace S/N) that replaced the equipment of the current equipment card. Field name: replcIns. This is a foreign key to the CustomerEquipmentCards object.
- `Public Property ServiceBPType() As BoEquipmentBPType` [R/W] Sets or returns the service BP type, whether your company provides support services to its customers, or receives support services from your vendors. Field name: BPType.
- `Public Property StateCode() As String` [R/W] Sets or returns the state code where the service is provided. Field name: State. Length: 3 characters. This is a foreign key to the States table (OCST), which is not exposed through the DI API.
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property StatusOfSerialNumber() As BoSerialNumberStatus` [R/W] Sets or returns a valid value of BoSerialNumberStatus type that specifies the current location of the equipment, for example at the customer premises, in the lab, and so on. Field name: status.
- `Public Property Street() As String` [R/W] Sets or returns the street name in the address where the service is provided. Field name: Street. Length: 100 characters.
- `Public Property StreetNo() As String` [R/W] Sets or returns the street number in the address where the service is provided. Field name: Street No. Length: 100 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property ZipCode() As String` [R/W] Sets or returns the zip code in the address where the service is provided. Field name: zip. Length: 20 characters.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal EquipmentCardNum As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `EquipmentCardNum`: Specifies the equipment card number in the database.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Not supported.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
