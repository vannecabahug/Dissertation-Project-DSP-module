# Dissertation-Project-DSP-module
A recommender system specifically designed for restaurants in London as my university dissertation project.
Built with Python on Visual Studio.

My attempt at creating a system named RRS (Restaurant Recommender System); the system is based on a colloborative filtering method which used matrix factorization.
Trip Advisor's dataset on restaurants was downloaded online and used to map outputs to restaurants in London. Their data included the name of places, ranking and ratings, price ranges and user reviews.

On compilation, the program will proceed to truncate data to get only what is necessary then will proceed with matrix factorization techniques.

The program will ask to enter the name of a restaurant in order to generate recommendations based on similar features.

***IMPORTANT***
Use specific names given only from TA's dataset provided as restaurants unlisted in the set will be unknown as no data is provided.
The int variable assigned ***rec_amount*** is to only be changed. This tries to lower the amount of recommendations as much as possible.
