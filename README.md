
# 🍸 🍹🥂🍷🍸🍾🍹CocktailDB

This API contains a collection of free, open source cocktail data. This project was created for entry level developers who need access to free API's. The API is built using Django Rest framework.

## 🚀 **Exciting Upcoming Features**

We're constantly evolving CocktailDB to better serve our developer community. Here's a sneak peek at some of the **awesome features** we're currently working on:

### 🎯 **1. Enhanced API Rate Limiting**
   - **Protect your usage:** Sophisticated rate limiting to ensure fair use and protect against abuse.
   - **Custom limits:** Personalized limits based on usage tiers.

### ⚡ **2. Blazing Fast Caching**
   - **Speed up your requests:** Caching frequently requested data to drastically reduce response times.
   - **Seamless experience:** Enjoy faster and more efficient data retrieval.

### 🔐 **3. Secure User Authentication**
   - **Keep it personal:** Implementing token-based authentication for secure and personalized API access.
   - **Your data, your rules:** Control who can access your API data.

### 🔍 **4. Advanced Search Capabilities**
   - **Powerful search:** Introducing multi-ingredient filtering and complex queries.
   - **Find exactly what you need:** More flexibility and precision in search results.

### 🥂 **5. Discover Popular & Latest Cocktails**
   - **Stay trendy:** New endpoints to showcase the most popular cocktails.
   - **What's new?** Easily discover the latest additions to the cocktail database.

### 📸 **6. High-Quality Ingredient Images**
   - **Visual delight:** Adding ingredient images in various resolutions (small, medium, large) to enhance API data.
   - **More than just text:** Elevate your application with stunning visual elements.

---

✨ **Stay tuned for these features and more as we continue to make CocktailDB the best API for developers!**


## Screenshots
<img src="https://github.com/carlagesa/CocktailDB/blob/main/templates/assets/img/Swagger.png?raw=true" alt="Success!" width="450"/>

## API Reference
The API reference is also accessible from the [API link](https://cocktaildb-one.vercel.app/) . This is made possible by the implementation of a preetry cool platform called Swagger.

Swagger is an Open Source set of rules, specifications and tools for developing and describing RESTful APIs. The Swagger framework allows developers to create interactive, machine and human-readable API documentation.


## Deployment

The project is currently deployed on Vercel and uses PostgreSQL.


## Run Locally

Clone the project

```bash
  git clone https://github.com/carlagesa/CocktailDB.git
```

Go to the project directory

```bash
  cd CocktailDB
```

Create you virtual environment & activate it.

```bash
  py -m venv myenv
```
```bash
  myenv\Scripts\activate.bat
```


Install from requirements.txt file

```bash
  pip freeze -r requirements.txt
```
Run migrations & start server

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```
## CocktailDB🍹 Web Scrapper
For the data to populate the DB check my other repository built specicically for this project. It scrapes the internet for cocktail data and arranges the data into
an excel sheet which later can be imported into the DB using one command.For more info on this, checkout the [Cocktail Scrapper](https://github.com/carlagesa/Cocktail-Scrapper.git).<br>
Although to save on time I took the initiative to place the already populated excel sheet inside the data folder. Quickly run👇🏾
```bash
  python manage.py populate_db_from_excel <path_to_excel_file>
```

Example:
```bash
  python manage.py populate_db_from_excel data/cocktail_data.xlsx
```

### Successfully imported cocktail data
<img src="https://github.com/carlagesa/CocktailDB/blob/main/templates/assets/img/import_data.png?raw=true" alt="Success!" width="450"/>

## Tech Stack

**Server:** Python, Django, PostgreSQL, Swagger API Doc


## Authors

- [@carlagesa](https://www.github.com/carlagesa)👨🏾‍💻

For project opportunities kindly check github profile for social links😊
