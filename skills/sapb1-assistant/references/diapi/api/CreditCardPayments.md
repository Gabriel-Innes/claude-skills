<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CreditCardPayments (Object)

The CreditCardPayments object enables to define dates for incoming payments from the credit card company. Source table: OCDT.

**Remarks:** Mandatory fields in SAP Business One: DueDateCode. To display the form in the application: - Select Administration --> Setup --> Banking --> Credit Card Payment.

## Properties (23)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DueDateCode() As String` [R/W] Sets or returns the code of the credit card due date payments. Field name: Code. Mandatory property. Length: 8 characters.
- `Public Property DueDateName() As String` [R/W] Sets or returns the name of the credit card due date payments. Field name: Name. Length: 30 characters.
- `Public Property DueDatesType() As DueDateTypesEnum` [R/W] Determines whether the payment due dates are based on ddtAfterTimePeriod (after number of days and months) or ddtByDates (voucher date of receipt). Field name: TERM_TYPE.
  - remarks: If you set ddtAfterTimePeriod (default), then you must set the PaymentAfterDays (PaymentAfterMonths is not mandatory). If you set ddtByDates, then you must set the due dates for payment from day 1 to day 31 of the month. You can split the month period to maximum four periods. The payment day must be within the period. For example: Voucher Date of Receipt Payment On Day FromDay1 = 1, ToDay1 = 7, PaymentDate1 = 10, (NoofMonths1 is not mandatory). FromDay2 = 8, ToDay2 = 15, PaymentDate2 = 20, (NoofMonths2 is not mandatory). FromDay3 = 16, ToDay3 = 23, PaymentDate3 = 25, (NoofMonths3 is not mandatory). FromDay4 = 24, ToDay4 = 31, PaymentDate4 = 30, (NoofMonths4 is not mandatory).
- `Public Property FromDay1() As Long` [R/W] Sets or returns the beginning day of the first period of voucher receipt. Field name: Day_From1.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property FromDay2() As Long` [R/W] Sets or returns the begining day of the second period of voucher receipt. Field name: Day_From2.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property FromDay3() As Long` [R/W] Sets or returns the begining day of the third period of voucher receipt. Field name: Day_From3.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property FromDay4() As Long` [R/W] Sets or returns the begining day of the fourth period of voucher receipt. Field name: Day_From4.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property NoOfMonths1() As Long` [R/W] Sets or returns the number of months to add to PaymentDay1. Field name: Pay_Month1.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property NoOfMonths2() As Long` [R/W] Sets or returns the number of months to add to PaymentDay2. Field name: Pay_Month2.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property NoOfMonths3() As Long` [R/W] Sets or returns the number of months to add to PaymentDay3. Field name: Pay_Month3.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property NoOfMonths4() As Long` [R/W] Sets or returns the number of months to add to PaymentDay4. Field name: Pay_Month4.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property PaymentAfterDays() As Long` [R/W] Sets or returns the number of days for payment after the voucher receipt. Field name: After_Days.
  - remarks: Applicable when DueDatesType is set to ddtAfterTimePeriod.
- `Public Property PaymentAfterMonths() As Long` [R/W] Sets or returns the number of months to add to PaymentAfterDays. Field name: After_Mnth.
  - remarks: Applicable when DueDatesType is set to ddtAfterTimePeriod.
- `Public Property PaymentDay1() As Long` [R/W] Sets or returns the payment day in the first payment period. For example, if the first payment period is from day 1 to day 7, the payment day can be 1 - 7. Field name: Pay_Day1.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property PaymentDay2() As Long` [R/W] Sets or returns the payment day in the second payment period. For example, if the first payment period is from day 8 to day 15, the payment day can be 8 - 15. Field name: Pay_Day2.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property PaymentDay3() As Long` [R/W] Sets or returns the payment day in the third payment period. Field name: Pay_Day3. For example, if the first payment period is from day 16 to day 24, the payment day can be 16 - 24.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property PaymentDay4() As Long` [R/W] Sets or returns the payment day in the forth payment period. Field name: Pay_Day4. For example, if the first payment period is from day 25 to day 31, the payment day can be 25 - 31.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property ToDay1() As Long` [R/W] Sets or returns the ending day of the first period of voucher receipt. Field name: Day_To1.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property ToDay2() As Long` [R/W] Sets or returns the ending day of the second period of voucher receipt. Field name: Day_To2.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property ToDay3() As Long` [R/W] Sets or returns the ending day of the third period of voucher receipt. Field name: Day_To3.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property ToDay4() As Long` [R/W] Sets or returns the ending day of the fourth period of voucher receipt. Field name: Day_To4.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a credit card due date payments definition.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrCode`: DueDateCode.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
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
