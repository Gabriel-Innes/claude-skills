<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ResourceAllocationEnum (Enumeration)

Determines how the resource is allocated.

| Member | Value | Description |
|---|---|---|
| raOnStartDate | 0 | The capacity of the resource is allocated to the start date of the production order. Default value. |
| raOnEndDate | 1 | The capacity of the resource is allocated to the end date of the production order regardless of the quantity of the Internal and Available capacities on that day. |
| raStartDateForwards | 2 | The capacity of the resource is allocated to the start date when it is assigned to the production order; however, if the Planned Quantity is greater than the Single Run Capacity for the start date, the system allocates only as much capacity as there is Single Run Capacity defined for the start date and continues to allocate the remaining capacity to the day after the start date. The process continues forwards for each day until it allocates all the remaining Planned Quantity. |
| raEndDateBackwards | 3 | The capacity of the resource is allocated to the end date when it is assigned to the production order; however, if the Planned Quantity is greater than the Single Run Capacity for the end date, the system allocates only as much capacity as there is Single Run Capacity defined for the end date and continues to allocate the remaining capacity to the day before the end date. The process continues backwards for each day until it reaches the current system date and allocates all the remaining Planned Quantity to the current system date regardless of how much Single Run Capacity is defined for that day. |
