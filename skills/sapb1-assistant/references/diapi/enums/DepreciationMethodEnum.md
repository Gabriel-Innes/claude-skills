<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DepreciationMethodEnum (Enumeration)

The depreciation method of the asset.

| Member | Value | Description |
|---|---|---|
| dmNoDepreciation | 0 | No depreciation is carried out |
| dmStraightLine | 1 | A method of distributing an asset's value evenly across its useful life. That is, the asset is depreciated by the same amount in each period. |
| dmStraightLinePeriodControl | 2 | A method that entails defining different factors used in depreciation calculation for different periods of an asset's useful life. |
| dmDecliningBalance | 3 | A method that entails applying a depreciation rate against the non-depreciated balance of an asset. Instead of spreading the cost of the asset evenly over its useful life, the method depreciates the asset at a constant rate, which results in declining depreciation charges each successive period. |
| dmMultilevel | 4 | A method of applying different depreciation rates to an asset for different stages of an asset's useful life. |
| dmImmediateWriteOff | 5 | A method generally applied to low-value assets whose full value can be depreciated in the acquisition year. |
| dmSpecialDepreciation | 6 | A method of carrying out automatic special depreciation. |
| dmManualDepreciation | 7 | A method of carrying out manual special depreciation. |
| dmAccelerated | 8 | A method of carrying out accelerated depreciation. |
