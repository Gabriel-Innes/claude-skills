<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AssetDocumentTypeEnum (Enumeration)

The transaction type of the asset document.

| Member | Value | Description |
|---|---|---|
| adtOrdinaryDepreciation | 0 | Ordinary depreciation includes the planned ordinary depreciation and the manual ordinary depreciation. The former is the depreciation calculated and carried out automatically by the system based on the depreciation type you assign to the asset. And the latter is the depreciation you manually perform using the manual depreciation document. |
| adtUnplannedDepreciation | 1 | Usually carried out when there is an unexpected reduction in the value of an asset resulting, for example, from an accident. |
| adtSpecialDepreciation | 2 | SAP Business One can carry out the special depreciation automatically for an asset, known as the automatic special depreciation. You can assign a depreciation type to an asset with the Special Depreciation method, and the system automatically calculates the special depreciation when it is due. |
| adtAppreciation | 3 | Increase in an asset's book value to offset the asset's unplanned depreciation. |
| adtAssetTransfer | 4 | Transfers an asset to another asset. |
| adtSales | 5 | Indicates an asset sold with a profit or loss. If you do not need to specify the customer information, use this type; otherwise, use an A/R invoice. |
| adtScrapping | 6 | Indicates a scrapped asset, with no revenue earned. SAP Business One posts the asset's remaining book value at the time of retirement as an expense. |
| adtAssetClassTransfer | 7 | Transfers an asset to a new asset class. You can perform the asset class transfer only if the asset uses the depreciation types with the No Depreciation method in all areas during the transfer period. |
