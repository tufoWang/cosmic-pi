# scripts/backup.py

import os
import shutil
from datetime import datetime

def backup():
    """Create a backup of the database and configuration files."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir = f"backup_{timestamp}"

    # Create backup directory
    os.makedirs(backup_dir, exist_ok=True)

    # Backup database (example for PostgreSQL)
    db_url = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost/dbname')
    db_name = db_url.split('/')[-1]
    os.system(f"pg_dump {db_url} > {backup_dir}/{db_name}_backup.sql")

    # Backup configuration files
    shutil.copy('src/config/config.py', backup_dir)
    shutil.copy('src/config/logging_config.py', backup_dir)
    shutil.copy('src/config/database_config.py', backup_dir)

    print(f"Backup created successfully in {backup_dir}.")

if __name__ == "__main__":
    backup()
