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