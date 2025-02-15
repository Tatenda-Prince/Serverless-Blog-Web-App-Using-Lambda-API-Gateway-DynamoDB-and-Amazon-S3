# Serverless Blog Platform with Lambda, API Gateway, DynamoDB, and S3

"Serverless Web App Blog"

# Technical Architecture

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/2e8be49796bd3cc67aade4b411c9456044d8d293/img/Screenshot%202025-02-04%20110011.png)

## Project Overview

This project is a serverless web blog application hosted on AWS, utilizing various cloud services to ensure scalability, security, and cost efficiency. The frontend is hosted on Amazon S3 as a static website, allowing users to access the blog interface. Authentication is managed through Amazon Cognito, which provides secure login and token-based authorization. 

Users interact with the blog by making API requests via Amazon API Gateway, which routes requests to AWS Lambda functions written in Python. The Lambda functions handle backend logic, such as retrieving, adding, updating, and deleting blog posts, and interact with Amazon DynamoDB, a NoSQL database used to store blog content efficiently. This architecture eliminates the need for server management, offers automatic scaling, and provides a secure and cost-effective solution for hosting a dynamic blogging platform.

## Project Objectives

1.Serverless Architecture – Build a fully serverless blog application using AWS services, eliminating the need for traditional server management.

2.Scalability & Performance – Ensure the system can automatically scale based on user demand using AWS Lambda and DynamoDB.

3.Cost Efficiency – Utilize pay-as-you-go AWS services to minimize costs while maintaining performance and reliability.

4.Secure Authentication – Implement Amazon Cognito for user authentication, ensuring secure access to the blog platform.

5.Seamless API Integration – Use Amazon API Gateway to efficiently route frontend requests to backend services.

6.Efficient Data Storage – Store and manage blog posts dynamically using Amazon DynamoDB, ensuring fast and reliable access.

7.Static Website Hosting – Host the frontend on Amazon S3, providing a highly available and cost-effective web hosting solution.

8.Improved User Experience – Deliver a responsive and interactive blog application with smooth API interactions.


## Prerequisites

1.AWS Account: Create an AWS Account.

2.AWS CLI Installed and Configured: Install & configure AWS CLI to programatically interact with AWS.

## Technologies

1.Amazon S3

2.AWS Lambda

3.Amazon Cognito

4.Amazon DynamoDB

5.Amazon API Gateway


## Step 1: Set Up the Frontend (Amazon S3)

1.1.Login to AWS Console:

Access the AWS Management Console and search for Amazon S3.

1.2.Create a bucket and give it name that is globally unique

Choose create bucket and leave everything as default

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/3bec13cda3896efd82bc4fd23e7ed6d510aac859/img/Screenshot%202025-02-03%20192716.png)



1.3.Enable Static Website Hosting in the bucket properties

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/3d34c5798c072d1e57911ce0943df8b6a388aa98/img/Screenshot%202025-02-03%20193016.png)


Set the `index.html` as the index document.

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/568272087c6e49a45fd69534a2f360c7a3187ebb/img/Screenshot%202025-02-03%20193046.png)


1.4.Upload Frontend Files:

We must create an index.html file for the blog frontend. This file will include a form to submit blog posts and display existing posts.

Upload the `index.html` and any other static assets (CSS, JS) to the S3 bucket.


![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/8ad49bffb3f3258f4ccf3528c44d5f29d807b738/img/Screenshot%202025-02-03%20193336.png)


1.5.Make the Bucket Public:

