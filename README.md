# EZ Eating

EZ Eating is a full-stack website for a restaurant business, where users have access to the following features:
- Account creation and management
- Read/post reviews
- Create,view,edit and delete their reservations
- View menu

Therefore, this site is intended for users who wish to avail of these features to make their experience of EZ Eating more
streamlined and enjoyable.

The live version of the project can be found [here](https://ez-eating-52f91ace33f6.herokuapp.com/).

## Existing Features

- Reservation Booking System
    - User enters the required information and if it is valid a reservation will be created in the database.
    - If the user enters a past date or if the time and date has already been booked then the data is not valid and a ValidationError will occur.

<br/>

![Reservation Past Date](/static/images/past_date.png)

<br/>

![Reservation Double Booking](/static/images/double_booking.png)

<br/>

- View Reservations 
    - Users can view all the reservations that have been made with the current account they are logged into.

<br/>

![Reservation View](/static/images/reservation_view.png)

<br/>

- Amend/Cancel Reservations
    - Users can cancel/amend any reservations associated with their account.

<br/>

![Reservation Cancel/Amend](/static/images/edit_reservation.png)

- Register/Login/Logout of Account
    - Users can register for an account to access the features of reservation booking and leaving reviews
    - Users have the ability to easily login and logout of their account

<br/> 

![Account Register](/static/images/register.png)

<br/>

![Account Login](/static/images/login.png)

<br/>

![Account Logout](/static/images/logout.png)

<br/>

- Reviews
    - Users with an account can write reviews which will be displayed on the home page.

<br/>

![Review](/static/images/review.png)

<br/>

![Review home](/static/images/review_home.png)

- Current User Display
    - Users can see which account is currently logged in.

<br/>

![Current Account](/static/images/current_account.png)

<br/>

- View Menu
    - Users can click on Menu tab to show the restaurant's current menu

![Menu](/static/images/menu_tab.png)

## Future Features

- Allow users to book multiple tables if occupancy is over the limit of 6, which it is currently set at.
- Addition of multiple menus accessible from the menu tab for breakfast,lunch and dinner instead of 1 which it currently has.
- Upgrade the aesthetic of the home page and add a gallery page to make the site more aesthetically pleasing.

## Testing
- Automated Testing:
    - Three test files were utilised in the testing of this project:
        - test_forms.py, test_views.py, test_models.py
        - Below is the total coverage for Project, not 100% for reasons given in 'Unfixed Bugs' section
    <br/>
    ![Coverage](/static/images/coverage.png)
    

## Validator Testing
- Html - No errors returned when passing through W3C validator
- CSS - No errors returned when passing through (Jigsaw) validator
- Used Pylint tool. No significant errors found.

## Unfixed Bugs
- As stated above in the Automated Testing section, a bug was encountered during testing. While running the test
for adding a reservation to the database and then redirecting to the /booking page an error occured. Instead of a 302 redirect response a 200 response was given. This bug has still not been rectified and is the reason for only 96% testing coverage.

## Deployment 
- Deployment steps
    - Fork/clone this repository
    - Create a new Heroku app
    - Add DATABASE_URL/SECRET_KEY config vars in settings tab on Heroku, also add key of PORT and value of 8000
    - Link the Heroku app to the repository
    - Click Deploy

## Credits 

### Content
- Code Institute walkthrough projects ('Hello Django','I Think Therefore I Blog') for instruction on how to use Django, create database models, implement views/forms, how to perform automated testing and finally how to use django-allauth to simplify the implementation of accounts in the project
- How to implement widgets in forms.py taken from (https://www.appsloveworld.com/django/100/187/how-to-return-a-list-of-available-time-slots-via-a-forms-validationerror?expand_article=1)
- How to prevent past dates being accepted for ReservationForm taken from [StackOverflow](https://stackoverflow.com/questions/70558856/django-how-to-prevent-to-accept-future-date)

### Media
- Menu image taken for free from (https://www.canva.com/p/templates/EAEfNjcKK9Q-simple-food-menu/)
- Main image used on index.html taken for free from [Pixabay](https://pixabay.com/photos/bar-alcohol-cocktail-glass-party-264227/)
- Favicon taken for free from [favicon.io](https://favicon.io/emoji-favicons/fork-and-knife-with-plate)