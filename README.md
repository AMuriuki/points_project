# Grid Point API

The Grid Point API receives a set of points on a grid as semicolon separated values. It finds the points that are closest to each other and stores the received set of points and the closest points on a DB.

## Installation
1. Clone the repository:
```bash
$ git clone https://github.com/AMuriuki/points_project.git
```

2. Change into the project directory:
```bash
$ cd points_project
```

3. Create a virtual environment:
```bash
$ python3 -m venv venv
```

4. Activate the virtual env:
* On MacOs/Linux
```bash
$ source venv/bin/activate
```

* On Windows
```bash
$ venv\Script\activate
```

5. Install dependencies
```bash
$ pip install -r requirements.txt
```

6. Apply DB migrations
```bash
$ python manage.py migrate
```

7. Create super user (provide username & password of choice)
```bash
$ python manage.py createsuperuser 
```

8. Start development server
```bash
$ python manage.py runserver
```

9. To access Admin Panel
```bash
$ http://127.0.0.1:8000/admin
```

## API Endpoints
* `POST /api/process-grid-points`: Accepts a set of points on a grid as input and process them

## Usage
To use the API, make a `POST` request to the `/api/process-grid-points` endpoint with the following parameters:

* `points`: A semicolor-seperated string of points on a grid, where each point consists of x and y coordinates separated by a comma

### Example Request:

```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"points": "2,2;-1,30;20,11;4,5"}' http://localhost:8000/api/process-grid-points/
```

### Example Response:
```bash
{
    "message": "Grid points processed successfully"
}
```

## Testing
To run the test suite, run the following command:
```bash
$ python manage.py test
```