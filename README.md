# 🍸 CocktailDB API

Welcome to **CocktailDB**, a Django-based API providing a collection of free, open-source cocktail data. Perfect for entry-level developers needing access to cocktail data APIs. With this API, you can easily search, filter, and manage cocktail recipes.

## 📸 Screenshots

![Swagger Interface](https://github.com/carlagesa/CocktailDB/blob/main/templates/assets/img/Swagger.png?raw=true)

## 📖 API Reference

Explore the API documentation and test endpoints interactively using the following platforms:

- [Swagger](https://cocktaildb-one.vercel.app/) - Interactive API documentation.
- [Postman](https://documenter.getpostman.com/view/21460726/2sA3s3GW7A) - Import our Postman collection to test endpoints.
- [Insomnia](https://insomnia.rest) - Use our Insomnia workspace for efficient API testing.

## 🛠️ Features
- Search Cocktails by Name - Find cocktails by specifying their name.
- List All Cocktails by First Letter - Retrieve cocktails starting with a specific letter.
- Search Ingredients by Name - Locate cocktails based on ingredients.
- Lookup Full Cocktail Details by ID - Get comprehensive details of a cocktail using its ID.
- Lookup Ingredient by ID - Retrieve details of an ingredient using its ID.
- Lookup a Random Cocktail - Get a random cocktail recipe.
- Search by Ingredient - Find cocktails that contain a specific ingredient.
- Filter by Alcoholic, Category, and Glass - Refine your search based on whether the drink is alcoholic, its category, or the type of glass used.
- List Categories, Glasses, Ingredients, and Alcoholic Filters - Obtain lists of available categories, glasses, ingredients, and alcoholic types.

🔒 Authentication and Rate Limiting
Authentication: Token-based authentication is implemented. Use your token in the Authorization header as Token your_token_here.

The project is deployed on Vercel and uses PostgreSQL as the database backend.
## 🔧 Tech Stack
- Backend: Python, Django
- Database: PostgreSQL
- API Documentation: Swagger, Postman, Insomnia
- Deployment: Vercel 

## 🛠️ Run Locally

To run the project locally, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/carlagesa/CocktailDB.git
    ```

2. **Navigate to the Project Directory**

    ```bash
    cd CocktailDB
    ```

3. **Create and Activate a Virtual Environment**

    ```bash
    py -m venv myenv
    ```

    On Windows:

    ```bash
    myenv\Scripts\activate.bat
    ```

    On macOS/Linux:

    ```bash
    source myenv/bin/activate
    ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run Migrations and Start the Server**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```


## 👥 Authors
- Calton Agesa 👨🏾‍💻
For project opportunities and more, check out my GitHub profile.

## 📝 License
- This project is licensed under the MIT License. See the LICENSE file for details.