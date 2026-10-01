<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SubsequentAcquisitionPeriodControlEnum (Enumeration)

Specify how an asset's subsequent acquisition affects the asset's depreciation.

| Member | Value | Description |
|---|---|---|
| sapcProRataTemporis | 0 | Specify one of the PR Temporis Type to determine the depreciation start date. |
| sapcHalfYearConvention | 1 | Recalculates the asset depreciation as one of the following: If an asset's subsequent acquisition takes place in the fiscal year of acquisition, the system recalculates the asset depreciation from the very day when the depreciation starts. If an asset's subsequent acquisition takes place in years that follow the fiscal year of acquisition, the system recalculates the asset depreciation from the first day of the fiscal year during which the subsequent acquisition occurs. |
| sapcFullYear | 2 | Recalculates the asset depreciation as one of the following: If an asset's subsequent acquisition takes place in the fiscal year of acquisition, the system recalculates the asset depreciation from the very day when the depreciation starts. If an asset's subsequent acquisition takes place in years that follow the fiscal year of acquisition, the system recalculates the asset depreciation from the first day of the fiscal year during which the subsequent acquisition occurs. |
