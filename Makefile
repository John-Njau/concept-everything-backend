migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

serve:
	python manage.py runserver

superuser:
	python manage.py createsuperuser

shell:
	python manage.py shell

test:
	python manage.py test

# Path: Makefile

newapp:
	django-admin startapp $(app)