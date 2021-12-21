# API-python

git clone <give the link>

pip install -r requirements.txt ---> all necessary libraries install
Better to use virtual environment before installing all libraries
  python -m venv <venv name>
  source <venv name>/bin/activate

Run the api.py code
Open postman with link generated
1. http://127.0.0.1:5000/Students --> Get all details of students (GET method)
2. http://127.0.0.1:5000/Students/ind/<Some ID to give> -->Get deatils of given Id (GET method)
3. http://127.0.0.1:5000/Students/upd/<ID> --> Updates given details for given ID (PUT method)
  In header --> key: content-type, accept & value:application/json, application/json
  In body --> select raw and given details for corresponding update
4. http://127.0.0.1:5000/Students/add --> Create new ID for given details and add them to Details list (POST method)
  In header --> key: content-type, accept & value:application/json, application/json
  In body --> select raw and given details for corresponding update
5. http://127.0.0.1:5000/Students/rem/<ID> --> delets details for given ID (DELETE method) 
