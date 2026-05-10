# Script para configurar variáveis de ambiente do Gmail
# Substitua os valores abaixo com suas informações reais

Write-Host "=== Configuração de Email para Alicedelice ===" -ForegroundColor Green
Write-Host ""

# Configure aqui suas credenciais
$SEU_EMAIL = "seu-email@gmail.com"
$SUA_APP_PASSWORD = "xxxx-xxxx-xxxx-xxxx"  # Cole aqui a App Password de 16 caracteres

# Definir variáveis de ambiente
$env:MAIL_USERNAME = $SEU_EMAIL
$env:MAIL_PASSWORD = $SUA_APP_PASSWORD
$env:MAIL_DEFAULT_SENDER = $SEU_EMAIL

Write-Host "Variáveis de ambiente configuradas:" -ForegroundColor Yellow
Write-Host "MAIL_USERNAME = $env:MAIL_USERNAME"
Write-Host "MAIL_PASSWORD = [OCULTO]"
Write-Host "MAIL_DEFAULT_SENDER = $env:MAIL_DEFAULT_SENDER"
Write-Host ""

Write-Host "Para tornar permanentes, execute:" -ForegroundColor Cyan
Write-Host "[System.Environment]::SetEnvironmentVariable('MAIL_USERNAME', '$SEU_EMAIL', 'User')"
Write-Host "[System.Environment]::SetEnvironmentVariable('MAIL_PASSWORD', '$SUA_APP_PASSWORD', 'User')"
Write-Host "[System.Environment]::SetEnvironmentVariable('MAIL_DEFAULT_SENDER', '$SEU_EMAIL', 'User')"
Write-Host ""

Write-Host "IMPORTANTE:" -ForegroundColor Red
Write-Host "1. Você precisa ativar a verificação em duas etapas no Google primeiro"
Write-Host "2. Acesse: https://myaccount.google.com/apppasswords"
Write-Host "3. Crie uma App Password para 'Mail' com nome 'Alicedelice'"
Write-Host "4. Copie a senha de 16 caracteres e cole na variável \$SUA_APP_PASSWORD"
Write-Host ""

Write-Host "Depois de configurar, execute o app com: python app.py" -ForegroundColor Green
