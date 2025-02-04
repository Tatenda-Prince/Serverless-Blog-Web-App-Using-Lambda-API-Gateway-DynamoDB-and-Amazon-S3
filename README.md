# Serverless-Blog-Web-App-Using-Lambda-API-Gateway-DynamoDB-and-Amazon-S3

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

![image_alt]()



1.3.Enable Static Website Hosting in the bucket properties

![image_alt]()


Set the `index.html` as the index document.

![image_alt]()




