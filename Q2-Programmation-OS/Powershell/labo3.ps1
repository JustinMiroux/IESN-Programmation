$argcount = $args.Length
$robertcount = 0
$testcount = 0
$admincount = 0

Write-Output "Il y a $argcount paramètre"

foreach ($arg in $args) {
    switch ($arg) {
        {$_ -eq "robert"} {"Bonjour Robert"; $robertcount+=1; break}
        {$_ -eq "test"} {"Ceci est un compte test"; $testcount+=1; break}
        {$_ -eq "admin"} {"Bienvenue cher administrateur"; $admincount+=1;break}
        Default {"Le paramètre $arg est inconnu !"}
    }
}

Write-Output "Il y a $robertcount robert"
Write-Output "Il y a $testcount test"
Write-Output "Il y a $admincount admin"