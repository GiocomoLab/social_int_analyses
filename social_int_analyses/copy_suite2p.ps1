$src = "Z:/giocomo/candong/social_interaction_data/calcium_imaging/social-0057-1"
$dest = "C:/Users/esay/data/social_interaction/calcium_imaging"

New-Item -ItemType Directory -Force -Path $dest | Out-Null

Get-ChildItem -Path $src -Directory | ForEach-Object {
    $suite2pPath = Join-Path $_.FullName "combined/suite2p"
    if (Test-Path $suite2pPath) {
        Copy-Item -Path $suite2pPath -Destination $dest -Recurse -Force
        Write-Host "Copied $suite2pPath"
    }
}