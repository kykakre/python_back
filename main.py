from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Конфигурация подключения к базе данных PostgreSQL
db_config = {
    'dbname': 'dialogues_db',
    'user': 'postgres',
    'password': '1412',
    'host': 'localhost',
    'port': 5432
}

def get_db_connection():
    conn = psycopg2.connect(**db_config)
    return conn

@app.route('/api/dialogues', methods=['GET'])
def get_dialogues():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM dialogues')
    dialogues = cur.fetchall()
    cur.close()
    conn.close()

    # Преобразование данных в JSON-совместимый формат
    dialogues_list = []
    for dialogue in dialogues:
        dialogues_list.append({
            'id': dialogue[0],
            'start_time': dialogue[1],
            'last_message_time': dialogue[2],
            'company': dialogue[3],
            'employee': dialogue[4],
            'comments': dialogue[5]
        })

    return jsonify(dialogues_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
