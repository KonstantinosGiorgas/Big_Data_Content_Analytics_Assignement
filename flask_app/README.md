# Flask Deployment

The steps in deployng the algorithm to Flask are the following:
1. Save in the same directory recommend_me.py and image_class_model.h5 and name the directory flask_app
2. Open the command prompt with administrator rights and browse to the directory were recommend_me.py and image_class_model.h5 are located: `cd C:\flask_app`
3. Export the application to Flask using the following command: `set FLASK_APP=recommend_me.py`
4. Start Flask and make the webservise visible andavailabel to all computers in the network using the follwing command: `flask run --host=0.0.0.0` or `flask run` to make the service available only through your local machine.  Your service is up and running! 
