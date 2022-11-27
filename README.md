# THE PINK SILK

For my Project Portifolio #5 on Code Institute's Diploma in Software Developement course I have created an E-commerce store for a SPA called The Pink Silk. 

On the website, all users have access to view and purchase the available spa packages. Registered users can also have access at their profile page, where is possible to edit their personal information and view previous orders. Store management with a superuser access can add new packages for sale, as well as edit and delete existing packages.


You can check the store page clicking [HERE](https://the-pink-silk.herokuapp.com/)


![HOME-PHOTO](media/images/all-devices-black.png)



# User Experience UX


## Site Goals

### Site Owner's Goals

* Selling spa packages to all users.
* Providing detailed information about what is being offered on each package.
* Offering a simple and secure checkout.
* Letting users leave their personal opnion on treatments received at the spa.

### Site User's Goals

* Finding information about the services offered.
* Benefitting from other user's testimonials to help on making decisions.
* Learning more about the company and it's policies.


## Agile Planning

The project was developed using agile methodologies, by delivering small features divided in 4 sprints - To do Admin, To do User, In progress, Done.

Every card was labeled under User Story, divided in User and Admin. There is also a label for Bug, used when some issue was found.

The board was created  using Github projects and can be located [HERE](https://github.com/users/rlorimier/projects/1/views/1) to have access to more information on the project cards.

![AGILE-BOARD](media/images/agile-board.png)


## User Stories

### As User:

* I want to see all packages available so I can decide what to buy.
* I want to see reviews so I can decide if this is the right place for me.
* I want to contact the Spa so I can have my queries answered.
* I want to be able to register so I can have my own account.
* I want to know more about the Spa and it's cancelation policy so I can make sure is a reliable place.
* I want to have a shopping bag so I can see what I am purchasing.
* I want to be able to update or delete items from my shopping bag so I can finish my purchase correctly.

### As Registered User:

* I want to write a testimonial so other users and the admin can read my opnion.
* I want to be able to login/out with no issues so I can have access to my profile.
* I want to have a personal profile so I can store my information and see previous orders made.

### As Admin:

* I want to add new packages for sale so I can increase the options available.
* I want to be able to edit existing packages so I can keep it updated. 
* I want to be able to delete existing packages so I can remove it if unavailable.


## The Scope

* Responsive design - site is fully functions on all screen sizes
* Navigation menu on all pages - Member Area changes depending on user status
* User authentication (register, login, logout)
* Hamburger menu for screens smaller than 994px
* CRUD functionality for admin users on packages
* List of packages and easy access to details page
* User profile, containing personal information and order history
* 404 error page


## Features

### User features


#### USER STORY

*As an user I want to see all packages available so I can decide what to buy*

*As an user I want to be able to register so I can have my own account*

*As an user I want to be able to login/out with no issues so I can have access to my profile*

*As an user I want to have a personal profile so I can store my information and see previous orders made*


* NAVBAR
  * Home - on the navigation bar at the top right, brings the user back to the home page.
  * Spa Packages - on the navigation bar at the top right, brings the user to a page containing a brief information about the available packages.
  * Testimonials - on the navigation bar at the top right, brings the user to a page where a list with all testimonials can be seen.
  * Contact - on the navigation bar at the top right, brings the user to a page containg a contact form.
  * Member Area - on the navigation bar at the top right:
    * All users have options to Register or Sign In
    * Registerd users have options to Sign Out, leave a New Testimonial or visit My Profile
    * Superusers have the same options as Registered users plus an option to Add New Package
  * Shopping Bag - on the navigation bar at the top right, brings the user to the shopping bag page.

  ![NAVBAR](media/images/navbar-home.png)


#### USER STORY

*As an user I want to contact the Spa so I can have my queries answered*

* CONTACT FORM
  * All users can file the contact form.

  ![CONTACT-FORM](media/images/contact-form.png)

* FOOTER
  * Get In Touch - column that provides the user the email and phone number of the Spa and also shows the openning times.
  * Subscribe - column where the user can subscribe for the Spa newsletter and also find a link to the Privacy Policy.
  * Find Us - column that shows the address and a map to the Spa location and also links to Social Media.
  
  ![FOOTER](media/images/footer-home.png)



#### USER STORY

*As an user I want to know more about the Spa and it's cancelation policy so I can make sure is a reliable place*

* DISCOVER
  * By clicking on the Discover button at the Home page, the user is redirected to a page containg more information about the Spa, such as Cancellation Policy, Privacy and Terms and Conditions.

  ![DISCOVER](media/images/about-us.png)

  ![ABOUT-US](media/images/about-page.png)


#### USER STORY

*As an user I want to have a shopping bag so I can see what I am purchasing*

*As an user I want to be able to update or delete items from my shopping bag so I can finish my purchase correctly*


* SHOPPING BAG
  * Where the user can see the packages seleted for purchase.
  * Is possible to adjust the quantity by typing a number in the box or using the arrows and then clicking on Update.
  * To remove thepackage from the bag, just click on the Remove buttom.
  * For purchase, click on Secure Checkout.
  * To add more items, click on Back to Packages.

  ![SHOPPING-BAG](media/images/shopping-bag.png)


#### USER STORY

*As an user I want to write a testimonial so other users and the admin can read my opnion*

*As an user I want to see reviews so I can decide if this is the right place for me*

* TESTIMONIALS
  * All users can read and leave comments on the testimonials.
  * Registered users can write new testimonials.

  ![TESTIMONIALS](media/images/testimonials-page.png)


#### USER STORY

*As an admin I want to add new packages for sale so I can increase the options available*

*As an admin I want to be able to edit existing packages so I can keep it updated*

*As an admin I want to be able to delete existing packages so I can remove it if unavailable*

* ADD NEW PACKAGE
  * Admin users can have access to create new packages and update/delete existing ones.

  ![ADD-PACKAGE](media/images/add-package.png)

  ![EDIT-PACKAGE](media/images/edit-package.png)



### Social Media



* FACEBOOK PAGE
  * All users can have access to the Facebook Page

  ![FACEBOOK](media/images/facebook-page.png)


### Favicon

A favicon was added the website to enable users to easily locate the website in the browser when multiple tabs are open.

![FAVICON](media/images/favicon-icon.png)


### Code features

* Created in Django using Gitpod.
* Deployed in Heroku for online interaction.
* Used AWS to store media files.


## Wireframes

* Home

![WF-HOME](media/images/wf-home.png)

* Discover

![WF-DISCOVER](media/images/wf-about.png)

* Spa Packages - All

![WF-PACKAGESALL](media/images/wf-packages-all.png)

* Spa Packages - Detail

![WF-PACKAGESDETAIL](media/images/wf-packages-detail.png)

* Spa Packages - Add New

![WF-PACKAGESADD](media/images/wf-packages-add.png)

* Testimonial - All

![WF-TESTIMONIALALL](media/images/wf-testimonial-all.png)

* Testimonial - Add New

![WF-TESTIMONIALNEW](media/images/wf-testimonial-new.png)

* Contact Us

![WF-CONTACT](media/images/wf-contact.png)

* Bag - Empty

![WF-BAGEMPTY](media/images/wf-bag-empty.png)

* Bag - Full

![WF-BAGFULL](media/images/wf-bag-full.png)

* Checkout

![WF-CHECKOUT](media/images/wf-checkout.png)

* Checkout Successful

![WF-CHECKOUTSUCCESS](media/images/wf-checkout-success.png)

* My Profile

![WF-PROFIILE](media/images/wf-profile.png)

* Navbar - Admin

![WF-NAVBARADMIN](media/images/wf-navbar-admin.png)

* Navbar - Registered User

![WF-NAVBARREG](media/images/wf-navbar-reguser.png)

* Navbar - All Users

![WF-NAVBARALL](media/images/wf-navbar-alluser.png)



## Technologies used


### Languages

* [Python3](https://www.python.org/)
* HTML5
* CSS
* [JavaScript](https://www.javascript.com/)


### Frameworks, Libraries and other programs

* [Django](https://www.djangoproject.com/) framework (from Python)
* Django [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) and [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/#) libraries
* [Gitpod](https://www.gitpod.io/) as IDE
* [GitHub](https://github.com/) to storage files
* [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/) for CSS package
* [Heroku](https://www.heroku.com) for deployment
* [ElephantSQL](https://www.elephantsql.com/) for database
* [Favicon](https://favicon.io/) for favicon
* [Pexels](https://www.pexels.com/) for images
* [AWS](https://aws.amazon.com/) for media storage
* [Mailchimp](https://mailchimp.com/) for email newslatter subscription


### Resources


* [Code Institute](https://codeinstitute.net/ie/) - course materials, Slack community and tutor/mentor support
* [Boostrap docs](https://getbootstrap.com/) - for material support
* [Django central](https://djangocentral.com/) - for inspiration and material support
* [Codemy.com](https://www.youtube.com/c/Codemycom) - youtube channel for material support
* [W3 Schools](https://www.w3schools.com/) - for material support












## Testing


### Manual Testing

* Manual tests done as admin user, regular user and visitant. In all scenarios the blog funcionalities worked without showing any issues.
* I also send the live link to friends and family members for testing and feedback.

Manual testing result:

![Manual-Testing](media/images/manual-testing.png)


### Code Testing

* Python - [PIP8](https://pep8ci.herokuapp.com/)

All .py files were individualy tested, with the exception of settings.py, as some of the lines are longer than 79 characters but they are required for functionality of the website.

* HTML - [W3C](https://validator.w3.org/nu/)

![HTML-testing](media/images/html-testing.png)

* CSS - [Jigsaw](https://jigsaw.w3.org/css-validator/)

![CSS-testing](media/images/css-testing.png)

* JavaScript - [JSHint](https://jshint.com/)

![JSHint-testing](media/images/jshint-testing.png)



### Accessibility Testing

* Tested using [Accessibility Test](https://accessibilitytest.org/). <br>You can check the full test result clicking [HERE](https://accessibilitytest.org/results/p8j650eYCBWt).
![Accessibility-test](media/images/accessibility-test.png)



### Browser Testing

The site was tested and worked without any issues, using:
* Internet Explorer
* Google Chrome
* Microsoft Edge
* Firefox
* Samsung Internet




## Bugs/Issues

* Webhooks

    All the code seems correct. It was tested with the help of the Tutors and Mentor, however we could not find a solution for this error on time for the submission. 

![WEBHOOK-ERROR](media/images/weebhook-error.png)




## Creating a Repository and Deploying

* To create a new repository:

Logged in my GitHub page and accessed Code Institute GitHub page. 

Selected python-essencials-template and clicked in Use This Template. 

Created a new repository from the one mentioned above and choose the option 'Gitpod'. Once the repository is open on Gitpod it is just start to code. I chose the option to save automatically. 

After every significant amount of coding is time for local commits: On Gitpot, go to Source Control, type in a message and click Commit. After a work day, the last local commit is done and then click in Push to commit all local commits to GitHub repository. 


* To Deploy:

The project was deployed using Heroku. The process is as follows:

Once you have signed up to Heroku, on the top right of the dashboard there is a button labelled 'New'. This will open a dropdown; please select 'Create new app'. On the next page you can choose your region and a name for the project. Then click 'Create app'.

On the next page there is a menu along the top. Navigate to 'Settings', where you will find the config vars. Scroll down to the section named 'Config vars' and click on the button labelled 'Reveal config vars'. All keys, secret keys and database url must be included in this section in order to the project work.

If you scroll back to the top of the page you will find the 'Deploy' tab, which has multiple options for deployment. As I am using Github for this project, I selected it and a bar came up to search for the repo I wish to connect to.

Once you have connected, you have the option to deploy automatically (the app will update every time you push) or manually (update only when you choose). I chose automatic but you can do what suits you.

After the first push/update, your app will be ready to go!




## Credits


### Code

* Code based on and developed from Code Institute's walkthrough Boutique Ado.


### Content

* Background image from [Pexels](https://www.pexels.com/).
