{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import mission_to_mars\n",
    "\n",
    "# Create an instance of Flask\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Use PyMongo to establish Mongo connection\n",
    "mongo = PyMongo(app, uri=\"mongodb://localhost:27017/weather_app\")\n",
    "\n",
    "\n",
    "# Route to render index.html template using data from Mongo\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "\n",
    "    # Find one record of data from the mongo database\n",
    "    destination_data = mongo.db.collection.find_all()\n",
    "\n",
    "    # Return template and data\n",
    "    return render_template(\"index.html\", news=mars_data)\n",
    "\n",
    "\n",
    "# Route that will trigger the scrape function\n",
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "\n",
    "    # Run the scrape function\n",
    "    mars_data = mission_to_mars.scrape_info()\n",
    "\n",
    "    # Update the Mongo database using update and upsert=True\n",
    "    mongo.db.collection.update({}, mars_data, upsert=True)\n",
    "\n",
    "    # Redirect back to home page\n",
    "    return redirect(\"/\")\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
