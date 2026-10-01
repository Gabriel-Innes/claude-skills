<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DepreciationType (Object)

In SAP Business One, you can use depreciation types to define different depreciation calculation methods for your fixed assets. After you create a depreciation type, you can assign it to a specific depreciation area of an asset class. Then, by assigning the asset class to a fixed asset, the depreciation calculation methods are finally applied to the asset. In general, SAP Business One lets you use the following depreciation methods: - Straight Line Method - Straight Line Period Control Method - Declining Balance Method - Multilevel Method - Immediate Write-Off Method - Special Depreciation Method - Manual Depreciation Method - Accelerated Method: Czech Republic and Slovakia Source table: ODTP.

## Properties (44)
- `Public Property AcquisitionPeriodControl() As AcquisitionPeriodControlEnum` [R/W] Specify how the acquisition of an asset determines the asset's depreciation start date. Field name: PerAcq.
- `Public Property AcquisitionProRataType() As AcquisitionProRataTypeEnum` [R/W] Specify one of the PR Temporis Type to determine the depreciation start date. Field name: AcqPRTyp.
- `Public Property CalculationBase() As CalculationBaseEnum` [R/W] The base with which you want to calculate the depreciation of assets. Field name: CalcBase.
- `Public Property Code() As String` [R/W] The code for the depreciation type. Field name: Code. Length: 15 characters.
- `Public Property DecliningChangeTo() As String` [R/W] Specify a depreciation type with the straight line method as the alternative depreciation type. Field name: dAltDprTyp.
- `Public Property DecliningFactor() As Double` [R/W] The factor for calculating the upper limit of an asset's depreciation amount in each period. The upper limit is calculated using the straight-line method and multiplied by this factor. Field name: dFactor.
- `Public Property DecliningPercentage() As Double` [R/W] The annual/monthly percentage rate for the depreciation calculation. Field name: dPercent.
- `Public Property DeltaCoefficient() As Long` [R] The delta coefficient in the accelerated depreciation method. Field name: DeltaCoeff.
  - remarks: The accelerated depreciation method is available in the Czech Republic and Slovakia localizations only.
- `Public Property DepreciationEndAtLastFullYear() As BoYesNoEnum` [R/W] Indicates whether to stop an asset's depreciation at the end of the last full fiscal year of the asset's useful life. Field name: DeprEndLFY.
- `Public Property DepreciationLevelCollection() As DepreciationLevelCollection` [R] Represents the depreciation levels of an asset's useful life.
- `Public Property DepreciationMethod() As DepreciationMethodEnum` [R/W] The depreciation method of the asset. Field name: DprMeth.
- `Public Property DepreciationTypePool() As String` [R/W] Specify a pool to which you want to assign the depreciation type. You must assign a special or manual depreciation type to a pool. Field name: PoolID.
- `Public Property Description() As String` [R/W] The description about the depreciation type. Field name: Descr. Length: 100 characters.
- `Public Property FactorOnlyRelevantToFirstFiscalYear() As BoYesNoEnum` [R/W] Indicates that the factor you specified is effective only in the first fiscal year of an asset's useful life. Field name: FactorFFY.
- `Public Property IncludePreviousDepreciationInCapitalizationPeriod() As BoYesNoEnum` [R/W] Indicates whether to move depreciation of previous periods in the fiscal year to the capitalization period. Field name: AccuPriorP.
- `Public Property IncludeSalvageInDepreciation() As BoYesNoEnum` [R/W] Includes the salvage value in the calculation of an asset's depreciation. Field name: InclSalv.
- `Public Property ManualDepreciationReduceDepreciationBase() As BoYesNoEnum` [R/W] Indicates whether to let manual depreciation affect the calculation of an asset's planned depreciation. Field name: maDecBase.
  - remarks: Once you enable this property, the system automatically reduces the depreciation base by the manual depreciation amount.
- `Public Property MaximumDepreciableValue() As Double` [R/W] the maximum depreciable value of an asset. Field name: MaxDepr.
  - remarks: The field is available only for depreciation types having the Straight Line or Declining Balance method.
