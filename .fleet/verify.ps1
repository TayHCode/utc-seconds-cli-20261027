$ErrorActionPreference = "Stop"
Push-Location (Join-Path $PSScriptRoot "..")
try {
    python -B -m unittest discover -s tests -v
    if ($LASTEXITCODE -ne 0) { throw "CLI tests failed" }
} finally {
    Pop-Location
}
