# Deploying Flask App in Azure Linux VM

# Setting up the VM
Boot a linux VM in azure. In the portal, navigate to the VM page, go to networking. Add inbound rule for port 5000 in the security group of the VM.

Port 5000 will be used for testing flask application.

# Install dependencies
`$ sudo apt-get install python python-pip`

# Create virtualenv
`$ mkdir -p www/flaskapp `
`$ cd www/flaskapp`
`$ pip3 install virtualenv	`
`$ python3 -m virtualenv flaskenv 	`
`$ chmod 755 flaskenv/ `

# Install python dependencies
`$ source flaskenv/bin/activate`
`$ python -V`
`$ pip install flask`

# Run the flask application
`$ FLASK_APP=app.py`
`$ flask run -h 0.0.0.0`

# Billing Cost 
Below is the screenshot of the billing cost of all the resources associated with this project

![Screenshot 2022-09-21 155423](https://user-images.githubusercontent.com/110800205/191480929-f4d74219-0c97-4b53-84f4-92f25b4ce5e1.png)
