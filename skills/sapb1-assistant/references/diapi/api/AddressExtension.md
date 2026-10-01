<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AddressExtension (Object)

The Bill To and Ship To address for a marketing document. Source table: INV12

**Example:**
- C# example (from SAP's help):
  ```csharp
  // Get Invoice document
  m_Doc = (SAPbobsCOM.Documents)m_Company.GetBusinessObject(BoObjectTypes.oInvoices);
  m_Doc.GetByKey(4);

  // Get the address sub object from the document object
  m_AddrExtension = (AddressExtension)m_Doc.AddressExtension;

  // Set bill to address properties
  m_AddrExtension.BillToBlock = "BillToBlockU";
  m_AddrExtension.BillToBuilding = "BillToBuildingU";
  m_AddrExtension.BillToCity = "BillToCityU";
  m_AddrExtension.BillToCountry = "BCU";
  m_AddrExtension.BillToCounty = "BUt";
  m_AddrExtension.BillToState = "BSU";
  m_AddrExtension.BillToStreet = "BillToStreetU";
  m_AddrExtension.BillToStreetNo = "BillToStreetNoU";
  m_AddrExtension.BillToZipCode = "BillToZipCodeU";
  m_AddrExtension.BillToAddressType = "BillToAddressTypeU";

  // Set ship to address properties
  m_AddrExtension.ShipToBlock = "ShipToBlockU";
  m_AddrExtension.ShipToBuilding = "ShipToBuildingU";
  m_AddrExtension.ShipToCity = "ShipToCityU";
  m_AddrExtension.ShipToCountry = "SCU";
  m_AddrExtension.ShipToCounty = "SUt";
  m_AddrExtension.ShipToState = "SUt";
  m_AddrExtension.ShipToStreet = "ShipToStreetU";
  m_AddrExtension.ShipToStreetNo = "ShipToStreetNoU";
  m_AddrExtension.ShipToZipCode = "ShipToZipCodeU";

  // Update the document
  m_Doc.Update();
  ```

## Properties (60)
- `Public Property BillToAddress2() As String` [R/W] property BillToAddress2
- `Public Property BillToAddress3() As String` [R/W] property BillToAddress3
- `Public Property BillToAddressType() As String` [R/W] The address type for the Bill To address. For Brazil only. Field name: AddrTypeB
- `Public Property BillToBlock() As String` [R/W] The block of the Bill To address. Field name: BlockB
- `Public Property BillToBuilding() As String` [R/W] The building of the Bill To address. Field name: BuildingB
- `Public Property BillToCity() As String` [R/W] The city of the Bill To address. Field name: CityB
- `Public Property BillToCountry() As String` [R/W] The country of the Bill To address. Field name: CountryB
  - remarks: Enter the 2- or 3-character country code; a list is available in the Code field of the OCRY table.
