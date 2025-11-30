# Installation & Setup Guide

## Prerequisites

- **Python 3.9+** - Download from [python.org](https://www.python.org/)
- **PostgreSQL 12+** - Download from [postgresql.org](https://www.postgresql.org/)
- **Redis 6+** - Download from [redis.io](https://redis.io/)
- **Node.js 16+** (optional, for frontend development)
- **Docker & Docker Compose** (optional, for containerized deployment)
- **Git** - For version control

---

## Option 1: Local Development Setup (Without Docker)

### Step 1: Clone Repository
```bash
git clone https://github.com/rb8406605-cmd/bromcom-2-mis-school-syterm.git
cd bromcom-2-mis-school-syterm
```

### Step 2: Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
```bash
# Copy example env file
cp .env.example .env

# Edit .env with your settings
nano .env  # or use your preferred editor
```

**Key variables to update:**
- `SECRET_KEY` - Generate a random secret key
- `DEBUG` - Set to False in production
- `DATABASE_URL` - Your PostgreSQL connection string
- `REDIS_URL` - Your Redis connection string
- `SENDGRID_API_KEY` - For email notifications
- `TWILIO_ACCOUNT_SID` - For SMS notifications

### Step 5: Create PostgreSQL Database
```bash
# Connect to PostgreSQL
psql -U postgres

# Create database and user
CREATE DATABASE bromcom_db;
CREATE USER bromcom_user WITH PASSWORD 'secure_password';
ALTER ROLE bromcom_user SET client_encoding TO 'utf8';
ALTER ROLE bromcom_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE bromcom_user SET default_transaction_deferrable TO on;
ALTER ROLE bromcom_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE bromcom_db TO bromcom_user;
\q
```

### Step 6: Run Database Migrations
```bash
python manage.py migrate
```

### Step 7: Create Superuser Account
```bash
python manage.py createsuperuser
# Follow prompts to create admin account
```

### Step 8: Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Step 9: Start Redis Server (in separate terminal)
```bash
# macOS
redis-server

# Ubuntu/Linux
redis-server

# Windows (if installed via WSL)
redis-server
```

### Step 10: Start Celery Worker (in separate terminal)
```bash
celery -A bromcom worker -l info
```

### Step 11: Start Development Server
```bash
python manage.py runserver
```

**Access the application:**
- Web Interface: http://localhost:8000
- Admin Panel: http://localhost:8000/admin
- API Documentation: http://localhost:8000/api/docs

---

## Option 2: Docker Deployment

### Step 1: Ensure Docker is Running
```bash
docker --version
docker-compose --version
```

### Step 2: Configure Environment
```bash
cp .env.example .env
# Edit .env if needed
```

### Step 3: Build and Start Containers
```bash
docker-compose up -d
```

This will start:
- **PostgreSQL Database** (Port 5432)
- **Redis Cache** (Port 6379)
- **Django Web Server** (Port 8000)
- **Celery Worker** (Background tasks)
- **Celery Beat** (Scheduled tasks)

### Step 4: Run Migrations in Container
```bash
docker-compose exec web python manage.py migrate
```

### Step 5: Create Superuser in Container
```bash
docker-compose exec web python manage.py createsuperuser
```

### Step 6: Access Application
- Web Interface: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

### Step 7: Stop Containers
```bash
docker-compose down
```

### Useful Docker Commands
```bash
# View logs
docker-compose logs -f web

# Execute command in container
docker-compose exec web python manage.py shell

# Rebuild containers
docker-compose up --build

# Remove all containers and volumes
docker-compose down -v
```

---

## Option 3: Production Deployment (Cloud)

### AWS EC2 Deployment

#### Step 1: Launch EC2 Instance
- AMI: Ubuntu 22.04 LTS
- Instance Type: t3.small (minimum)
- Security Group: Allow ports 80, 443, 22

#### Step 2: Connect and Update System
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
sudo apt update && sudo apt upgrade -y
```

#### Step 3: Install Dependencies
```bash
sudo apt install -y python3.11 python3-pip postgresql postgresql-contrib \
    redis-server nginx git curl

# Install Node.js (optional)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
```

#### Step 4: Clone and Setup Application
```bash
cd /var/www
sudo git clone https://github.com/rb8406605-cmd/bromcom-2-mis-school-syterm.git
cd bromcom-2-mis-school-syterm
sudo python3 -m venv venv
source venv/bin/activate
sudo pip install -r requirements.txt
```

#### Step 5: Configure Database
```bash
sudo -u postgres psql
CREATE DATABASE bromcom_db;
CREATE USER bromcom_user WITH PASSWORD 'strong_password';
ALTER ROLE bromcom_user SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE bromcom_db TO bromcom_user;
\q
```

#### Step 6: Setup Environment and Migrations
```bash
cp .env.example .env
sudo nano .env  # Configure with production settings
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

#### Step 7: Configure Gunicorn
```bash
pip install gunicorn
# Create systemd service file
sudo nano /etc/systemd/system/bromcom.service
```

Add the following content:
```ini
[Unit]
Description=Bromcom Django Application
After=network.target postgresql.service

[Service]
Type=notify
User=ubuntu
Group=www-data
WorkingDirectory=/var/www/bromcom-2-mis-school-syterm
ExecStart=/var/www/bromcom-2-mis-school-syterm/venv/bin/gunicorn \
    --workers 3 \
    --bind 127.0.0.1:8000 \
    bromcom.wsgi:application

Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

#### Step 8: Start Services
```bash
sudo systemctl enable bromcom
sudo systemctl start bromcom
sudo systemctl enable celery
sudo systemctl start celery
```

#### Step 9: Configure Nginx
```bash
sudo nano /etc/nginx/sites-available/bromcom
```

Add proxy configuration to forward requests to Gunicorn on port 8000.

#### Step 10: Install SSL Certificate (Let's Encrypt)
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot certonly --nginx -d yourdomain.com
```

---

## Verification Checklist

After installation, verify:

- [ ] PostgreSQL database created and accessible
- [ ] Redis server running and accessible
- [ ] Django migrations completed successfully
- [ ] Static files collected
- [ ] Superuser account created
- [ ] Development server starts without errors
- [ ] Admin panel accessible at `/admin`
- [ ] API documentation accessible
- [ ] Celery worker running (if using background tasks)
- [ ] Email sending configured (if using notifications)

---

## Troubleshooting

### Issue: Database Connection Error
```bash
# Check PostgreSQL is running
sudo service postgresql status

# Verify credentials in .env
cat .env | grep DATABASE
```

### Issue: Redis Connection Error
```bash
# Check Redis is running
redis-cli ping
# Should return: PONG
```

### Issue: Permission Denied Errors
```bash
# Ensure user has proper permissions
sudo chown -R $USER:$USER .
chmod -R 755 .
```

### Issue: Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000

# Kill process (on Linux/Mac)
kill -9 <PID>
```

### Issue: Module Import Errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

---

## Next Steps

1. **Create your first data entry**: Use `python manage.py shell` or the web interface
2. **Configure notification services**: Setup SendGrid and Twilio
3. **Customize settings**: Edit configuration in Django admin
4. **Deploy to production**: Follow cloud deployment guide above
5. **Setup monitoring**: Configure Sentry and logging
6. **Backup strategy**: Setup automated database backups

---

## Support

For issues:
1. Check the FAQ section below
2. Review application logs: `tail -f logs/bromcom.log`
3. Check system logs: `sudo tail -f /var/log/syslog`
4. Review error messages carefully and search online

---

## System Requirements

### Minimum (Small School - 500 students)
- CPU: 2 cores
- RAM: 4 GB
- Storage: 20 GB SSD
- Database: PostgreSQL 12+
- Cache: Redis 6+

### Recommended (Medium School - 2000 students)
- CPU: 4 cores
- RAM: 8 GB
- Storage: 50 GB SSD
- Database: PostgreSQL 14+
- Cache: Redis 6+

### Production (Large School - 5000+ students)
- CPU: 8+ cores
- RAM: 16+ GB
- Storage: 100+ GB SSD/NVMe
- Database: PostgreSQL 15+, with replication
- Cache: Redis cluster
- Load Balancer: Nginx or AWS ELB

---

**Installation Complete!** 🎉

You can now start using Bromcom for managing attendance, behavior, and detention in your school.
