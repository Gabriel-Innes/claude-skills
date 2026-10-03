<#
.SYNOPSIS
  Dump every public enumeration in the Pastel.Evolution namespace from the shipped SDK assembly to JSON
  (maintenance only; feeds build_sdk_ref.py --enum-json).

.DESCRIPTION
  The shipped CHM documents 41 enumerations but lists members for only 6 of them, and the assembly carries
  more public enums than the CHM names at all. This script reads the real members and values by reflection.

  The assemblies are .NET Framework, so run this in Windows PowerShell 5.1 (not pwsh). They are loaded from
  bytes so a "downloaded from the internet" zone mark on the DLLs does not block the load, and the
  dependency Pastel.Evolution.Common.dll is loaded first from the same folder.

.EXAMPLE
  powershell -File scripts/dump_enums.ps1 -SdkDir docs/Pastel.Evolution.11.0.0.10 -Out /c/temp/evo/enums.json
#>
param(
    [Parameter(Mandatory = $true)] [string] $SdkDir,
    [Parameter(Mandatory = $true)] [string] $Out,
    [string] $Namespace = "Pastel.Evolution"
)

$ErrorActionPreference = "Stop"
$SdkDir = (Resolve-Path $SdkDir).Path

$null = [System.Reflection.Assembly]::Load([IO.File]::ReadAllBytes((Join-Path $SdkDir "Pastel.Evolution.Common.dll")))
$asm  = [System.Reflection.Assembly]::Load([IO.File]::ReadAllBytes((Join-Path $SdkDir "Pastel.Evolution.dll")))

try { $types = $asm.GetTypes() }
catch [System.Reflection.ReflectionTypeLoadException] { $types = $_.Exception.Types | Where-Object { $_ -ne $null } }

$enums = $types | Where-Object { $_.IsEnum -and ($_.IsPublic -or $_.IsNestedPublic) -and $_.Namespace -eq $Namespace }

$list = foreach ($t in $enums) {
    # Nested enums are named the way the CHM names them: DeclaringType.Enum (e.g. Bank.AccountType).
    $name = if ($t.IsNested) { $t.DeclaringType.Name + "." + $t.Name } else { $t.Name }
    $members = foreach ($n in [System.Enum]::GetNames($t)) {
        [ordered]@{ name = $n; value = [Convert]::ToInt64([System.Enum]::Parse($t, $n)) }
    }
    [ordered]@{
        name       = $name
        fullname   = $t.FullName
        underlying = [System.Enum]::GetUnderlyingType($t).Name
        flags      = [bool]($t.GetCustomAttributes([System.FlagsAttribute], $false).Count)
        members    = @($members)
    }
}

$list = @($list | Sort-Object { $_.name.ToLower() })
$json = ConvertTo-Json -InputObject $list -Depth 5
[IO.File]::WriteAllText($Out, $json, (New-Object System.Text.UTF8Encoding $false))
Write-Output ("{0} public enumerations in {1} written to {2} (assembly {3})" -f $list.Count, $Namespace, $Out, $asm.GetName().Version)
