pip install -r requirements.txt
python3.9 manage.py makemigrations
python3.9 manage.py migrate --fake
python3.9 manage.py collectstatic