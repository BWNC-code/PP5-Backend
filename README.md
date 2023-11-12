# TRAVEL SOCIAL (BACKEND)

## Introduction

For more information about this projects frontend, please visit [this link](https://github.com/BWNC-code/Travel-Social-PP5-Frontend)

Travel Social's backend API is a Django REST Framework-based application that serves as the backbone for a React-based frontend. It's designed to handle data management and server-side logic for a social media platform centered around travel.

The Travel Social API powers a dynamic platform where users can share, discover, and engage with travel-related content. It facilitates a range of functionalities for creating, viewing, editing, and deleting posts related to travel experiences, destinations, reviews, and photo stories. Users can craft their own travel posts, enriching them with vivid descriptions, captivating images, and relevant category tags such as adventure, budget travel, or cultural experiences.

## Table of Contents

- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Architecture](#architecture)
  - [Database](#database)
  - [API and Server](#api-and-server)
  - [Cloud Services and Storage](#cloud-services-and-storage)
  - [CORS Configuration](#cors-configuration)
  - [Security and Performance](#security-and-performance)
- [API Endpoints](#api-endpoints)
  - [Authentication and User Management](#authentication-and-user-management)
  - [Profiles](#profiles)
  - [Posts](#posts)
  - [Likes](#likes)
  - [Followers](#followers)
  - [Comments](#comments)
  - [Categories](#categories)
- [Production Configuration: JSON-Only Responses](#production-configuration-json-only-responses)
  - [Reasons for JSON-Only Responses](#reasons-for-json-only-responses)
  - [Implementation in Django Settings](#implementation-in-django-settings)
- [Models and Data Structure](#models-and-data-structure)
  - [Database Design](#database-design)
  - [Profile](#profile)
  - [Post](#post)
  - [Like](#like)
  - [Follower](#follower)
  - [Comment](#comment)
  - [Category](#category)
- [Features left to implement](#features-left-to-implement)
- [Technology Used](#technology-used)
- [Testing](#testing)
  - [Python Linting](#python-linting)
  - [Feature Testing](#feature-testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
  - [Forking the Project Repository](#forking-the-project-repository)
  - [Cloning the Project Repository](#cloning-the-project-repository)
  - [Remote Deployment](#remote-deployment)
- [Credits and Acknowledgements](#credits-and-acknowledgements)

[Table of contents generated with markdown-toc](http://ecotrust-canada.github.io/markdown-toc/)

## Architecture

Travel Social's backend is built using Django and the Django REST Framework, following a traditional MVC (Model-View-Controller) architecture pattern. The API serves as the server-side component of a web application, interfacing with a React-based frontend.

### Database

- PostgreSQL via ElephantSQL: The application uses PostgreSQL as its primary database, with ElephantSQL as the database hosting service.

### API and Server

- RESTful API: Adheres to REST principles, providing a set of stateless, cacheable operations.
- Authentication: Implements JWT (JSON Web Token) authentication for secure access, using dj-rest-auth and djangorestframework-simplejwt.
- Session and Token Authentication: Supports both session and token-based authentication, catering to different client requirements.

### Cloud Services and Storage

- Cloudinary: Used for image storage and management, integrated via django-cloudinary-storage. This is essential for handling media files like user profile pictures and post images.
- Heroku Deployment: The API is deployed on Heroku, with direct deployment from the GitHub repository. This setup suggests a streamlined deployment pipeline, possibly with CI/CD practices.

### CORS Configuration

- CORS Headers: Managed by django-cors-headers to enable CORS (Cross-Origin Resource Sharing), crucial for API communication with the React frontend.

### Security and Performance

- Security Middleware: Incorporates Django's security best practices, including middleware for session management and CSRF protection.
- Performance Considerations: While specific performance strategies (like caching) are not detailed in the settings file, the use of pagination in the REST Framework suggests attention to efficient data handling.

## API Endpoints

A detailed description of the RESTful API endpoints, including the request and response formats for profiles, posts, likes, comments, and followers.

### Authentication and User Management

- Root Route (/): Root endpoint, only used for API health check, contains a greeting
- Admin (/admin/): Django's admin interface.
- API Auth (/api-auth/): Standard REST framework browsable API authentication.
- Logout (/dj-rest-auth/logout/): Endpoint for user logout.
- Authentication Endpoints (/dj-rest-auth/): Includes endpoints for login, password reset, etc.
- User Registration (/dj-rest-auth/registration/): Endpoints for user registration.

### Profiles

- List Profiles (/profiles/): GET to retrieve all profiles, POST to create a new profile.
- Profile Detail (/profiles/<int:pk>/): GET, PUT, DELETE for specific profile details (identified by primary key).

### Posts

- List Posts (/posts/): GET to retrieve all posts, POST to create a new post.
- Post Detail (/posts/<int:pk>/): GET, PUT, DELETE for specific post details.

### Likes

- List Likes (/likes/): GET to retrieve all likes, POST to create a new like.
- Like Detail (/likes/<int:pk>/): GET, PUT, DELETE for specific like details.

### Followers

- List Followers (/followers/): GET to retrieve all followers, POST to create a new follower relationship.
- Follower Detail (/followers/<int:pk>): GET, PUT, DELETE for specific follower details.

### Comments

- List Comments (/comments/): GET to retrieve all comments, POST to create a new comment.
- Comment Detail (/comments/<int:pk>/): GET, PUT, DELETE for specific comment details.

### Categories

- List Categories (/categories/): GET to retrieve all categories, POST to create a new category.
- Category Detail (/categories/<int:pk>/): GET, PUT, DELETE for specific category details.

## Production Configuration: JSON-Only Responses

In the production environment, the "Travel Social" API is configured to respond with JSON data exclusively. This decision aligns with the RESTful principles and ensures consistency, efficiency, and compatibility across different clients, particularly our React-based frontend.

### Reasons for JSON-Only Responses

--Uniformity and Predictability--: JSON, being the standard data interchange format in modern web applications, provides a uniform structure for responses. This consistency is crucial for the frontend to reliably parse and use the data.

--Efficiency--: JSON is lightweight and easy to parse, which is especially beneficial for web applications that need to transmit data quickly over the internet. By sending only JSON data, we reduce the bandwidth usage and improve the performance of our API.

--Frontend Compatibility--: Given that our frontend is built with React, which naturally handles JSON, this approach ensures maximum compatibility. React components can seamlessly integrate and manipulate JSON data for rendering and state management.

--Simplicity in Client-Side Processing--: JSON data can be easily consumed by various client-side technologies. By standardizing on JSON, we simplify the client-side processing, as there is no need to handle different data formats.

### Implementation in Django Settings

This behavior is implemented in the Django settings of the backend. In the production environment, the Django REST Framework's DEFAULT_RENDERER_CLASSES is set to use rest_framework.renderers.JSONRenderer. This renderer ensures that all responses from our API, regardless of the endpoint, are in JSON format.

```python
# Django settings.py snippet for production configuration

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
    "rest_framework.renderers.JSONRenderer",
]
```

This configuration is activated only in a production setting, allowing for more flexibility during development, such as the use of the browsable API interface provided by Django REST Framework for easier debugging and testing.

## Models and Data Structure

### Database Design

The relationships between all of these models is summarised in the followed entity relationship diagram:

![Database Model using DBML](https://res.cloudinary.com/share-the-plate-cloud/image/upload/v1699707987/travel_social_db_qlftrn.png "Database model using DBML")

### Profile

- Model Name: Profile
- Purpose: Represents user profiles in the system.
- Fields:
  - owner: A one-to-one link to the Django User model, indicating the user to whom the profile belongs.
  - created_at: A datetime field that records when the profile was created, automatically set when a profile is first created.
  - updated_at: A datetime field that tracks the last update time of the profile, automatically updated on profile modification.
  - name: A character field for the user's name. It is optional.
  - content: A text field for additional profile information or bio. It is optional.
  - image: An image field for the profile picture, with a default image set.

### Post

- Model Name: Post
- Purpose: Manages the creation and storage of posts.
- Fields:
  - owner: A foreign key linking to the User model, representing the user who created the post.
  - category: A foreign key to the Category model, allowing categorization of posts. It is optional.
  - created_at and updated_at: Datetime fields similar to the Profile model.
  - title: A character field to store the post's title.
  - content: A text field for the post's main content.
  - image: An optional image field for the post.

### Like

- Model Name: Like
- Purpose: Tracks likes on posts.
- Fields:
  - owner: A foreign key to the User model, representing the user who liked a post.
  - post: A foreign key to the Post model, indicating the post that received the like.
  - created_at: A datetime field marking when the like was made.

### Follower

- Model Name: Follower
- Purpose: Manages follower relationships between users.
- Fields:
  - owner: A foreign key to the User model, representing the follower.
  - followed: Another foreign key to the User model, representing the followed user.
  - created_at: A datetime field indicating when the follow relationship was established.

### Comment

- Model Name: Comment
- Purpose: Handles comments on posts.
- Fields:
  - owner: A foreign key to the User model, denoting the user who made the comment.
  - post: A foreign key to the Post model, indicating the post on which the comment is made.
  - created_at and updated_at: Datetime fields tracking the creation and last update of the comment.
  - content: A text field for the comment's text.

### Category

- Model Name: Category
- Purpose: Categorizes posts.
- Fields:
  - name: A character field for the category's name, marked as unique.
  - description: A text field for a more detailed description of the category, optional.

## Features left to implement

Future enhancements could include more robust filtering options, integration with external travel APIs, and enhanced analytics features for user engagement tracking.

## Technology Used

- Django and Django REST Framework for building the API.
- Cloudinary for image storage and management.
- PostgreSQL as the databasePython and Django REST Framework
- The backend is built using Python and Django REST Framework, providing a powerful, scalable, and flexible foundation for the API.

## Testing

### Python Linting

All code passed through PEP8 linter (pylint) with no errors

### Feature Testing

All test cases can be found in [TESTING.md](./TESTING.md)

## Bugs

No known bugs remaining

## Deployment

The project was deployed to Heroku. To deploy, please follow the process below:

### Forking the Project Repository

You can create your own independent version of this project by forking the repository. This allows you to experiment and make changes without impacting the original codebase. Here's how to fork the repository:

1. Sign in to your GitHub account and navigate to the repository.
2. Look for the 'Fork' button at the top right corner of the page and click on it. This action creates a personal copy of the repository in your GitHub account.

### Cloning the Project Repository

Cloning the repository creates a local copy on your machine, maintaining a connection with the original GitHub repository. This enables you to sync your local version with any updates made in the original project. To clone the repository, follow these steps:

1. In your forked repository, click the 'Code' button.
2. From the dropdown, choose the method of cloning you prefer (HTTPS, SSH, or GitHub CLI), and copy the provided URL.
3. Open your terminal, navigate to the directory where you want to clone the repository, and run git clone followed by the copied URL.
4. By forking and cloning the repository, you can freely experiment with the code and even contribute to the original project through pull requests.

### Remote Deployment

To deploy the application on Heroku and ensure that all features work as expected, follow these steps:

- Create a new Heroku app.

- Set up the necessary Config Vars in the Settings tab.

- Connect your GitHub account and select the repository to be deployed.

- Choose either manual deployment or enable automatic deployment.

## Credits and Acknowledgements

Thanks to my mentors, Jubril Akolade and Chris Quinn for their advice and guidance. Thanks as well to the Code Institute team and tutors for their support.
