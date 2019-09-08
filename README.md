# Big Data Content Analytics Assignement

## Downloading the dataset
The dataset we used can be downloaded as a zipped file from [here](https://www.kaggle.com/paramaggarwal/fashion-product-images-small/downloads/fashion-product-images-small.zip/1).

## Creating the dataset
Line 41 to line 97 were run localy in order to create the datased for our model
Then the folders were uploaded to google drive so that the data can be accesed from google Colab

## Image Respository
In lines 249 to 259 we move all the images we used from the multiple directories we created to a common one. It is the directory where based on the nearest neighbor algorithm results which we can quiry to fetch the 10 most simiral clothes.  

## Results
Once all the code is run, libraries loaded and the model and functions initiated then function recommend_me() on line 290 will accept as input a path of an image and plot as output the most similar ones.

## Trained model
You can find the model already trained in the flask_app directory ofths repository saved as a `.h5` file and load it using the `load_model('image_class_model')` command.
