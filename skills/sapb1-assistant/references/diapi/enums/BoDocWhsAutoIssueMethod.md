<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BoDocWhsAutoIssueMethod (Enumeration)

The method by which items in bin locations are issued.

| Member | Value | Description |
|---|---|---|
| aimSingleChoiceOnly | 0 | Single Choice - Allocates items from bin locations when there is only one way of doing it. If there is more than one way to allocate items from bin locations, the single choice method is not effective. |
| aimBinCodeOrder | 1 | Bin Location Code Order - Allocates items from bin locations according to the alphanumeric order of the bin location codes. |
| aimAlternativeSortCodeOrder | 2 | Alternative Sort Code Order - Allocates items from bin locations according to the alphanumeric order of the bin locations' alternative sort codes. |
| aimQtyDescendingOrder | 3 | Descending Quantity - Allocates items from bin locations according to the descending order of the item quantity in the bin locations. |
| aimQtyAscendingOrder | 4 | Ascending Quantity - Allocates items from bin locations according to the ascending order of the item quantity in the bin locations. |
| aimBinFIFO | 5 |  |
| aimBinLIFO | 6 |  |
| aimSingleBinPreferred | 7 |  |
