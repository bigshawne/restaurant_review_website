# restaurant_review_website
This is a restaurant review website developed by django framework.
1. User login/pout, register and profile management:

  i. Use the django-allauth application to implement the User login/out, register. Combine the email app built in django and allauth to implement the verification email sending and check if the email address is verified.
  
  ii. Expand the profile app built in Chicago that customize the user information, and update password.
  

2. Use the PostgreSQL as the database to store the users information.

3. There are eight main functions of this website

  i. Browse all resturants. (All users)
  
  ii. Check the detail of all resturants (Name, Address, Web, Menu, Rating, and Comments) (All users)
  
  iii. Create resturant (Only for logged in users)
  
  iv. Edit resturants (Only for logged in owner)
  
  v. Add dishes (Price, Description, Photo) (Only for logged in user)
  
  vi. Edit dishes (Only for logged in owner)
  
  vii. Check the details of all dishes (All users)
  
  viii. Rate and comment the resturant (Logged in users)
  
  iv. Search the resturant with key words. (All users)
  
 * The real-time search function is powered by Ajax
 * The front-end is developed under HTML5 standard and decorated by Bootstrap4
