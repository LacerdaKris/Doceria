# 📧 Configuração de Email - Alicedelice

## 🚨 Passo a Passo Obrigatório

### 1. Ativar Verificação em Duas Etapas (2FA)
1. Acesse: https://myaccount.google.com/security
2. Procure por "Verificação em duas etapas"
3. Clique em "Ativar" e siga as instruções
4. **É obrigatório ter 2FA ativada para criar App Passwords**

### 2. Criar App Password
1. Após ativar 2FA, acesse: https://myaccount.google.com/apppasswords
2. Em "Selecionar app", escolha **"Mail"**
3. Em "Selecionar dispositivo", escolha **"Outro (nome personalizado)"**
4. Digite **"Alicedelice"** e clique em **"Gerar"**
5. **Copie a senha de 16 caracteres** (formato: xxxx xxxx xxxx xxxx)
   - ⚠️ **ATENÇÃO:** Esta senha só aparece uma vez!

### 3. Configurar Variáveis de Ambiente

#### Opção A: Usar o script PowerShell (Recomendado)
```powershell
.\configurar_email.ps1
```
Edite o arquivo `configurar_email.ps1` e substitua os valores antes de executar.

#### Opção B: Configurar manualmente no PowerShell
```powershell
# Substitua com suas informações reais
$env:MAIL_USERNAME="seu-email@gmail.com"
$env:MAIL_PASSWORD="xxxx-xxxx-xxxx-xxxx"  # Cole a App Password aqui
$env:MAIL_DEFAULT_SENDER="seu-email@gmail.com"
```

#### Opção C: Tornar permanente (recomendado para desenvolvimento)
```powershell
[System.Environment]::SetEnvironmentVariable('MAIL_USERNAME', 'seu-email@gmail.com', 'User')
[System.Environment]::SetEnvironmentVariable('MAIL_PASSWORD', 'xxxx-xxxx-xxxx-xxxx', 'User')
[System.Environment]::SetEnvironmentVariable('MAIL_DEFAULT_SENDER', 'seu-email@gmail.com', 'User')
```

### 4. Testar a Configuração
Execute o aplicativo:
```bash
python app.py
```

Faça um pedido de teste. Se os emails não forem enviados, verifique:
- As variáveis de ambiente estão configuradas corretamente
- A App Password foi criada corretamente
- O email e senha estão corretos

## 🔧 Como o Sistema Funciona

O sistema envia automaticamente:
1. **Email para o administrador**:
   - Detalhes completos do pedido
   - Informações do cliente
   - Observações
   - Lista de itens

2. **Email para o cliente** (se fornecido):
   - Confirmação do pedido
   - Resumo dos itens
   - Informações de contato

## 🐛 Solução de Problemas

### "App Passwords não aparece"
- ✅ Verifique se a 2FA está ativada
- ✅ Tente acessar diretamente: https://myaccount.google.com/apppasswords
- ✅ Use conta Google pessoal (contas corporativas podem ter restrições)

### "Email não é enviado"
- ✅ Verifique se as variáveis de ambiente estão definidas
- ✅ Confirme se a App Password tem 16 caracteres
- ✅ Teste com outro email Gmail

### "Erro de autenticação"
- ✅ Use a App Password, NUNCA a senha normal do Gmail
- ✅ Verifique se não há espaços extras na senha
- ✅ Confirme se o email está correto

## 📝 Importante

- **Nunca** compartilhe sua App Password
- **Nunca** use sua senha normal do Gmail no código
- A App Password só funciona com a conta Google que a criou
- Se precisar resetar, exclua a App Password antiga e crie uma nova

---

**Dúvidas?** Verifique o console do aplicativo para mensagens de erro de email.
