$html = Get-Content -Raw 'c:\Users\Dell\Documents\AntiG Proj\Portfolio\Files\Hideout - My Framer Site.htm'
$html = $html -replace '(?si)<script.*?</script>', ''
$html = $html -replace '(?si)<style.*?</style>', ''
$html = $html -replace '(?si)<svg.*?</svg>', ''
$html = $html -replace '<[^>]+>', "`n"
$html = $html -replace '(?m)^\s*$', ''
$html = $html -replace "`n{2,}", "`n"
$html = $html.Trim()
$html | Out-File -Encoding utf8 "$env:TEMP\hideout_text.txt"
