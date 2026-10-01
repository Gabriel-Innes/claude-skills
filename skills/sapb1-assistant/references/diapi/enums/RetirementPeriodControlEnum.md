<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# RetirementPeriodControlEnum (Enumeration)

Specify how an asset's retirement affects the asset's depreciation.

| Member | Value | Description |
|---|---|---|
| rpcProRataTemporis | 0 | Specify one of the PR Temporis Type to determine the depreciation end date. |
| rpcHalfYearConvention | 1 | Calculates the asset depreciation as one of the following: If the asset retirement takes place in the first half of the fiscal year, the system calculates the depreciation till the last day of the first half of the year. If the asset retirement takes place in the second half of the fiscal year, the system calculates the depreciation till the last day of the second half of the year. |
| rpcOnlyAfterEndOfUsefulLife | 2 | Select this for low value assets, which can be retired only after the end of their useful life. Note that this option is available in the Germany localization only. |
