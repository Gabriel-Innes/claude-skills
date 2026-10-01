<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesTaxCodes (Object)

SalesTaxCodes is a business object that represents the inclusive sales tax codes. Each sales tax code consists of one or more sales taxes as defined in SalesTaxAuthorities object. This object enables you to: - Add a sales tax code. - Retrieve a sales tax code by its key. - Update a sales tax code data. - Save the object in XML format. Source table: OSTC.

**Remarks:** Mandatory fields in SAP Business One: ValidForAP and /or ValidForAR must be tYES. To display the form in the application (US and Canada localizations): - Select Administration --> Setup --> Financials --> Tax --> Sales Tax Codes. To display the form in the application (Latin America localization): - Select Administration --> Setup --> Financials --> Tax --> Tax Codes.

## Properties (17)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CFOPIn() As String` [R/W] property CFOPIn
- `Public Property CFOPOut() As String` [R/W] property CFOPOut
- `Public Property Code() As String` [R/W] Sets or returns the tax code. Mandatory in SAP Business One. Field name: Code. Length: 8 characters.
- `Public Property FADebit() As BoYesNoEnum` [R/W] property FADebit
- `Public Property Freight() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to calculate the tax also on expenses, such as shipping expenses. Default: tNO. Field name: Freight.
- `Public Property Inactive() As BoYesNoEnum` [R/W] property Inactive
- `Public Property IsItemLevel() As BoYesNoEnum` [R/W] Indicates whether to apply a jurisdiction's minimum amount, maximum amount, and flat tax thresholds (MinTaxableAmount, MaxTaxableAmount, and FlatTaxAmount properties of the SalesTaxAuthorities object) to the document amount or to each item's amount.
- `Public Property Lines() As SalesTaxCodes_Lines` [R] Returns the SalesTaxCodes_Lines child object.
- `Public Property Name() As String` [R/W] Sets or returns the name of the tax code. Field name: Name. Length: 100 characters.
- `Public Property Rate() As Double` [R] Returns the inclusive tax percentage based on the selected tax authorities/types in SalesTaxCodes_Lines child object. Field name: Rate.
  - remarks: The inclusive rate equals to sum of EffectiveRate specified in each line.
- `Public Property TypeFormulaCombId() As Long` [R/W] property TypeFormulaCombId
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the ID of the user who enters the object's details. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property ValidForAP() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the tax is valid for purchase - A/P. Field name: ValidForAP.
  - remarks: Default: tYES. If you set to tNO, you must set ValidForAR to tYES.
- `Public Property ValidForAR() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the tax is valid for Sales - A/R. Field name: ValidForAR.
  - remarks: Default: tYES. If you set to tNO, you must set ValidForAP to tYES.
- `Public Property VATExemption() As BoYesNoEnum` [R/W] property VATExemption

## Methods (6)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
  - example note: The following sample shows how to add an invoice (with lines) document to the database. Use this sample as a basis for all business objects of document type (not master data type).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
     Sub AddInvoice_Click()

        Dim RetVal As Long

        Dim ErrCode As Long

        Dim ErrMsg As String

        'Create the Documents object

        Dim vInvoice    As SAPbobsCOM.Documents

        Set vInvoice = vCmp.GetBusinessObject(oInvoices)

        'Set values to the fields

        vInvoice.Series = 0

        vInvoice.CardCode = "BP234"

        vInvoice.HandWritten = tNO

        vInvoice.PaymentGroupCode = "-1"

        vInvoice.DocDate = "21/8/2003"

        vInvoice.DocTotal = 264.6

        'Invoice Lines - Set values to the first line

        vInvoice.Lines.ItemCode = "A00023"

        vInvoice.Lines.ItemDescription = "Banana"

        vInvoice.Lines.PriceAfterVAT = 2.36

        vInvoice.Lines.Quantity = 50

        vInvoice.Lines.Currency = "Eur"

        vInvoice.Lines.DiscountPercent = 10

        'Invoice Lines - Set values to the second line

        vInvoice.Lines.Add

        vInvoice.Lines.ItemCode = " A00033"

        vInvoice.Lines.ItemDescription = "Orange"

        vInvoice.Lines.PriceAfterVAT = 118

        vInvoice.Lines.Quantity = 1

        vInvoice.Lines.Currency = "Eur"

        vInvoice.Lines.DiscountPercent = 10

        'Add the Invoice

        RetVal = vInvoice.Add

       'Check the result

        If RetVal <> 0 Then

            vCmp.GetLastError ErrCode, ErrMsg

            MsgBox ErrCode & " " & ErrMsg

        End If

     End Sub
    ```
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal Key As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `Key`: (Code).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
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
