Write-Output "La température introduite est: $temperature"

switch ($temperature) {
    {$_ -ge 30} {"Maillot et coups de soleil"; break}
    {$_ -ge 20} {“Tee-shirt et sandales”; break}
    {$_ -ge 10} {“Pull et chaussures”; break}
    {$_ -ge 0} {“Doudoune et bottines”; break}
    Default {"Double doudoune et après-skis"}
}