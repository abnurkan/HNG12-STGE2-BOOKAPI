from tests import client


def test_get_all_books():
    """Test retrieving all books."""
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) == 3  # Ensure there are 3 books


def test_get_single_book():
    """Test retrieving a specific book by ID."""
    response = client.get("/books/1")
    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"


def test_create_book():
    """Test creating a new book."""
    new_book = {
        "id": 4,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "publication_year": 1997,
        "genre": "Fantasy",
    }
    response = client.post("/books/", json=new_book)
    assert response.status_code == 201

    data = response.json()
    assert data["id"] == 4
    assert data["title"] == "Harry Potter and the Sorcerer's Stone"


def test_update_book():
    """Test updating an existing book."""
    updated_book = {
        "id": 1,
        "title": "The Hobbit: An Unexpected Journey",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    response = client.put("/books/1", json=updated_book)
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "The Hobbit: An Unexpected Journey"


def test_delete_book():
    """Test deleting a book by ID."""
    response = client.delete("/books/3")
    assert response.status_code == 204

    # Verify the book is actually deleted
    response = client.get("/books/3")
    assert response.status_code == 404
