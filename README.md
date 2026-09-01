# Healthcare System Backend

A RESTful healthcare backend built with Django REST Framework and PostgreSQL for managing users, patients, doctors, and patient-doctor mappings.

## Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- Postman

## APIs

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and obtain JWT tokens |

### Patients

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/patients/` | Create a patient |
| GET | `/api/patients/` | Get all patients |
| GET | `/api/patients/<id>/` | Get patient by ID |
| PUT | `/api/patients/<id>/` | Update patient |
| PATCH | `/api/patients/<id>/` | Partially update patient |
| DELETE | `/api/patients/<id>/` | Delete patient |

### Doctors

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/doctors/` | Create a doctor |
| GET | `/api/doctors/` | Get all doctors |
| GET | `/api/doctors/<id>/` | Get doctor by ID |
| PUT | `/api/doctors/<id>/` | Update doctor |
| PATCH | `/api/doctors/<id>/` | Partially update doctor |
| DELETE | `/api/doctors/<id>/` | Delete doctor |

### Patient-Doctor Mapping

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/mappings/` | Assign a doctor to a patient |
| GET | `/api/mappings/` | Get all patient-doctor mappings |
| GET | `/api/mappings/<patient_id>/` | Get doctors assigned to a patient |
| DELETE | `/api/mappings/<id>/` | Remove a doctor from a patient |

## Environment Setup

Create a `.env` file in the project root directory:

```env
SECRET_KEY=your_django_secret_key

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432