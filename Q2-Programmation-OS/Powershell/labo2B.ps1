if ($temperature -is [int]) {

    Write-Output "La température introduite est: $temperature"

    switch ($temperature) {
        {$_ -ge 30} {"Maillot et coups de soleil"; break}
        {$_ -ge 20} {“Tee-shirt et sandales”; break}
        {$_ -ge 10} {“Pull et chaussures”; break}
        {$_ -ge 0} {“Doudoune et bottines”; break}
        Default {"Double doudoune et après-skis"}
    }

    switch ($temperature) {
        {$_ -ge 1 -and $_ -le 7} {“Un temps d’hiver”}
        {$_ -ge 6 -and $_ -le 15} {“Un temps de printemps”}
        {$_ -ge 13 -and $_ -le 23} {“Un temps d’été”}
        {$_ -ge 8 -and $_ -le 15} {“Un temps d’automne”}
    }
}
else {
    Write-Output "Aucune température détectée"
}

