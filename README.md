"# Lab05" 
pip install django 
pip install django pillow
pip install -r requirements.txt
cd src
python manage.py makemigrate
python manage.py migrate
python manage.py createsuperuser  
python manage.py runserver


 Example Data
 python manage.py populate_db
