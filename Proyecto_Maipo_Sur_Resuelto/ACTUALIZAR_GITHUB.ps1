# Maipo Sur DevSecOps — Daniel Silva, Allen Ramirez, Antonella Mancilla
# Solo para usar en tu propio repositorio. Se pide confirmación antes de publicar.
$ErrorActionPreference = 'Stop'
$repo = 'https://github.com/Allen2109/taller-devsecops-maipo-sur.git'
$zip = Join-Path $PSScriptRoot 'Proyecto_Maipo_Sur_MEJORADO.zip'
$extraido = Test-Path -LiteralPath (Join-Path $PSScriptRoot '.github/workflows/ci.yml')
if (-not $extraido -and -not (Test-Path -LiteralPath $zip)) { throw 'Extrae el ZIP y ejecuta este script desde la carpeta del proyecto, o deja el ZIP junto al script.' }
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'Git para Windows no esta instalado. Usa GitHub Desktop o carga los archivos desde el navegador.' }
$work = Join-Path ([IO.Path]::GetTempPath()) ('maipo-upgrade-' + [guid]::NewGuid().ToString('N').Substring(0,8))
$src = Join-Path $work 'nuevo'
$dest = Join-Path $work 'repositorio'
if ($extraido) {
    $src = $PSScriptRoot
} else {
    New-Item -Path $src -ItemType Directory -Force | Out-Null
    Expand-Archive -LiteralPath $zip -DestinationPath $src -Force
}
Write-Host 'Clonando tu repositorio...' -ForegroundColor Cyan
& git clone -- $repo $dest
if ($LASTEXITCODE -ne 0) { throw 'No se pudo clonar el repositorio. Comprueba tus permisos.' }
# Copia todo en la raiz, incluyendo la carpeta .github
& robocopy.exe $src $dest /E /R:1 /W:1 /XD .git dist __pycache__ | Out-Null
if ($LASTEXITCODE -ge 8) { throw 'Error copiando los archivos.' }
Push-Location $dest
try {
    & git status --short
    Write-Host "`nSe agregaran los archivos mejorados en la RAIZ. La carpeta anterior se conserva como respaldo." -ForegroundColor Yellow
    $respuesta = Read-Host 'Escribe SI para confirmar la publicacion'
    if ($respuesta -cne 'SI') { Write-Host 'No se subieron cambios.'; return }
    & git add -A
    if ($LASTEXITCODE -ne 0) { throw 'Error en git add.' }
    & git diff --cached --quiet
    if ($LASTEXITCODE -eq 0) { Write-Host 'No hay cambios que subir.'; return }
    & git commit -m 'Mejoras DevSecOps: Daniel Silva, Allen Ramirez y Antonella Mancilla'
    if ($LASTEXITCODE -ne 0) { throw 'Configura tu identidad de Git y vuelve a intentarlo.' }
    & git push origin HEAD:main
    if ($LASTEXITCODE -ne 0) { throw 'El push fallo. Comprueba que iniciaste sesion en Git y tienes permisos.' }
    Write-Host 'Publicado. Revisa GitHub > Actions.' -ForegroundColor Green
}
finally { Pop-Location }
