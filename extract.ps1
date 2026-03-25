$html = Get-Content "Files\Clash of Beast - My Framer Site.htm" -Raw
$html = $html -replace '(?s)<style[^>]*>.*?</style>', ''
$html = $html -replace '(?s)<script[^>]*>.*?</script>', ''
$html = $html -replace '(?s)<svg[^>]*>.*?</svg>', ''
$html = $html -replace '<[^>]+>', "`n"
$html = $html -replace '(&nbsp;|&#160;|&#x20;)', ' '
$html = $html -replace "`n\s*`n", "`n"
$html | Out-File "extracted.txt"
