<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ContactEmployees (Object)

ContactEmployees is a business object that represents the contact employees in the Business Partners module. This object enables you to add contact information of employees to the Business Partners master record. Source table: OCPR.

**Remarks:** Mandatory fields in SAP Business One: Name. To display the form in the application: - Select Business Partners --> Business Partner Master Data --> Contact Persons tab.

## Properties (36)
- `Public Property Active() As BoYesNoEnum` [R/W] Indicates whether or not the contact person for a particular business partner is available for selection in transactions.
- `Public Property Address() As String` [R/W] Sets or returns the employee address. Field name: Address. Length: 100 characters.
- `Public Property BlockSendingMarketingContent() As BoYesNoEnum` [R/W] Specifies whether or not to block sending marketing contnet to the contact employee. Field name: BlockComm. Length: 1 character.
- `Public Property CardCode() As String` [R] Returns the business partner identification number. Field name: CardCode. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property CityOfBirth() As String` [R/W] Sets or returns the city of birth of the employee. Field name: BirthCity. Length: 100 characters.
- `Public Property ConnectedAddressName() As String` [R/W] Description of the connected address. Field name: CnnectAddr. Length: 50 characters.
- `Public Property ConnectedAddressType() As BoAddressType` [R/W] Type of the connected address: B stands for bill to or pay to address; S stands for ship to address. Field name: CnAddrType.
- `Public Property ContactEmployeeBlockSendingMarketingContents() As ContactEmployeeBlockSendingMarketingContents` [R] Returns the ContactEmployeeBlockSendingMarketingContents object.
- `Public Property Count() As Long` [R] Returns the number of contact employees included in the object.
- `Public Property CreateDate() As Date` [R] property CreateDate
- `Public Property CreateTime() As Date` [R] property CreateTime
- `Public Property DateOfBirth() As Date` [R/W] Sets or returns the employee birth date. Field name: BirthDate.
- `Public Property E_Mail() As String` [R/W] Sets or returns the e-mail address of the contact employee. Field name: E_MailL. Length: 100 characters.
- `Public Property EmailGroupCode() As String` [R/W] property EmailGroupCode
- `Public Property Fax() As String` [R/W] Sets or returns the fax number of the contact employee. Field name: Fax. Length: 50 characters.
- `Public Property FirstName() As String` [R/W] property FirstName
- `Public Property ForeignCountry() As String` [R/W] Field name: Frgncntry. Length: 3 characters.
  - remarks: For the Italy localization only, field "Stato Estero".
- `Public Property Gender() As BoGenderTypes` [R/W] Sets or returns a valid value of BoGenderTypes that specifies the employee gender. Field name: Gender.
- `Public Property InternalCode() As Long` [R] Returns the internal code of the contact employee. Field name: CntctCode.
- `Public Property LastName() As String` [R/W] property LastName
- `Public Property MiddleName() As String` [R/W] property MiddleName
- `Public Property MobilePhone() As String` [R/W] Sets or returns the employee mobile phone number. Field name: Cellolar. Length: 50 characters.
- `Public Property Name() As String` [R/W] Sets or returns the employee name. Field name: Name. Mandatory property. Length: 50 characters.
- `Public Property Pager() As String` [R/W] Sets or returns the pager number of the employee. Field name: Pager. Length: 30 characters.
- `Public Property Password() As String` [R/W] Sets or returns the employee access password to e-commerce applications. Field name: Password. Length: 8 characters.
  - remarks: This property is used for B2C and B2B systems.
- `Public Property Phone1() As String` [R/W] Sets or returns the primary phone number of the employee. Field name: Tel1. Length: 50 characters.
- `Public Property Phone2() As String` [R/W] Sets or returns the secondary phone number of the employee. Field name: Tel2. Length: 50 characters.
- `Public Property PlaceOfBirth() As String` [R/W] Sets or returns the country of birth of the employee. Field name: BirthPlace. Length: 100 characters.
- `Public Property Position() As String` [R/W] Sets or returns the employee position in the company. Field name: Position. Length: 90 characters.
- `Public Property Profession() As String` [R/W] Sets or returns the employee profession. Field name: Profession. Length: 50 characters.
- `Public Property Remarks1() As String` [R/W] Sets or returns remarks for the employee. Field name: Notes1. Length: 100 characters.
- `Public Property Remarks2() As String` [R/W] Sets or returns secondary remarks for the employee. Field name: Notes2. Length: 100 characters.
- `Public Property Title() As String` [R/W] Sets or returns the Contact Employee's Title. Field name: Title. Field name: Title. Length: 10 characters.
- `Public Property UpdateDate() As Date` [R] property UpdateDate
- `Public Property UpdateTime() As Date` [R] property UpdateTime
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a new contact employee.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: To save the information to the database, use the BusinessPartners object, Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - remarks: If you delete the default contact employee, the first contact employee in the remaining list becomes the default.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.BusinessPartners oBP;

    // Delete contact employee
    if (oBP.GetByKey("BP1") == true)
    {
        oBP.ContactEmployees.SetCurrentLine(0);
        oBP.ContactEmployees.Delete();
        oBP.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
