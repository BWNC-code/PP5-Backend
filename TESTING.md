# Travel Social API Testing Documentation

## Table of Contents

- [Travel Social API Testing Documentation](#travel-social-api-testing-documentation)
  - [Code Validation](#code-validation)
    - [PEP8 Compliance](#pep8-compliance)
  - [Automated Testing](#automated-testing)
    - [Overview](#overview)
    - [Test Cases](#test-cases)
      - [Profiles App](#profiles-app)
      - [Posts App](#posts-app)
      - [Comments App](#comments-app)
      - [Likes App](#likes-app)
      - [Followers App](#followers-app)
      - [Categories App](#categories-app)
    - [Automated Testing Results](#automated-testing-results)
  - [Manual Testing](#manual-testing)
    - [Profiles](#profiles)
    - [Posts](#posts)
    - [Comments](#comments)
    - [Likes](#likes)
    - [Followers](#followers)

[Table of contents generated with markdown-toc](http://ecotrust-canada.github.io/markdown-toc/)

## Code Validation

### PEP8 Compliance

The Travel Social API adheres to PEP8 standards, ensuring clean and readable code. Tools like pylint and black were used extensively during development for formatting, linting, and compliance checks. These tools helped maintain code quality and consistency, resulting in a codebase with no significant PEP8 violations or warnings.

## Automated Testing

### Overview

Automated tests play a crucial role in the development of the Travel Social API. A suite of tests has been implemented to cover critical functionalities across the various apps.

### Test Cases

#### Profiles App

- Test for successful profile creation and verification of profile data.
- Update functionality tests, ensuring profile data can be accurately modified.
- Data retrieval tests, checking that profile information is correctly returned by the API.

#### Posts App

- Creation tests to confirm that new posts can be successfully added to the API.
- Editing tests to ensure that post data can be updated and is correctly reflected.
- Deletion tests to verify that posts can be removed from the API without residual data.
- Listing functionality tests, ensuring that posts are accurately retrieved and listed, including checks for proper ordering and pagination.

#### Comments App

- Tests to verify that comments can be added to posts, ensuring correct association and data integrity.
- Editing tests for comments, ensuring updates are accurately reflected in the API.
- Deletion tests to confirm that comments can be removed, validating the removal process and data integrity.

#### Likes App

- Tests to validate the like functionality, including adding and removing likes.
- Checks to ensure that likes are correctly tallied and associated with the respective posts.
- Verification that user likes are properly reflected and managed in user-related queries.

#### Followers App

- Tests for the follower functionality, ensuring that users can follow and unfollow others.
- Validation of the follower count and follower list integrity.
- Tests to ensure proper functionality of the API in scenarios like mutual following and follower retrieval.

#### Categories App

- Tests to verify that a category can be created and retrieved

### Automated Testing Results

![Testing results](https://res.cloudinary.com/share-the-plate-cloud/image/upload/v1699825559/Screenshot_2023-11-12_214542_gyymlp.png)

## Manual Testing

### Profiles

- Verified that user profiles are created and updated correctly.
- Checked profile data retrieval for accuracy.

### Posts

- Manually tested post creation, editing, and deletion.
- Ensured accurate display and sorting of posts in various views.

### Comments

- Checked adding, editing, and removing comments on posts.
- Verified the correct association of comments with respective posts.

### Likes

- Tested liking and unliking posts, and the correct tally of likes.

### Followers

- Confirmed the functionality of following and unfollowing users.
- Tested the correct listing of followers and followed users.