- `Public Property MinimumDepreciatedValue() As Double` [R/W] The minimum book value of an asset after depreciation. Field name: DprTo.
- `Public Property PercentageOfDepreciationReversedInRetirementYear() As Double` [R/W] The amount (in percentage) of depreciation you want to reverse for an asset in the retirement year. Field name: PerDpRev.
- `Public Property RetirementPeriodControl() As RetirementPeriodControlEnum` [R/W] Specify how an asset's retirement affects the asset's depreciation. Field name: PerRet.
- `Public Property RetirementProRataType() As RetirementProRataTypeEnum` [R/W] Specify one of the PR Temporis Type to determine the depreciation end date. Field name: RetPRTyp.
- `Public Property RoundingMethod() As DepreciationRoundingMethodEnum` [R/W] The rounding method of Round Year End Book Value. Field name: RoundMeth.
- `Public Property RoundYearEndBookValue() As BoYesNoEnum` [R/W] Rounds the net book values of assets at the end of each fiscal year. Field name: Rounding.
- `Public Property SalvagePercentage() As Double` [R/W] The salvage value percentage. Field name: SalvPerc.
- `Public Property SpecialDepreciationAlternativeDepreciation() As String` [R/W] To compare different depreciation calculations, specify a second depreciation type here. The system calculates the depreciation for this depreciation type in parallel. The result of the alternative calculation is for reference only, and no bookings are carried out in the general ledger. Field name: spAlDpr.
- `Public Property SpecialDepreciationCalculationMethod() As SpecialDepreciationCalculationMethodEnum` [R] The calculation method of special depreciation. Field name: spMeth.
- `Public Property SpecialDepreciationConcessionPeriodYears() As Long` [R/W] The number of years during which the special depreciation is legally permitted. Field name: spConcPer.
- `Public Property SpecialDepreciationMaximumAmount() As Double` [R/W] The maximum depreciation amount allowed in addition to the normal depreciation. The maximum amount is an alternative to the maximum percentage. Field name: spMaxAmnt.
- `Public Property SpecialDepreciationMaximumFlag() As SpecialDepreciationMaximumFlagEnum` [R/W] To optimize depreciation from a tax point of view, you can split the concession period into multiple sub-periods and freely distribute the maximum percentage over these periods. Field name: spMaxFlag.
- `Public Property SpecialDepreciationMaximumPercentage() As Double` [R/W] The percentage rate for calculating the maximum depreciation amount allowed in addition to the normal depreciation. Field name: spMaxPerc.
  - remarks: National legislation specifies this value. The system calculates the maximum special depreciation amount as follows: (Acquisition and Production Costs – Salvage Value) * Maximum Percentage
- `Public Property SpecialDepreciationNormalDepreciation() As String` [R/W] The normal depreciation of the asset. Field name: spAdDpr.
  - remarks: Usually, a certain percentage of the asset value can be depreciated in addition to the normal depreciation amount. The percentage allowed for the special depreciation, as well as the period over which you can carry out the special depreciation, are dependent on national legislation.
- `Public Property StraightLineCalculationMethod() As StraightLineCalculationMethodEnum` [R/W] The calculation method of the straight line period control depreciation method. Field name: sCalcMeth.
- `Public Property StraightLinePercentage() As Double` [R/W] The annual percentage rate for the depreciation calculation. Field name: sPercent.
- `Public Property StraightLinePeriodControlDepreciationPeriods() As StraightLinePeriodControlDepreciationPeriodsEnum` [R/W] The depreciation period of the straight line period control depreciation method. Field name: DprPer.
- `Public Property StraightLinePeriodControlFactor() As Double` [R/W] The factor for the straight line period control depreciation method. Field name: PerFactor.
  - remarks: If you have specified Standard in the StraightLinePeriodControlDepreciationPeriods property, enter a factor for depreciation calculation that is applied to all periods of an asset's useful life. If you have specified Individual in the StraightLinePeriodControlDepreciationPeriods property, enter a factor for depreciation calculation that is taken as the default factor for all periods.
- `Public Property SubsequentAcquisitionPeriodControl() As SubsequentAcquisitionPeriodControlEnum` [R/W] Specify how an asset's subsequent acquisition affects the asset's depreciation. Field name: PerSubAcq.
- `Public Property SubsequentAcquisitionProRataType() As SubsequentAcquisitionProRataTypeEnum` [R/W] Specify one of the PR Temporis Type to determine the depreciation start date. Field name: SubPRTyp.
- `Public Property TransferSourcePeriodControl() As TransferSourcePeriodControlEnum` [R/W] property TransferSourcePeriodControl
- `Public Property TransferSourceProRataType() As TransferSourceProRataTypeEnum` [R/W] property TransferSourceProRataType
- `Public Property TransferTargetPeriodControl() As TransferTargetPeriodControlEnum` [R/W] property TransferTargetPeriodControl
- `Public Property TransferTargetProRataType() As TransferTargetProRataTypeEnum` [R/W] property TransferTargetProRataType
- `Public Property ValidFrom() As Date` [R/W] The valid start date of the depreciation type. Field name: ValidFrom.
- `Public Property ValidTo() As Date` [R/W] The valid to date of the depreciation type. Field name: ValidTo.

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
