# Coupon Collection & Redemption System

A Django-based platform for collecting and redeeming coupons with WhatsApp OTP verification.

## Prerequisites
*   Python 3.9+
*   Redis (for Celery tasks)

## Installation

1.  **Clone/Navigate to directory**:
    ```bash
    cd coupon_project
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Create Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run Redis** (Make sure Redis is installed and running):
    ```bash
    redis-server
    ```

6.  **Run Celery Worker**:
    ```bash
    celery -A coupon_project worker --loglevel=info
    ```

7.  **Run Development Server**:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Authentication
*   POST `/api/auth/register/` - Register
*   POST `/api/auth/login/` - Login (Get JWT)

### Coupons
*   GET `/api/coupons/` - List Coupons

### Verification
*   POST `/api/verification/request/<id>/` - Request OTP (Requires Auth)
*   POST `/api/verification/verify/<id>/` - Verify OTP & Collect (Requires Auth, triggers Collection)

### Redemptions
*   GET `/api/redemptions/my-coupons/` - My Collected Coupons
*   POST `/api/redemptions/redeem/` - Redeem Coupon (Body: `{"coupon_code": "..."}`)
