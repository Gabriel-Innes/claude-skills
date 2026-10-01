<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AcquisitionPeriodControlEnum (Enumeration)

Specify how the acquisition of an asset determines the asset's depreciation start date.

| Member | Value | Description |
|---|---|---|
| apcProRataTemporis | 0 | Specify one of the PR Temporis Type to determine the depreciation start date. |
| apcFirstYearConvention | 1 | Determines the depreciation start date as follows: When your fiscal year matches a calendar year: If the asset acquisition takes place before July 1st, the depreciation starts from January 1st. If the asset acquisition takes place after July 1st, the depreciation starts from July 1st. When your fiscal year does not match a calendar year: If the asset acquisition takes place in the first half of the fiscal year, the depreciation starts from the first day of the first half of the year. If the asset acquisition takes place in the second half of the fiscal year, the depreciation starts from the first day of the second half of the year. |
| apcHalfYear | 2 | The depreciation of the asset always starts from the first day of the second half of the fiscal year during which the asset acquisition takes place. |
| apcFullYear | 3 | The depreciation of the asset always starts from the first day of the fiscal year during which the asset acquisition takes place. |
