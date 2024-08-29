# JRAR
## What is it?
A school project. It demonstrates automotive IoT (sort of). This repo stores the Django backend and React frontend. 

[**React frontend**](https://github.com/lostmypillow/jRAR-web)

[**Demo website**](https://lostmypillow.github.io/jRAR-web)

[**API Docs**](https://jrar.lostmypillow.duckdns.org/api/docs)

[**Backup API Docs (Loads slow!)**](https://jrar-latest.onrender.com/api/docs)


**Demo video below**

https://github.com/user-attachments/assets/7e0da181-2ff6-4c8c-aa30-8ee38f792b5e


## How does it work?
1. One swiped an RFID card against an RFID sensor connected to an Arduino.
2. The Arduino send the card number to the Raspberrry Pi 400 via wired connection
3. Pi 400 sends the data using a Python script to our Django (also Python) backend
4. Backend checks card data against known numbers in database, which one can add via the React frontend
5. Backend sends "ok" or "not authorized" signal to RPi
6. RPi sends 0 or 9 to Arduino
7. Arduino flashes light differently based on the number it recieves. (couldn't get this part right tho)
![image](https://github.com/user-attachments/assets/a81383d4-4c07-4278-bba2-7929305c2db2)

## Tech Stack
- **Django Ninja** API endpoints
- **SQLite** database
- **Vite(React)** frontend x **MUI** components



