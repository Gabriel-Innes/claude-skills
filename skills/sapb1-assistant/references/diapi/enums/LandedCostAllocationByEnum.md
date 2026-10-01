<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# LandedCostAllocationByEnum (Enumeration)

Specify the distribution type for the landed cost.

| Member | Value | Description |
|---|---|---|
| asCashValueBeforeCustoms | 0 | The related costs are distributed in relation to the share of an item of the total FOB price of the delivery minus customs. |
| asCashValueAfterCustoms | 1 | The related costs are distributed in relation to the share of an item of the total FOB price of the delivery plus customs. |
| asQuantity | 2 | The related costs are distributed according to the quantity of an item in proportion to the total quantity of the delivery. |
| asWeight | 3 | The related costs are distributed according to the weight of an item in proportion to the total weight of the delivery. |
| asVolume | 4 | The related costs are distributed according to the volume of an item in proportion to the total volume of the delivery. |
| asEqual | 5 | The related costs are distributed equally among the delivery items. |
| asLegalCost | 6 |  |
