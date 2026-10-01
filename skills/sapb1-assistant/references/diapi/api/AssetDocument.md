<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AssetDocument (Object)

AssetDocument is a business object that represents the header data of asset documents in the Fixed Asset function of SAP Business One application. With SAP Business One, you can carry out a series of transactions for your fixed assets as follows: - Capitalization - Capitalization Credit Memo - Retirement - Transfer - Manual Depreciation Source table: OACQ.

## Properties (31)
- `Public Property AssetDocumentAreaJournalCollection() As AssetDocumentAreaJournalCollection` [R] Represents the Accounting tab fields of an asset document.
- `Public Property AssetDocumentLineCollection() As AssetDocumentLineCollection` [R] Represents the line entries of an asset document.
- `Public Property AssetValueDate() As Date` [R/W] The date on which the asset is valued. By default, the date is the same as the posting date. Field name: AssetDate.
- `Public Property BaseReference() As String` [R] Displays the document number according to the definition in the Document Numbering - Setup window. Field name: BaseRef.
- `Public Property BPLID() As Long` [R/W] Represents the branch ID (in Brazilian localization); represents the business place ID (in Korean localization). Field name: BPLId.
- `Public Property BPLName() As String` [R/W] Represents the branch name (in Brazilian localization); represents the business place name (in Korean localization). Field name: BPLName. Length: 100 characters.
- `Public Property CancellationDate() As Date` [R/W] The cancellation date. Field name: CancelDate.
- `Public Property CancellationOption() As ClosingOptionEnum` [R/W] The cancellation option - specify a posting date to be used in the cancelled asset document. Field name: CancelOpt.
- `Public Property Currency() As String` [R/W] The currency for the asset document. Field name: Currency. Length: 3 characters.
- `Public Property DepreciationArea() As String` [R/W] The depreciation area in which the asset's depreciation takes effect. Field name: DprArea. Length: 100 characters.
- `Public Property DocEntry() As Long` [R] The internal ID of the asset document. Field name: DocEntry.
- `Public Property DocNum() As Long` [R/W] The number of the asset document. Field name: DocNum.
- `Public Property DocumentDate() As Date` [R/W] The document date. By default, the document date is the same as the posting date. Field name: DocDate.
- `Public Property DocumentRate() As Double` [R/W] The exchange rate of the document currency. Field name: DocRate.
- `Public Property DocumentTotal() As Double` [R] The total amount of the document. Field name: DocTotal.
- `Public Property DocumentTotalFC() As Double` [R] The total amount of the document in foreign currency. Field name: DocTotalFC.
- `Public Property DocumentTotalSC() As Double` [R] The total amount of the document in system currency. Field name: DocTotalSC.
- `Public Property DocumentType() As AssetDocumentTypeEnum` [R/W] The transaction type of the asset document. Field name: DocType.
- `Public Property HandWritten() As BoYesNoEnum` [R/W] Indicates whether it is manual numbering. Field name: Handwrtten.
- `Public Property LowValueAssetRetirement() As BoYesNoEnum` [R/W] Indicates whether this is low value asset retirement. Field name: LVARetire.
- `Public Property ManualDepreciationType() As String` [R/W] The type of the manual depreciation. Field name: ManDprType. Length: 15 characters.
- `Public Property Origin() As Long` [R] The origin of the asset document. Field name: CreatedBy.
- `Public Property OriginalType() As AssetOriginalTypeEnum` [R] The original type of the asset document. Field name: TransType.
- `Public Property PostingDate() As Date` [R/W] The date on which the journal entry is posted. Field name: PostDate.
- `Public Property Reference() As String` [R/W] The additional information about the asset document. Field name: Reference. Length: 32 characters.
- `Public Property Remarks() As String` [R/W] The remarks about the asset. Field name: Comments. Length: 254 characters.
- `Public Property Series() As Long` [R/W] Specify a numbering series. Field name: Series.
- `Public Property Status() As AssetDocumentStatusEnum` [R] The status of the asset document. Field name: DocStatus.
- `Public Property SummerizeByDistributionRules() As BoYesNoEnum` [R/W] Consolidates journal entry rows according to the distribution rules assigned to the assets. Field name: DstRlSmarz.
- `Public Property SummerizeByProjects() As BoYesNoEnum` [R/W] Consolidates journal entry rows according to the projects assigned to the assets. Field name: PrjSmarz.
- `Public Property VATRegNum() As String` [R/W] Represents CNPJ (in Brazilian localization); represents the VAT registration number (in Korean localization). Field name: VatRegNum. Length: 32 characters.

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
