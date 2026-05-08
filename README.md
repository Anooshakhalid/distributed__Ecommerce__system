# Rosélia: Distributed E-Commerce System

A distributed bouquet e-commerce platform developed using microservices architecture.

This project demonstrates core distributed computing concepts including:

* Service separation
* REST API communication
* Independent databases
* Docker containerization
* Gateway-based routing
* Scalable architecture

# Project Overview

Instead of using a monolithic architecture, the application is divided into multiple independent services:

| Service         | Responsibility             | Port |
| --------------- | -------------------------- | ---- |
| Gateway Service | Main entry point / routing | 5000 |
| User Service    | User management            | 5001 |
| Product Service | Bouquet/product management | 5002 |
| Order Service   | Order handling             | 5003 |
| Payment Service | Payment simulation         | 5004 |
| Frontend        | User Interface             | 5005 |

Each service communicates through HTTP REST APIs.
- Each service handles a specific domain
- API Gateway acts as a single entry point
- MySQL is shared across services (separate databases per service)
- Frontend communicates only with Gateway



# Architecture
```
Frontend (Port 5005)
        ↓
API Gateway (Port 5000)
        ↓
--------------------------------
| User Service    (5001)      |
| Product Service (5002)      |
| Order Service   (5003)      |
| Payment Service (5004)      |
--------------------------------
        ↓
      MySQL DB
```      

---

# Project Structure

```text
distributed__Ecommerce__system/
│
├── gateway/
│   └── app.py
│
├── user_service/
│   ├── app.py
│   ├── db.py
│   └── Dockerfile
│
├── product_service/
│   ├── app.py
│   ├── db.py
│   └── Dockerfile
│
├── order_service/
│   ├── app.py
│   ├── db.py
│   └── Dockerfile
│
├── payment_service/
│   ├── app.py
│   ├── db.py
│   └── Dockerfile
│
├── frontend/
│   ├── templates/
│        ├── index.html
│        ├── products.html
│        ├── orders.html
│        └── payment.html
│   ├── app.py
│
├── database_dumps/
│   └── product_db.sql
|   └── payment_db.sql
|   └── user_db.sql
|   └── order_db.sql
│
├── docker-compose.yml
├── init.sql
└── README.md
```

---

# Technologies Used

| Technology       | Purpose               |
| ---------------- | --------------------- |
| Python           | Backend development   |
| Flask            | REST API framework    |
| MySQL            | Database              |
| Docker           | Containerization      |
| HTML/CSS/JS      | Frontend              |
| Requests Library | Service communication |

---

# How To Run The Project

# STEP 1 — Clone the project

```bash
git clone https://github.com/Anooshakhalid/distributed__Ecommerce__system.git
cd distributed__Ecommerce__system
```

# STEP 2 — Install Requirements

Install:

* Python 3
* Docker Desktop

# STEP 3 — Install Python Libraries

Run:

```bash
pip install flask requests mysql-connector-python
pip install flask-cors
```

# STEP 4 — Database Setup

```bash
docker compose up --build
```
OR
Import Database (First Time Setup) - Manual:
```bash
docker exec -i mysql_db mysql -u root -proot product_db < database_dumps/product_db.sql
docker exec -i mysql_db mysql -u root -proot order_db < database_dumps/order_db.sql
docker exec -i mysql_db mysql -u root -proot payment_db < database_dumps/payment_db.sql
docker exec -i mysql_db mysql -u root -proot user_db < database_dumps/user_db.sql
```

Export Database (After Final Updatation)
```bash
docker exec mysql_db mysqldump -u root -proot product_db > database_dumps/product_db.sql
docker exec mysql_db mysqldump -u root -proot order_db < database_dumps/order_db.sql
docker exec mysql_db mysqldump -u root -proot payment_db < database_dumps/payment_db.sql
docker exec mysql_db mysqldump -u root -proot user_db < database_dumps/user_db.sql
```

This creates:

* user_db
* product_db
* order_db
* payment_db

# STEP 5 — Run Gateway

Open another terminal:

```bash
cd gateway
py app.py
```

Gateway runs on:

```text
http://localhost:5000/api/
```

# STEP 6 — Run Frontend

Open another terminal:

```bash
cd frontend
py app.py
```

Frontend runs on:

```text
http://localhost:5005/
```
---

# Docker Usage

## Start Containers

```bash
docker compose up --build
```

## Stop Containers

```bash
docker compose down
```

## Restart Containers

```bash
docker compose restart
```
---

# Sustainability Analysis

The project includes sustainability considerations:

* Independent services reduce unnecessary resource usage.
* Services can scale individually.
* Containerization improves deployment efficiency.
* Distributed systems reduce single-point overload.

---

# License

This project is for academic and educational purposes.
