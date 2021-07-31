FROM python:3.8

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this
# instruction creates a directory with this name if it doesn’t exist
WORKDIR /app

# Install any needed packages specified in requirements.txt
#RUN chown -R www-data:www-data /var/www/html/storage
#RUN chmod 777 /var/www/html/storage


COPY requirements.txt /app


RUN pip install -r requirements.txt

# Run appr.py when the container launches
COPY src/ .
#COPY . .

CMD python app.py

