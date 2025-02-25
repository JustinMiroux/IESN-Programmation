# Hello world
Write-Output "Hello world"

# Manipulation d'objet
"PowerShell is powerful!".Length

# Nouvelle alias pour afficher les éléments dans le dir
New-Alias listd -Value Get-ChildItem
listd

# Nouvelle alias affiche ip public
function getpublicip {(Invoke-WebRequest -uri "https://ifconfig.me/ip").Content}
New-Alias ippub -Value getpublicip
ippub

# Affiche toutes les commandes avec le mot services dedans
Get-Command *services*