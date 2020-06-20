# Project Title

 * Social media Network
 
---
### Table of Contents

In this section you will know More bout this interesting project :smiley:

- [overview](#overview)
- [An_open_source_Social_Network](#An_open_source_Social_Network)
- [Current_Features](#Current_Features)
- [Ai_model_on_heroku](#Ai_model_on_heroku)
- [Homepage](#Home_page)
- [user_profile](#user_profile)
- [error_when_try_to_publish_empty_post](#error_when_try_to_publish_empty_post)
- [recommendation_using_Ai ](#recommendation_using_Ai )


---

### overview

 The idea of the project is summarized in how to make classify posts and determine which is spam or not and if spam, this post must be
 discarded else insert post in database Ai model run on database and use it to classify post, Make frontend form where each user can 
 post in it and pass this post to ai model to classify it , and determine number of like in this post 
 
 * Main goal of this project
 
      To avoid posting fake and not important posts
 
 
---

#### An_open_source_Social_Network

Used Tech Stack

1. Django
2. Mysql database
3. Web Socket (Django Channel)
4. Workbensh
---

### Current_Features:

1. Login/Register

2. Create post and comment on the particular post

3. Receive love when someone comment on your post

4. recommendation when user publish post 

5. see when someone comment on post

5. Natural language processing on posts to analyze it using arabic posts

---

## sign in form 

User must has an account, supplying the following data:

- Email

- Password

Searching in database if email & password exists, the second form must be opened If not, display a message to allow a new user to sign up  New user may click sign up, the sign up form must be opened

<p align = "center"> 
<img src="./img/signin.PNG">
</p>

---

## sign up form

New user must has an account with the following data:

* Email

* Password

* User name

* Picture to user (if exist)

* Date of birth

* Detailed location information

<p align = "center">
 
<img src="./img/signup.PNG" >

</p>

---


## user_profile

  each user have information that appear in homepage and easily can create this information 
  this information appear in database and easily can change it
  
  <p align = "center">
<img src="./img/create_profile.PNG">
</p>

---

 user can update information which belongs to it and if he want to upload image this link to image is saved in database 

<p align = "center">
<img src="./img/edit_profile.PNG">
</p>


---

## Homepage

* we use this design in frontend using bootstrap to make social media responsive 

<p align = "center">
<img src="./img/homepage.PNG">
</p>

---

### comment 

users can comment to any post and appear to it , Users see posts from homepage

<p align = "center">
<img src="./img/comment.PNG" width ="300" height = "400">
</p>

--- 
## error_when_try_to_publish_empty_post

## recommendation_using_Ai 

<img src="screenshots/two.png" height="400">


---

### Ai_model_on_heroku

* Ai model we deploy it on heroku to try model 

<p align = "center">
 
<img src="./img/finaln.PNG" height="400" width = "700">
 
</p>

[link heroku](https://posts-classification.herokuapp.com/)



Show your support by 🌟 the project!!
