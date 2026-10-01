<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BlanketAgreement (Object)

A blanket agreement is a longer-term arrangement between a purchasing organization and a vendor, or a sales organization and a customer, for the supply of items or provision of services over a period of time based on predefined terms and conditions. If an approved and valid blanket agreement exists with a customer or vendor, SAP Business One automatically links sales and purchasing documents with the blanket agreement. As such, the prices agreed on with the business partners are automatically copied into the sales and purchasing document. You can also choose to remove the link and create a sales or purchasing document that is not governed by a blanket agreement. Source table: OOAT.

## Properties (37)
- `Public Property AgreementMethod() As BlanketAgreementMethodEnum` [R/W] property AgreementMethod
- `Public Property AgreementNo() As Long` [R] Sequential number of the agreement that is assigned automatically by SAP Business One. Field name: AbsID.
- `Public Property AgreementType() As BlanketAgreementTypeEnum` [R/W] The type (category) of the agreement you have made with your business partner. Field name: Type.
- `Public Property AmendmentTo() As Long` [R/W] property AmendmentTo
- `Public Property AttachmentEntry() As Long` [R/W] The file path of the agreement document that you want to attach to the blanket agreement. Field name: AtchEntry. Length: 11 characters.
- `Public Property BlanketAgreements_ItemsLines() As BlanketAgreements_ItemsLines` [R] The items that can be purchased or sold within the scope of the blanket agreement.
- `Public Property BPCode() As String` [R/W] Code of the business partner with whom you have made the agreement. Field name: BpCode. Length: 15 characters.
- `Public Property BPCurrency() As String` [R/W] property BPCurrency
- `Public Property BPName() As String` [R] Name of the business partner with whom you have made the agreement. Field name: BpName.
- `Public Property ContactPersonCode() As Long` [R/W] Code of the contact person. Field name: CntctCode. Length: 11 characters.
- `Public Property Description() As String` [R/W] Descriptive text for the agreement. Field name: Descript. Length: 254 characters.
- `Public Property DocNum() As Long` [R/W] property DocNum
- `Public Property EndDate() As Date` [R/W] Date until which the agreement is effective. Field name: EndDate.
- `Public Property ExchangeRate() As Double` [R/W] property ExchangeRate
- `Public Property HandWritten() As BoYesNoEnum` [R/W] property HandWritten
- `Public Property IgnorePricesInAgreement() As BoYesNoEnum` [R] If you set this flag, any special prices that may have been defined for the business partner in price lists take precedence over the price you specify in the blanket agreement. Field name: UseDiscnt.
- `Public Property NumAtCard() As String` [R/W] property NumAtCard
- `Public Property Owner() As Long` [R/W] Name of the user who is responsible for the blanket agreement. Field name: Owner. Length: 6 characters.
- `Public Property PaymentMethod() As String` [R/W] property PaymentMethod
- `Public Property PaymentTerms() As Long` [R/W] property PaymentTerms
- `Public Property PeriodIndicator() As String` [R] property PeriodIndicator
- `Public Property PriceList() As Long` [R/W] property PriceList
- `Public Property PriceMode() As PriceModeEnum` [R/W] property PriceMode
- `Public Property Project() As String` [R/W] property Project
- `Public Property Remarks() As String` [R/W] Comments about the agreement. Field name: Remarks. Length: 16 characters.
- `Public Property RemindTime() As Long` [R/W] The number of days, weeks, or months for an alert to appear prior to the termination of the blanket agreement. Field name: RemindVal. Length: 6 characters.
- `Public Property RemindUnit() As BoRemindUnits` [R/W] The reminder time units. Field name: RemindUnit.
- `Public Property Renewal() As BoYesNoEnum` [R/W] Enables you to set a reminder for renewing a service contract before it expires. Field name: Renewal.
- `Public Property SAPPassport() As String` [R] property SAPPassport
- `Public Property Series() As Long` [R/W] property Series
- `Public Property SettlementProbability() As Double` [R/W] The percentage value to indicate how probable it is that the business partner will pay for the goods. Field name: SettleProb.
- `Public Property ShippingType() As Long` [R/W] property ShippingType
- `Public Property SigningDate() As Date` [R/W] property SigningDate
- `Public Property StartDate() As Date` [R/W] Date on which the agreement becomes effective. Field name: StartDate.
- `Public Property Status() As BlanketAgreementStatusEnum` [R/W] The status of the blanket agreement. Field name: Status.
- `Public Property TerminateDate() As Date` [R/W] Date on which the blanket agreement ceases to be effective, if the agreement is terminated before the actual end date. The agreement status changes to Terminated. Field name: TermDate.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