Update the bucket policy to allow public read access:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-blog-frontend/*"
    }
  ]
}
```


## Step 2: Set Up the Database (DynamoDB)

2.1..Lets Navigate to DynamoDB:

Go to the DynamoDB service in the AWS Management Console.

Click "Create table"


2.2.Configure the Table

We will give our table a name `BlogPosts`

Partition key: `PostID` Type "String"


![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/e2877cd8f74f353e2a7e6bd9c2d69783afbaae80/img/Screenshot%202025-02-03%20193520.png)


Click Create Table

2.3.As you can our table active now see example below-


![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/57adb9e3b85d3179f2250a3fb607785dc20f94a3/img/Screenshot%202025-02-03%20193606.png)


## Step 3: Set Up the Backend (AWS Lambda)

3.1.Navigate to Lambda:

Go to the Lambda service.

3.2.Create two Lambda functions:

CreatePost: To handle creating new blog posts.

GetPosts: To retrieve all blog posts.

Click "Create function".

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/210d28881a47451bf29cb70281fc7cae8be861d4/img/Screenshot%202025-02-03%20193741.png)


Add Permissions:

Attach the `AmazonDynamoDBFullAccess`  and `AWSLambdaBasicExecutionRole` policy to the Lambda functions' IAM roles.

choose the role that you have created 

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/82060548e2173e3df0ffeb361f97f000a6b6487d/img/Screenshot%202025-02-03%20193820.png)


3.3.Lets write the Lambda Functions 

Scroll down to the "Function code" section.

Replace the default code with the following Python code: 

## CreatePost Lambda Function:

```python

import json
import boto3
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BlogPosts')

def lambda_handler(event, context):
    # Parse the request body
    body = json.loads(event['body'])
    post_id = str(uuid4())
    title = body['title']
    content = body['content']

    # Insert into DynamoDB
    table.put_item(Item={
        'PostID': post_id,
        'Title': title,
        'Content': content
    })

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Post created successfully!'})
    }

```

## code explanation

This AWS Lambda function handles the creation of blog posts by storing them in a DynamoDB table named "BlogPosts". It first initializes a connection to DynamoDB using boto3 and targets the BlogPosts table. When triggered, the function extracts the request body (which is expected to be JSON), generating a unique PostID using uuid4(). It then retrieves the title and content fields from the request and stores them in DynamoDB as a new item. After successfully inserting the data, the function returns a 200 OK response with a success message in JSON format.



## GetPosts Lambda Function:

```python

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BlogPosts')

def lambda_handler(event, context):
    # Scan the table to get all posts
    response = table.scan()
    items = response['Items']

    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }

```


## code explanation

This AWS Lambda function retrieves all blog posts from a DynamoDB table named "BlogPosts". It first establishes a connection to DynamoDB using boto3 and selects the BlogPosts table. When the function is triggered, it performs a scan() operation to fetch all items stored in the table. The retrieved items are then extracted from the response and converted into a JSON-formatted string. Finally, the function returns a 200 OK response with the list of blog posts in the response body.

## Step 4: Set Up API Gateway

4.1.Create a New API:

Go to the API Gateway Console.

Create a new REST API click Build

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/f4efb9b2e937d8885f7b93b8e16a1c4ed4dc12c8/img/Screenshot%202025-02-03%20194433.png)


name your API 


![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/311040acc39ec249f515611aaf886f34a2c03923/img/Screenshot%202025-02-03%20194500.png)


4.2.Create Resources and Methods:

Create a resource /posts.

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/e56db15b31f4f653244b98074426de6c930afc77/img/Screenshot%202025-02-03%20194552.png)



Add a `POST` method for creating posts and connect it to the `CreatePost` Lambda function.

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/e47f5cce5a168e3ca0f2a907fdb19fa150f169c6/img/Screenshot%202025-02-03%20194710.png)

Add a `GET` method for retrieving posts and connect it to the `GetPosts` Lambda function.

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/a4362dc399d43d1e160bc65bbef14ed883c857c3/img/Screenshot%202025-02-03%20194804.png)


4.3.Enable CORS:

Enable CORS for the /posts resource to allow requests from your S3 frontend.

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/38d791c144c85be1aa1daba78541690b1e7d1e0a/img/Screenshot%202025-02-03%20194956.png)


4.4.Deploy the API:

Deploy the API to a stage (e.g., prod).


![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/bb0a4d7d319368e8c221fd084e2655bba3904574/img/Screenshot%202025-02-03%20195620.png)


Take Note the API endpoint URL.


## Step 5: Connect Frontend to Backend

5.1.Update Frontend Code:

In your index.html, use JavaScript to make API calls to the API Gateway endpoint.

```html

<!DOCTYPE html>
<html>
<head>
    <title>My Blog</title>
</head>
<body>
    <h1>My Blog</h1>
    <form id="blogForm">
        <input type="text" id="title" placeholder="Title" required>
        <textarea id="content" placeholder="Content" required></textarea>
        <button type="submit">Submit</button>
    </form>
    <div id="posts"></div>

    <script>
        const apiUrl = 'https://YOUR_API_GATEWAY_URL/prod/posts';

        // Function to fetch and display posts
        async function fetchPosts() {
            const response = await fetch(apiUrl);
            const posts = await response.json();
            const postsContainer = document.getElementById('posts');
            postsContainer.innerHTML = posts.map(post => `
                <div>
                    <h2>${post.Title}</h2>
                    <p>${post.Content}</p>
                </div>
            `).join('');
        }

        // Function to submit a new post
        document.getElementById('blogForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const title = document.getElementById('title').value;
            const content = document.getElementById('content').value;

            await fetch(apiUrl, {
                method: 'POST',
                body: JSON.stringify({ title, content }),
                headers: { 'Content-Type': 'application/json' }
            });

            fetchPosts(); // Refresh posts after submission
        });

        // Fetch posts on page load
        fetchPosts();
    </script>
</body>
</html>
```

5.2.Upload Updated Frontend Files:

Upload the updated index.html to your S3 bucket.


## Step 6: Lets Test the Application

6.1.We should  go back to our s3 bucket under under "Properties" scrolll down till you find website hosting and copy our S3 static website URL in a browser.

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/855257dd93836441b2d258c463df7badccd4473d/img/Screenshot%202025-02-03%20195659.png)


6.2.Submit a blog post using the form

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/708f204e13e44a16001af5bb20067205195ed7fc/img/Screenshot%202025-02-03%20200943.png)


6.3.Verify that the post is saved in DynamoDB and displayed on the frontend.

![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/bfacbc5207b3eab3188e3686b836c728272167f7/img/Screenshot%202025-02-03%20200924.png)


4.4.We can also view all our saved blog post in DynamoDB using our api gateway URL


![image_alt](https://github.com/Tatenda-Prince/Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3/blob/0bd6a2e00b97aedba1659a788cc34dce850a0086/img/Screenshot%202025-02-03%20201012.png)


## Future Enhancements

1.We will add authentication using AWS Cognito to allow only Authenticated users to post to our blog.

# Congratulations

We have successfully deployed a fully serverless web application using AWS services. We have learned how to host a static website on Amazon S3, configure Amazon API Gateway to handle frontend API requests, and develop a backend using AWS Lambda with Python for processing blog data.Additionally, we understood how to implement user authentication with Amazon Cognito, managing secure access with JWT tokens. Working with Amazon DynamoDB, you will explore NoSQL database operations, including storing and retrieving blog posts efficiently. This project will also enhance your knowledge of CORS policies, API security, and cost optimization in cloud computing.












