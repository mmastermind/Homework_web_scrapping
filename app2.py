from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars2
from splinter import Browser

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
mongo.db.mars_data.drop()

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find record of data from the mongo database
    mars_data = mongo.db.mars_data.find_one()

    # Return template and data
    return render_template("index_hw.html", mars_data=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mongo.db.mars_data.drop()
    mars_data = mongo.db.mars_data
    # Run the scrape function from file mission_to_mars2   
    mars_inf = mission_to_mars2.scrape_header()
    mars_inf = mission_to_mars2.scrape_weather()
    mars_inf = mission_to_mars2.scrape_jpl()
    mars_inf = mission_to_mars2.scrape_quadrants()
    # mars_inf = mission_to_mars2.scrape_facts()

    # Update the Mongo database using updateOne due to the mongo version and upsert=True
    # mars_data.update_one({}, {"$set": done}, upsert=True)
    print("llegamos")
    print(mars_inf)
    # Syntaxis for insert_one example: result = db.test.insert_one({'x': 1})
    mars_data.insert_one(mars_inf)
    # mars_db.insert_one({"status":"done"})
    print("terminamos")
    # mars_data.update({}, mars_inf, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
