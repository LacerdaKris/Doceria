# Alicedelice - Doceria Artesanal

Sistema web de e-commerce para a doceria Alicedelice, permitindo que clientes visualizem produtos, adicionem ao carrinho, escolham data de entrega e enviem pedidos para análise.

## 🎨 Características do Projeto

- **Nome**: Alicedelice
- **Logo**: SVG personalizado com a letra "A" em gradiente de tons de verde
- **Paleta de Cores**: Tons de verde da bandeira lésbica (#026335, #5D9B58, #9ED386) e branco (#FFFFFF)
- **Banco de Dados**: SQLite
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Email**: Flask-Mail (notificações de pedidos)

## 📦 Produtos Disponíveis

1. **Red Velvet** - Massa de chocolate vermelha e cobertura de branquinho - aproximadamente 500g - R$ 90,00
2. **Cookies** - Cookie com massa de baunilha e gotas de chocolate - 8 unidades - R$ 60,00
3. **Meio cento de docinhos** - Negrinho ou branquinho, tipo de granulado à escolha - 50 unidades - R$ 100,00
4. **Torta de morango** - Massa de maisena, creme de baunilha e morangos - aproximadamente 500g - R$ 110,00
5. **Trio de ovos** - Casquinhas de chocolate recheadas; de brigadeiro, brigadeiro meio amargo com branquinho e branquinho com leite ninho, com pedaços de bombom por cima - aproximadamente 350g - R$ 90,00
6. **Bolo chocoffe** - Massa molhadinha de chocolate com leve toque de café e cobertura de chocolate - aproximadamente 500g - R$ 90,00
7. **Torta cookie** - Massa de cookie e recheio de brigadeiro - aproximadamente 400g - R$ 90,00
8. **Bolo de ninho** - Massa de chocolate e cobertura de branquinho de leite ninho - aproximadamente 500g - R$ 90,00
9. **Bolo de laranja** - Massa de laranja e cobertura de calda de laranja - aproximadamente 400g - R$ 80,00
10. **Vulcão de chocolate** - Massa de fubá ou chocolate com cobertura de brigadeiro - aproximadamente 500g - R$ 90,00

## 📁 Estrutura do Projeto

```
alicedelice/
├── app.py                 # Aplicação Flask (backend)
├── index.html             # Página principal (frontend)
├── requirements.txt       # Dependências Python
├── README.md              # Este arquivo
├── alicedelice.db         # Banco de dados SQLite (criado automaticamente)
└── images/                # Pasta com imagens dos produtos
    ├── 1.jpeg
    ├── 2.jpeg
    ├── 3.jpeg
    ├── 4.jpeg
    ├── 5.jpeg
    ├── 6.jpeg
    ├── 7.jpeg
    ├── 8.jpeg
    ├── 9.jpeg
    └── 10.jpeg
```

## 🚀 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## 📋 Instalação

### 1. Clone ou baixe o projeto

Se estiver usando Git:
```bash
git clone <url-do-repositorio>
cd "Projeto de extensão"
```

Se baixou como ZIP, extraia e navegue até a pasta do projeto.

### 2. Crie um ambiente virtual (recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

As dependências instaladas serão:
- Flask==3.0.0 (Framework web)
- Flask-CORS==4.0.0 (Suporte a CORS para requisições cross-origin)
- Flask-Mail==0.9.1 (Envio de emails)

### 4. Configure o envio de emails

Para que as notificações de pedidos funcionem, você precisa configurar as credenciais do Gmail:

**Windows (PowerShell):**
```bash
$env:MAIL_USERNAME="seu-email@gmail.com"
$env:MAIL_PASSWORD="sua-app-password"
$env:MAIL_DEFAULT_SENDER="seu-email@gmail.com"
```

**Windows (CMD):**
```cmd
set MAIL_USERNAME=seu-email@gmail.com
set MAIL_PASSWORD=sua-app-password
set MAIL_DEFAULT_SENDER=seu-email@gmail.com
```

**Linux/Mac:**
```bash
export MAIL_USERNAME="seu-email@gmail.com"
export MAIL_PASSWORD="sua-app-password"
export MAIL_DEFAULT_SENDER="seu-email@gmail.com"
```

**Importante:** Para usar o Gmail, você precisa criar uma "App Password":
1. Acesse sua conta Google
2. Vá em Configurações de Conta > Segurança
3. Ative a verificação em duas etapas (2FA)
4. Em "App Passwords", crie uma nova senha para "Mail"
5. Use essa senha no lugar da senha normal da sua conta

O sistema enviará emails automaticamente para:
- **k.cris.poa@gmail.com** (administrador) com detalhes do pedido e observações
- **Email do cliente** (se fornecido) com confirmação do pedido

## 🏃 Executando o Projeto

### Iniciar o servidor de desenvolvimento

```bash
python app.py
```

O servidor iniciará na porta 5000. Você verá uma mensagem similar a:
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
```

### Acessar a aplicação

Abra seu navegador e acesse:
```
http://localhost:5000
```

## 🗄️ Banco de Dados

O banco de dados SQLite (`alicedelice.db`) é criado automaticamente na primeira execução do aplicativo. Ele contém três tabelas:

### Tabela `products`
Armazena informações dos produtos:
- `id`: Identificador único (auto-incremento)
- `name`: Nome do produto
- `description`: Descrição detalhada
- `price`: Preço do produto
- `image_path`: Caminho da imagem

### Tabela `orders`
Armazena informações dos pedidos:
- `id`: Identificador único (auto-incremento)
- `customer_name`: Nome do cliente
- `customer_phone`: Telefone do cliente
- `customer_email`: E-mail do cliente (opcional)
- `delivery_date`: Data de entrega desejada
- `total_amount`: Valor total do pedido
- `status`: Status do pedido (padrão: 'pending')
- `created_at`: Data e hora de criação

### Tabela `order_items`
Armazena os itens de cada pedido:
- `id`: Identificador único (auto-incremento)
- `order_id`: ID do pedido (chave estrangeira)
- `product_id`: ID do produto (chave estrangeira)
- `quantity`: Quantidade do item
- `price`: Preço unitário na hora da compra

## 🔌 API Endpoints

### GET `/api/products`
Retorna todos os produtos disponíveis.

**Resposta:**
```json
[
  {
    "id": 1,
    "name": "Red Velvet",
    "description": "Massa de chocolate vermelha...",
    "price": 90.0,
    "image_path": "images/1.jpeg"
  },
  ...
]
```

### POST `/api/orders`
Cria um novo pedido.

**Corpo da Requisição:**
```json
{
  "customer_name": "Maria Silva",
  "customer_phone": "(11) 99999-9999",
  "customer_email": "maria@email.com",
  "delivery_date": "2026-05-15",
  "total_amount": 180.0,
  "items": [
    {
      "product_id": 1,
      "quantity": 2,
      "price": 90.0
    }
  ]
}
```

**Resposta:**
```json
{
  "order_id": 1,
  "status": "success"
}
```

### GET `/api/orders`
Retorna todos os pedidos (útil para administração).

### PUT `/api/orders/<order_id>/status`
Atualiza o status de um pedido.

**Corpo da Requisição:**
```json
{
  "status": "approved"
}
```

## 🎯 Funcionalidades

### Catálogo de Produtos
- Visualização de todos os produtos com imagens
- Informações detalhadas (nome, descrição, preço)
- Layout responsivo em grid

### Carrinho de Compras
- Adicionar produtos ao carrinho
- Alterar quantidade de itens
- Remover itens do carrinho
- Cálculo automático do total
- Contador de itens no cabeçalho

### Formulário de Pedido
- Nome completo (obrigatório)
- Telefone (obrigatório)
- E-mail (opcional)
- Data de entrega (obrigatório, não permite datas passadas)
- Envio para análise

### Design
- Logo SVG personalizado com letra "A"
- Paleta de cores em tons de verde da bandeira lésbica
- Interface moderna e responsiva
- Animações suaves
- Notificações de feedback

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask 3.0.0
- **Banco de Dados**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **CORS**: Flask-CORS 4.0.0

## 📱 Responsividade

O site é totalmente responsivo e funciona em:
- Desktop (1920px+)
- Laptop (1366px - 1920px)
- Tablet (768px - 1366px)
- Mobile (320px - 768px)

## 🔧 Personalização

### Alterar cores

Edite as variáveis CSS em `index.html`:
```css
:root {
    --dark-green: #026335;
    --medium-green: #5D9B58;
    --light-green: #9ED386;
    --white: #FFFFFF;
}
```

### Adicionar novos produtos

Edite o arquivo `app.py` e adicione novos produtos à lista `products` na função `init_db()`:
```python
products = [
    # ... produtos existentes ...
    ('Novo Produto', 'Descrição do produto', 95.00, 'images/nova-imagem.jpeg')
]
```

### Alterar porta do servidor

Edite a última linha de `app.py`:
```python
app.run(debug=True, port=5000)  # Altere 5000 para a porta desejada
```

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'flask'"
**Solução**: Certifique-se de que instalou as dependências:
```bash
pip install -r requirements.txt
```

### Erro: "Permission denied" ao acessar imagens
**Solução**: Verifique se a pasta `images` está no mesmo diretório do `app.py` e se as permissões estão corretas.

### Porta 5000 já em uso
**Solução**: Altere a porta em `app.py` ou encerre o processo que está usando a porta 5000.

**Windows:**
```bash
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

## 📝 Notas Importantes

- Este é um servidor de desenvolvimento e não deve ser usado em produção sem configurações adicionais de segurança
- O banco de dados SQLite é criado localmente e pode ser acessado com qualquer cliente SQLite
- Para produção, considere usar um servidor WSGI como Gunicorn ou uWSGI
- As imagens dos produtos devem estar na pasta `images/` com os nomes 1.jpeg a 10.jpeg

## 🤝 Contribuindo

Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos e de extensão universitária.

## 👥 Contato

Para dúvidas ou suporte, entre em contato através do projeto de extensão.

---

**Desenvolvido com ❤️ para a doceria Alicedelice**
