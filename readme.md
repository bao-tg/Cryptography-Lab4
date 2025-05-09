# Introduction

This is the lab 4, web attacks, for the course Cryptography, at VinUniversity, Spring 25.

The [report](Lab4%20-%20Lab.pdf).


# Getting started

Requirements:
+ Docker

Builder the docker image:
```bash
docker build -t flask-secure-app .
```

Run the container:
```bash
docker run -d -p 5000:5000 --name flask-secure-container flask-secure-app
```

Visit the app (open your browser and type):
```bash
http://localhost:5000
```

Manage the container:
+ View logs:
```bash
docker logs flask-secure-container
```

+ Stop the container:
```bash
docker stop flask-secure-container
```

+ Remove the container:
```bash
docker rm flask-secure-container
```
