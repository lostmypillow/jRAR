# RAR Server
Django API Backend for Raspberry Pi | Arduino | RFID Project

[Demo/API Documentation](https://rarserver.onrender.com/api/docs)

Or alternatively pull my Docker image:

```bash
#ARM64 version
docker pull lostmypillow/rarserver:1.0.4

#AMD64 version
docker pull lostmypillow/rarserver:1.0.3
```


[GitHub for RAR Client](https://github.com/lostmypillow/rarclient)

## Tech Stack
**Django** with **Django Ninja** and **SQLite**


## Recreate this Project

```bash
python -m pip install -r requirements.txt
python -m manage.py runserver
# OR alternatively run it as a Docker container
docker compose up
```


## Future for this Project

### Mobile App
I want an app for it

### Dark Mode
Self explanatory.
