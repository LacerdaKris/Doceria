from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_mail import Mail, Message
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@alicedelice.com')

mail = Mail(app)

DATABASE = 'alicedelice.db'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ADMIN_EMAIL = 'k.cris.poa@gmail.com'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL,
            image_path TEXT NOT NULL
        )
    ''')
    
    # Orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            customer_phone TEXT NOT NULL,
            customer_email TEXT,
            observations TEXT,
            delivery_date TEXT NOT NULL,
            total_amount REAL NOT NULL,
            status TEXT DEFAULT 'pending',
            created_at TEXT NOT NULL
        )
    ''')
    
    # Order items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders (id),
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')
    
    # Check if products are already inserted
    cursor.execute('SELECT COUNT(*) FROM products')
    product_count = cursor.fetchone()[0]
    
    if product_count == 0:
        # Insert products
        products = [
            ('Red Velvet', 'Massa de chocolate vermelha e cobertura de branquinho - aproximadamente 500g', 90.00, 'images/1.jpeg'),
            ('Cookies', 'Cookie com massa de baunilha e gotas de chocolate - 8 unidades', 60.00, 'images/2.jpeg'),
            ('Meio cento de docinhos', 'Negrinho ou branquinho, tipo de granulado à escolha - 50 unidades', 100.00, 'images/3.jpeg'),
            ('Torta de morango', 'Massa de maisena, creme de baunilha e morangos - aproximadamente 500g', 110.00, 'images/4.jpeg'),
            ('Trio de ovos', 'Casquinhas de chocolate recheadas; de brigadeiro, brigadeiro meio amargo com branquinho e branquinho com leite ninho, com pedaços de bombom por cima - aproximadamente 350g', 90.00, 'images/5.jpeg'),
            ('Bolo chocoffe', 'Massa molhadinha de chocolate com leve toque de café e cobertura de chocolate - aproximadamente 500g', 90.00, 'images/6.jpeg'),
            ('Torta cookie', 'Massa de cookie e recheio de brigadeiro - aproximadamente 400g', 90.00, 'images/7.jpeg'),
            ('Bolo de ninho', 'Massa de chocolate e cobertura de branquinho de leite ninho - aproximadamente 500g', 90.00, 'images/8.jpeg'),
            ('Bolo de laranja', 'Massa de laranja e cobertura de calda de laranja - aproximadamente 400g', 80.00, 'images/9.jpeg'),
            ('Vulcão de chocolate', 'Massa de fubá ou chocolate com cobertura de brigadeiro - aproximadamente 500g', 90.00, 'images/10.jpeg')
        ]
        
        cursor.executemany('''
            INSERT INTO products (name, description, price, image_path)
            VALUES (?, ?, ?, ?)
        ''', products)
    
    conn.commit()
    conn.close()

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'images'), filename)

@app.route('/api/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return jsonify([dict(product) for product in products])

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.json
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create order
    cursor.execute('''
        INSERT INTO orders (customer_name, customer_phone, customer_email, observations, delivery_date, total_amount, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['customer_name'],
        data['customer_phone'],
        data.get('customer_email', ''),
        data.get('observations', ''),
        data['delivery_date'],
        data['total_amount'],
        'pending',
        datetime.now().isoformat()
    ))
    
    order_id = cursor.lastrowid
    
    # Add order items
    for item in data['items']:
        cursor.execute('''
            INSERT INTO order_items (order_id, product_id, quantity, price)
            VALUES (?, ?, ?, ?)
        ''', (order_id, item['product_id'], item['quantity'], item['price']))
    
    conn.commit()
    
    # Get product names for email
    items_details = []
    for item in data['items']:
        product = conn.execute('SELECT name FROM products WHERE id = ?', (item['product_id'],)).fetchone()
        if product:
            items_details.append(f"{product['name']} (x{item['quantity']}) - R$ {item['price']:.2f}")
    
    conn.close()
    
    # Send email to admin
    try:
        admin_subject = f"Novo Pedido #{order_id} - Alicedelice"
        admin_body = f"""
        Novo pedido recebido!
        
        Pedido #{order_id}
        Cliente: {data['customer_name']}
        Telefone: {data['customer_phone']}
        Email: {data.get('customer_email', 'Não informado')}
        Data de Entrega: {data['delivery_date']}
        
        Observações: {data.get('observations', 'Nenhuma')}
        
        Itens do Pedido:
        {chr(10).join(items_details)}
        
        Total: R$ {data['total_amount']:.2f}
        
        Status: Aguardando análise
        """
        
        msg = Message(
            admin_subject,
            recipients=[ADMIN_EMAIL]
        )
        msg.body = admin_body
        mail.send(msg)
    except Exception as e:
        print(f"Erro ao enviar email para admin: {e}")
    
    # Send confirmation email to customer
    if data.get('customer_email'):
        try:
            customer_subject = f"Confirmação do Pedido #{order_id} - Alicedelice"
            customer_body = f"""
            Olá {data['customer_name']}!
            
            Recebemos seu pedido com sucesso!
            
            Pedido #{order_id}
            Data de Entrega: {data['delivery_date']}
            
            Itens do Pedido:
            {chr(10).join(items_details)}
            
            Total: R$ {data['total_amount']:.2f}
            
            Seu pedido está em análise. Entraremos em contato pelo telefone {data['customer_phone']} para confirmar os detalhes.
            
            Obrigado pela preferência!
            Alicedelice - Doceria Artesanal
            """
            
            msg = Message(
                customer_subject,
                recipients=[data['customer_email']]
            )
            msg.body = customer_body
            mail.send(msg)
        except Exception as e:
            print(f"Erro ao enviar email para cliente: {e}")
    
    return jsonify({'order_id': order_id, 'status': 'success'}), 201

@app.route('/api/orders', methods=['GET'])
def get_orders():
    conn = get_db_connection()
    orders = conn.execute('''
        SELECT o.*, 
               GROUP_CONCAT(p.name || ' (x' || oi.quantity || ')', ', ') as items
        FROM orders o
        LEFT JOIN order_items oi ON o.id = oi.order_id
        LEFT JOIN products p ON oi.product_id = p.id
        GROUP BY o.id
        ORDER BY o.created_at DESC
    ''').fetchall()
    conn.close()
    return jsonify([dict(order) for order in orders])

@app.route('/api/orders/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    data = request.json
    conn = get_db_connection()
    conn.execute('''
        UPDATE orders SET status = ? WHERE id = ?
    ''', (data['status'], order_id))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
