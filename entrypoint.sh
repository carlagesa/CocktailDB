#!/bin/sh

# Exit on error
set -e

# This script is executed on container startup.
# It applies database migrations before starting the main application.

echo "Applying database migrations..."
python manage.py migrate

# The 'exec "$@"' command replaces the script process with the command
# passed as arguments to the script. In the Dockerfile, this will be the
# gunicorn command.
echo "Starting server..."
exec "$@"