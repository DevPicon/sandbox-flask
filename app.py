from flask import Flask, jsonify, request
app = Flask(__name__)

from books import books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

@app.route('/api/books/<string:book_name>', methods=['GET'])
def get_book(book_name):
    print(book_name)
    book_found = [book for book in books if book['name'] == book_name]
    if (len(book_found) > 0):
        return jsonify({"book": book_found[0]})
    return jsonify({"message": "Book not found"})

@app.route('/api/book', methods=['POST'])
def add_book():
    new_book = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    books.append(new_book)
    return jsonify({
        "message": "Book added successfully",
        "books": books
    })

@app.route('/api/books/<string:book_name>', methods=['PUT'])
def update_book(book_name):
    book_found = [book for book in books if book['name'] == book_name]
    if (len(book_found) > 0):
        book_found[0]['name'] = request.json['name']
        book_found[0]['price'] = request.json['price']
        book_found[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Book updated",
            "book": book_found[0]
        })
    return jsonify({"message":"Book not found"})

@app.route('/api/books/<string:book_name>', methods=['DELETE'])
def delete_book(book_name):
    book_found = [book for book in books if book['name'] == book_name]
    if(len(book_found) > 0):
        books.remove(book_found[0])
        return jsonify({
            "message": "Book deleted",
            "books": books
        })
    return jsonify({"message": "Book not found"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    