# Library Management System (DDD)

This project is a **Library Management System** built using **Domain-Driven Design (DDD)** principles. It allows users to borrow books and manage memberships while ensuring data consistency and business logic encapsulation.

## Features
- **Domain-Driven Design (DDD)**: Follows a structured domain model.
- **Unit of Work Pattern**: Ensures data consistency.
- **Event-Driven Architecture**: Uses an event-driven approach with a message bus.
- **SQLAlchemy ORM**: Handles database operations efficiently.
- **Message Bus**: Manages domain events asynchronously.

## Technologies Used
- **Python 3.x**
- **SQLAlchemy**
- **PostgreSQL**
- **Domain-Driven Design (DDD)**
- **Unit of Work Pattern**
- **Event-Driven Architecture**

## Project Structure
```
├── adapters
│   ├── repository.py
│   ├── orm.py
├── domain
│   ├── model.py
├── event_handlers
│   ├── message_bus.py
├── service_layer
│   ├── issue_book_service.py
│   ├── unit_of_work.py
|   ├── due_date_calculator.py   
├── tests
│   ├── test_issue_book.py
├── .gitignore
├── README.md
```

## Installation & Setup
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/library-management-ddd.git
cd library-management-ddd
```

### 2. Create a Virtual Environment & Install Dependencies
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up the Database
> **Note:** Update `DATABASE_URL` in `database.py` before proceeding.

```sh
python -c 'from database import init_db; init_db()'
```

### 4. Run the Application
```sh
python main.py
```

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License.

