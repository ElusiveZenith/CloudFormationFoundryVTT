# Intro
Multiplayer FoundryVTT hosted with AWS ECS Fargate, and utilizing AWS Lambda for managing the server. 

## Used Docker Images
[felddy/foundryvtt-docker](https://github.com/felddy/foundryvtt-docker)
[atmoz/sftp](https://github.com/atmoz/sftp)

This is not at the point where it is an easy setup. Technical knowledge will be required to set it up and maintain it. While this utilizes AWS Fargate to minimize costs, you are altimetry responsible for managing cost of your AWS resources and properly deprovisioning AWS resources when no longer in use. It is also your responsibility to ensure data and endpoint security.

# Requirements
- Docker Knowledge
- AWS Knowledge
  - Cloud Formation
  - IAM
  - API Gateway
  - Route 53
- AWS Account
- Python 3.10+
- Domain for hosting

# Setup
1. Build the Doker Image and upload to a container registry such as AWS ECR
2. Create a bucket called [LowercaseName]-efs-sync-bucket-[AWS::AccountId] // LowercaseName is a parameter for the stack.
3. Copy Lambda files into bucket.
4. Deploy Stack.

# Connecting
## FoundryVTT
Connect from your browser by going to your domain, prepended with port 30000. Example: my-domain.com:30000
- Will take a few minutes after starting the server to start and for the DNS to be updated
- Server will automatically shut down after a short while of no connections to port 30000

## SFTP
A SFTP server is run alongside FoundryVTT for easy access to files. With your FTP application of choice, connect to same domain using the user `admin`. 
The password is the same admin password that you set as the FoundryAdminPassword in the stack formation

# Some Screws Not Included
Besides building and hosting the container registry, you will need to develop a way for your players to access the endpoint to launch the server. There is a IAM User created which has that permission to invoke the API, but it is pest to not give users direct AWS access. Personally, I created a Discord bot that exposed slash commands which used the IAM User to make the API calls.

# Future Improvements
- Save a backup of the world to S3 on server shut down.
- API endpoint to get the current number of players.
- Build lambda jobs into release with GHA
- Host Docker Image and update when felddy/foundryvtt updates

# Disclaimer and Indemnification
By using the code, templates, or any other content provided in this repo ("Repo"), you ("User") agree to indemnify and hold harmless the repo owner and any contributors from any claims, damages, or expenses arising from the User's use or misuse of this Repo.

