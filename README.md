# Food-Co-op | Greenhill Food Co-op Ordering System

A web-based ordering and distribution management system built for community food cooperatives. The system streamlines member ordering, round-based order lifecycle management, product catalog maintenance, wholesale order aggregation, and on-site packing sheet generation, replacing manual spreadsheet workflows.

## Key Features

### Member Side
- Member registration, login and profile management
- Browse open order rounds and place orders
- Support two pricing modes: per-unit and per-weight (kg)
- Price locking at order placement time
- Personal order history and detail view
- Role-based access control (members only access own orders)

### Coordinator Side
- Order round management (create, open, close, mark as packed)
- Product catalog management (add, edit, activate/deactivate, bay location assignment)
- Round-wide order overview by member
- Automated wholesale purchase order aggregation (total quantities per product)
- Printable packing sheet sorted by crate number with bay locations
- Actual packed quantity recording fields for on-site use

## Tech Stack
- **Backend**: Python 3.10 + Flask 3.0
- **ORM**: Flask-SQLAlchemy 3.1
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: Bootstrap 5.3 + Jinja2 templates
- **Version Control**: Git + GitHub
- **Deployment**: Render Platform
- **CI/CD**: GitHub Actions

## Local Run Guide

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/060104-hwb/Food-Co-op.git
   cd Food-Co-op
