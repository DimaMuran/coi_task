# Setup
 - git clone https://github.com/DimaMuran/coi_task.git
 - pip install -r requirements.txt
 - python manage.py makemigrations
 - python manage.py migrate
 - python manage.py runserver

# Routes
## Returns list of directions
 - .../api/directions
## Returns list of doctors and some filter and order queries
 - .../api/doctors
 - .../api/doctors?page=2
 - .../api/doctors?direction__name=Direction1
 - .../api/doctors?exp_from=5
 - .../api/doctors?exp_to=5
 - .../api/doctors?experience=5
 - .../api/doctors?ordering=-birthday
## Return specific doctor
 - .../api/doctors/1
