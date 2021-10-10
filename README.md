# Smart Sentiments PSA Codesprint 

### Link to Dashboard : https://hoholyin.github.io/psa-codesprint/

### Link to Github Repository: https://github.com/hoholyin/psa-codesprint/tree/master/BE

### Link to Questionnaire: https://forms.gle/tuU6rPN2LiZb7jr49 (Also accessible in Dashboard)

# Model

### Technical Specifications
The neural network is created using PyTorch.

### Network Architecture
The network consists of one input layer with 13 dimensions, a hidden layer with 128 dimensions, a dropout layer, and an output layer with 5 dimensions for classification.

The loss function is Cross Entropy Loss

The learning rate is 0.01, the batch size is 4 and the number of epochs is 30.

# Front-End

### Technical Specification
The front end web application is built on Angular. 

It makes REST Api calls to the server to retrieve Employees' Information and Score and display them onto a visual dashboard.

# Back-End

### Technical Specification
The server is developed in Python Flask, hosted on repl with connection to a MongoDB database.

It allows for the Angular application to make `GET` requests to get Employees' Information and ratings and `POST` to save Employees' questionnaire results.

### Contributors
- Brandon Chong (https://github.com/brandoncjh)
- Glenn Tan (https://github.com/GlennTJR96)
- Ho Hol Yin (https://github.com/hoholyin)
