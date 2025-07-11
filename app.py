from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask CI/CD Demo</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin: 50px; }
            .container { max-width: 600px; margin: 0 auto; }
            h1 { color: #333; }
            .info { background-color: #f0f8ff; padding: 20px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Flask CI/CD Demo</h1>
            <div class="info">
                <h2>Chào mừng đến với ứng dụng Flask!</h2>
                <p>Ứng dụng này được triển khai tự động bằng Jenkins và Docker.</p>
                <p><strong>Version:</strong> 1.0.0</p>
                <p><strong>Status:</strong> Đang chạy thành công! ✅</p>
            </div>
        </div>
    </body>
    </html>
    ''')

@app.route('/health')
def health():
    return {'status': 'healthy', 'version': '1.0.0'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
