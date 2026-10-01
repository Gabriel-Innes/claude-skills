<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BPAddresses (Object)

BPAddresses is a child object of the BusinessPartners and represents the Ship To and Bill To addresses list of the business partner. This object is part of the Business Partner module. You can retrieve or set this object by using the Addresses property of the BusinessPartners object. This object enables you to add Ship To, Bill To, and multiple addresses to the business partner master data. Source table: CRD1.

**Remarks:** Mandatory field in SAP Business One: AddressName. To display the form in the application: - Select Business Partners --> Business Partner Master Data --> Addresses tab.

**Example:**
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  Dim bp As SAPbobsCOM.BusinessPartners

  Set bp = DIcompany.GetBusinessObject(oBusinessPartners)

  Dim bpA As SAPbobsCOM.BPAddresses

  Set bpA = bp.Addresses

  bp.CardName = "C009"

  bp.CardCode = "C009"

  bp.CardType = SAPbobsCOM.BoCardTypes.cCustomer

  bp.Addresses.AddressName = "Address1"

  bp.Addresses.Block = "1"

  bp.Addresses.Street = "street 1"

  bp.Addresses.City = "City 1"

  bp.Addresses.Country = "DE"

  bp.Addresses.AddressType = SAPbobsCOM.BoAddressType.bo_BillTo

  bp.Addresses.Add

  bp.Addresses.AddressName = "Address2"

  bp.Addresses.Block = "2"

  bp.Addresses.Street = "street 2"

  bp.Addresses.City = "City 2"

  bp.Addresses.Country = "DE"

  bp.Addresses.AddressType = SAPbobsCOM.BoAddressType.bo_BillTo

  bp.Addresses.Add

  bp.Addresses.AddressName = "Address3"

  bp.Addresses.Block = "3"

  bp.Addresses.Street = "street 3"

  bp.Addresses.City = "City 3"

  bp.Addresses.Country = "DE"

  bp.Addresses.AddressType = SAPbobsCOM.BoAddressType.bo_BillTo

  bp.Addresses.Add

  bp.Add

  bp.GetByKey ("C009")

  Set bpA = bp.Addresses

  bpA.SetCurrentLine (1)
  ```

## Properties (29)
- `Public Property AddressName() As String` [R/W] Sets or returns the name of the address (Bill To address, Main address, Ship To address, and so on). Field name: Address. Mandatory property. Length: 50 characters.
- `Public Property AddressName2() As String` [R/W] Sets or returns the BP second, alternative Address. Field name: Address2. Length: 50 characters.
- `Public Property AddressName3() As String` [R/W] Sets or returns the BP third, alternative Address. Field name: Address3. Length: 50 characters.
- `Public Property AddressType() As BoAddressType` [R/W] Sets or returns a valid value of BoAddressType type that specifies the type of the business partner's address: Ship To or Bill To. Field name: AdresType.
  - remarks: Default address type: Ship To.
- `Public Property Block() As String` [R/W] Sets or returns the block address. Field name: Block. Length: 100 characters.
- `Public Property BPCode() As String` [R] The key to the current object's parent business partner.
- `Public Property BuildingFloorRoom() As String` [R/W] Sets or returns the additional address details, such as building number, floor number, and room number. Field name: Building. Length: 64,000 characters.
- `Public Property City() As String` [R/W] Sets or returns the city. Field name: City. Length: 100 characters.
- `Public Property Count() As Long` [R] Returns the number of addresses in the object.
- `Public Property Country() As String` [R/W] Sets or returns the country code (for example, DE). Field name: City. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
  - remarks: You can set any country code that is defined in the Countries table (OCRY - not exposed through the DI API).
- `Public Property County() As String` [R/W] Sets or returns the county. Field name: County. Length: 100 characters.
- `Public Property CreateDate() As Date` [R] property CreateDate
- `Public Property CreateTime() As Date` [R] property CreateTime
- `Public Property FederalTaxID() As String` [R/W] Sets or returns the federal tax ID of the business partner. Field name: LicTradNum. Length: 32 characters.
- `Public Property GlobalLocationNumber() As String` [R/W] property GlobalLocationNumber
- `Public Property GSTIN() As String` [R/W] property GSTIN
- `Public Property GstType() As BoGSTRegnTypeEnum` [R/W] property GstType
- `Public Property MYFType() As BoMYFTypeEnum` [R/W] property MYFType
- `Public Property Nationality() As String` [R/W] property Nationality
- `Public Property RowNum() As Long` [R] The line number within the lines of the current object's parent business partner.
- `Public Property State() As String` [R/W] Sets or returns the state code of the business partner. Field name: State. Length: 3 characters. This is a foreign key to the States table (OCST), which is not exposed through the DI API.
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property Street() As String` [R/W] Sets or returns the street of the business partner address. Field name: Street. Length: 100 characters.
- `Public Property StreetNo() As String` [R/W] The street number. Field name: StreetNo
  - remarks: For Brazil only.
- `Public Property TaasEnabled() As BoYesNoEnum` [R/W] property TaasEnabled
- `Public Property TaxCode() As String` [R/W] Sets or returns the sales tax code. Field name: TaxCode. Length: 8 characters.
  - remarks: Country-specific property for USA. The tax code represents the sales tax related to specific locations where the business transaction occurs. Tax codes are defined in SAP Business One.
- `Public Property TaxOffice() As String` [R/W] property TaxOffice
- `Public Property TypeOfAddress() As String` [R/W] The address type. Field name: AddrType
  - remarks: For Brazil only.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property ZipCode() As String` [R/W] Sets or returns the zip code. Field name: ZipCode. Length: 20 characters.

## Methods (3)
- `Public Sub Add()` Adds a new Address record. To save the information to the database, use the Add method in the BusinessPartners object.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.BusinessPartners oBP;

    // Delete BP address
    if (oBP.GetByKey("11") == true)
    {
        oBP.Addresses.SetCurrentLine(2);
        oBP.Addresses.Delete();
        oBP.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
