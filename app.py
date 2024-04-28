from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [    
    {
        'id': 1,
        'titulo': 'A pequena coreografia do adeus',
        'autor': 'Aline Bei'
    },
    {
        'id': 2,
        'titulo': 'Tudo o que eu sei sobre o amor',
        'autor': 'Dolly Alderton'
    },
    {
        'id': 3,
        'titulo': 'A metamorfose',
        'autor': 'Franz Kafka'
    }
]

@app.route('/livros/criar', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro)

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

@app.route('/livros/editar/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livro.update(livro_alterado)
            return jsonify(livro)
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

@app.route('/livros/excluir/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify({'mensagem': 'Livro excluído com sucesso'})
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

if __name__ == "__main__":
    app.run()



