- `Public Property BillToCounty() As String` [R/W] The county of the Bill To address. Field name: CountyB
- `Public Property BillToGlobalLocationNumber() As String` [R/W] property BillToGlobalLocationNumber
- `Public Property BillToState() As String` [R/W] The state of the Bill To address. Field name: StateB
- `Public Property BillToStreet() As String` [R/W] The street of the Bill To address. Field name: StreetB
- `Public Property BillToStreetNo() As String` [R/W] The street number of the Bill To address. Field name: StreetNoB
- `Public Property BillToZipCode() As String` [R/W] The zip code of the Bill To address. Field name: ZipCodeB
- `Public Property DeliveryPlaceBlock() As String` [R/W] Delivery Place Block. Field name: BlckDlvryP. Length: 100 characters.
- `Public Property DeliveryPlaceBP() As String` [R/W] Delivery Place BP. Field name: BPDelivryP. Length: 15 characters.
- `Public Property DeliveryPlaceBuilding() As String` [R/W] Delivery Place Building. Field name: BldDlvryP. Length: 16 characters.
- `Public Property DeliveryPlaceCity() As String` [R/W] Delivery Place City. Field name: CityDlvryP. Length: 100 characters.
- `Public Property DeliveryPlaceCNPJ() As String` [R/W] Delivery Place CNPJ. Field name: CNPJDlvryP. Length: 100 characters.
- `Public Property DeliveryPlaceCountry() As String` [R/W] Delivery Place Country. Field name: CtryDlvryP. Length: 3 characters.
- `Public Property DeliveryPlaceCounty() As String` [R/W] Delivery Place County. Field name: CntyDlvryP. Length: 100 characters.
- `Public Property DeliveryPlaceCPF() As String` [R/W] Delivery Place CPF. Field name: CPFDlvryP. Length: 100 characters.
- `Public Property DeliveryPlaceDepartureDate() As String` [R/W] Delivery Place Departure Date. Field name: DpDtDlvryP. Length: 8 characters.
- `Public Property DeliveryPlaceEMail() As String` [R/W] Delivery Place E-Mail. Field name: MailDlvryP. Length: 100 characters.
- `Public Property DeliveryPlacePhone() As String` [R/W] Delivery Place Phone. Field name: FoneDlvryP. Length: 50 characters.
- `Public Property DeliveryPlaceState() As String` [R/W] Delivery Place State. Field name: StatDlvryP. Length: 3 characters.
- `Public Property DeliveryPlaceStreet() As String` [R/W] Delivery Place Street. Field name: StrtDlvryP. Length: 100 characters.
- `Public Property DeliveryPlaceStreetNo() As String` [R/W] Delivery Place Street Number. Field name: StrNoDlvrP. Length: 100 characters.
- `Public Property DeliveryPlaceZip() As String` [R/W] Delivery Place Zip Code. Field name: ZipDlvryP. Length: 20 characters.
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property GoodsIssuePlaceBlock() As String` [R/W] Goods Issue Place Block. Field name: BlockGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceBP() As String` [R/W] Goods Issue Place BP. Field name: BPGdsIssP. Length: 15 characters.
- `Public Property GoodsIssuePlaceBuilding() As String` [R/W] Goods Issue Place Building. Field name: BldngGIP. Length: 16 characters.
- `Public Property GoodsIssuePlaceCity() As String` [R/W] Goods Issue Place City. Field name: CityGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceCNPJ() As String` [R/W] Goods Issue Place CNPJ. Field name: CNPJGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceCountry() As String` [R/W] Goods Issue Place Country. Field name: CountryGIP. Length: 3 characters.
- `Public Property GoodsIssuePlaceCounty() As String` [R/W] Goods Issue Place County. Field name: CountyGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceCPF() As String` [R/W] Goods Issue Place CPF. Field name: CPFGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceDepartureDate() As String` [R/W] Goods Issue Place Departure Date. Field name: DptDateGIP. Length: 8 characters.
- `Public Property GoodsIssuePlaceEMail() As String` [R/W] Goods Issue Place E-Mail. Field name: EMailGIP. Length: 100 characters.
- `Public Property GoodsIssuePlacePhone() As String` [R/W] Goods Issue Place Telephone. Field name: PhoneGIP. Length: 50 characters.
- `Public Property GoodsIssuePlaceState() As String` [R/W] Goods Issue Place State. Field name: StateGIP. Length: 3 characters.
- `Public Property GoodsIssuePlaceStreet() As String` [R/W] Goods Issue Place Street. Field name: StreetGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceStreetNo() As String` [R/W] Goods Issue Place Street Number. Field name: StrtNoGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceZip() As String` [R/W] Goods Issue Place Zip Code. Field name: ZipGIP. Length: 20 characters.
- `Public Property PlaceOfSupply() As String` [R/W] property PlaceOfSupply
- `Public Property PurchasePlaceOfSupply() As String` [R/W] property PurchasePlaceOfSupply
- `Public Property ShipToAddress2() As String` [R/W] property ShipToAddress2
- `Public Property ShipToAddress3() As String` [R/W] property ShipToAddress3
- `Public Property ShipToAddressType() As String` [R/W] The address type for the Ship To address. For Brazil only. Field name: AddrTypeS
- `Public Property ShipToBlock() As String` [R/W] The block of the Ship To address. Field name: BlockS
- `Public Property ShipToBuilding() As String` [R/W] The building of the Ship To address. Field name: BuildingS
- `Public Property ShipToCity() As String` [R/W] The city of the Ship To address. Field name: CityS
- `Public Property ShipToCountry() As String` [R/W] The country of the Ship To address. Field name: CountryS
  - remarks: Enter the 2- or 3-character country code; a list is available in the Code field of the OCRY table.
- `Public Property ShipToCounty() As String` [R/W] The county of the Ship To address. Field name: CountyS
- `Public Property ShipToGlobalLocationNumber() As String` [R/W] property ShipToGlobalLocationNumber
- `Public Property ShipToState() As String` [R/W] The state of the Ship To address. Field name: StateS
- `Public Property ShipToStreet() As String` [R/W] The street of the Ship To address. Field name: StreetS
- `Public Property ShipToStreetNo() As String` [R/W] The street number of the Ship To address. Field name: StreetNoS
- `Public Property ShipToZipCode() As String` [R/W] The zip code of the Ship To address. Field name: ZipCodeS
- `Public Property UserFields() As UserFields` [R] property UserFields
