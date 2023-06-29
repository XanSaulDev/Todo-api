pip install -r requirements/production.txt
python3.9 manage.py collectstatic --no-input
python3.9 manage.py migrate --fake