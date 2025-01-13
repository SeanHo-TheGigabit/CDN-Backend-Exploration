# Contents of /flask-smorest-app/flask-smorest-app/migrations/README.md

This directory contains the migration scripts for the Flask-Smorest application. 

To manage database schema changes, we use Flask-Migrate, which is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.

## Getting Started with Migrations

1. **Initialize Migrations**: 
   If you haven't already initialized migrations, run the following command:
   ```
   flask db init
   ```

2. **Create a Migration**: 
   To create a new migration script after making changes to your models, use:
   ```
   flask db migrate -m "Description of changes"
   ```

3. **Apply Migrations**: 
   To apply the migration to the database, run:
   ```
   flask db upgrade
   ```

4. **Downgrade Migrations**: 
   If you need to revert to a previous migration, you can downgrade using:
   ```
   flask db downgrade
   ```

## Important Commands

- `flask db current`: Show the current migration version.
- `flask db history`: Show the migration history.
- `flask db stamp`: Stamp the current revision without running migrations.

For more detailed information, refer to the Flask-Migrate documentation.