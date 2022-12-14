# CS50 Final Project Andres Eduardo Genes (Nasassistant)

## Distinctiveness and Complexity


1.	### Difference with previous projects
My project is very different from previous projects (it is not a social network, nor a page similar to Wikipedia, nor is it an ecommerce), it is much better designed and much more complex:

-The design is very meticulously worked, it has different variants of HTML, and CSS to achieve an innovative design, with visual impact and next-generation functionalities.
Each page has been very worked. The break points were designed with CSS and are at 1366px, 820px (Tablet), 480px (Mobile), 414px, 393px, 375px and 360px; making it very versatile for a large part of devices and screen sizes

2.	### More complex than previous projects
It has all the complexity of the previous projects, but in this one we will also add that it works with API Rest, with the great complexity that this has, and not only that, but it also works by connecting to the NASA page, bringing the data from over there. The NASA website is very extensive, with a lot of data and you have to have a lot of interpretation criteria to use the data it provides us.
It was thought as a dynamic page, by bringing the data from the NASA page, our web page will never be the same, every day it will have new things to offer.
As for the code, I have worked hard with Python, but to this I have added a lot of Javascript work, with different complex functions and handling of the DOM.

3.	### It features Django and has three models.

4.	### I have worked with Javascript in the Front-end.
I have modified the Dom by means of Javascript in almost all the pages, the work is extensive and meticulous, for example, in the main menu, when changing the size of the device, this brought is done with Javascript; Both the “Picture of the Day” page and the web page showing the Rover Curiosity expedition to Mars use Javascript to extract NASA data, process the data, and modify the front-end of my page to display the data.

5.	 ### It is compatible with Desktop, Tablet and Mobile Screens.

6.	 ### Complete documentation of what I did and why I did it.

Documentation
Generalities and documents:
The project consists of 9 pages (Layout, Index, Login, Register, Contact US (Form1), Exoplanets, Exoplanets-comparison, Day, Mars)
-	Layout:
This is the main page of the project, in this are all the links to the different files CSS, Javascript, Bootstrap, Image Folder. It contains the main menu as an element that will be fixed on the other pages. The body will be dynamic, so it will show the different pages in it.
Main Menu: This menu is designed with responsive design, so it will adapt to different devices. It has the logo section with an image (This has a link to the home page) and the name of the project as an H1. The links will take us to different pages, the options are: Home, Photo of this day, Mars potos, Contact, login (if the user is registered and logged in, they can access the link called "Exoplanets", if they are not logged in, this link will not be visible), the last item is the username.
-	Index:
This page is the home page of the project, it has a video of the shuttle takeoff, this video is in lopp and without audio. It has a short sentence that talks about the project, and a section where you can see images of a toy astronaut and various shapes behind it. The idea is just to have a brief explanation of the project and a nice and attractive first impression.
The footer is displayed on this page.
[![Home.png](https://i.postimg.cc/T3h6Zggj/Home.png)](https://postimg.cc/zym6hLd3) 

-	Login: 
On this page there is a login form, it has the username and password fields, a submit button and a phrase with a link to the register page for users who are not registered. The idea of this page is login, its design is clean, clear and designed in neumorphism style.
[![Login.png](https://i.postimg.cc/MpfL7D1L/Login.png)](https://postimg.cc/nXZTZqRK)

-	Register
On this page there is a register form, it has the user fields, user email, password, confirm password, a submit button and a phrase with a link to the login page for users who are already registered. The idea of this page is for the user to register and access all the features, its design is clean, clear and designed in neumorphism style.
[![Register.png](https://i.postimg.cc/fykCwzKP/Register.png)](https://postimg.cc/Fk53pQwb)

-	Contact US (Form1): 
On this page you have a glassmorphism style contact form, it has the username, email, message fields and a submit button. When loading all the fields, pressing the submit button will open the user's personal email and send the message to the address andresgenes01@gmail.com. But it's not just a contact page, on this page I've put a lot of emphasis on design, it has several background images that will move when you move the mouse (this is designed with Javascript modifying the DOM) and the mouse cursor is a Luminous orb that moves through Javascript following the movement generated by the user.
[![Contact.png](https://i.postimg.cc/2SnwjXQC/Contact.png)](https://postimg.cc/Js4JPxYF)

-	Exoplanets:
On this page we will see a presentation and explanation of how many exoplanets NASA has discovered so far and how many it has confirmed to date. He also explains that by pressing the button we will go to the "exoplanets comparison" page, in which we will compare the size of 8 real exoplanets discovered by NASA (We will see the largest, the smallest and 6 more planets. It has a sample video of the "exoplanets comparison" page. This page is available only to registered users. It has Glasmorphism style. The button changes its shape with Hover effect.
The footer is displayed on this page.

-	Photo of this day: 
It has Glasmorphism style.
It has a section where it shows an image of the moon, which will be replaced by pressing the button that says "Image of the day". Pressing the button will bring an image through API Rest that the NASA website has prepared, this image will be different every day.
It has a section that has an explanation of what this page does and what it will do if you press the "Image of the day" button, this explanation will be replaced via Javascript and Rest API with the explanation of the image and the title of the page. image. It gives a simple and elegant effect, but behind it there is a lot of work in Python, Javascript and DOM management.
The footer is displayed on this page.

[![Moon.png](https://i.postimg.cc/W3YmfRvw/Moon.png)](https://postimg.cc/1n6Nfj48)

-	Mars Photos:
It has Glasmorphism style.
It has a section where it shows an image of the Rover Curiosity, which will be replaced by pressing the button that says "Observe Mars". Pressing the button will bring up an image via Rest API that the rover has taken on its mission to Mars. Every time you press this button you will see a new image and the date it was taken.
It has a section that has an explanation of what this page does and what it will do if you press the “Observe Mars” button, this explanation will be replaced via Javascript and Rest API with the date of the image. It gives a simple and elegant effect, but behind it there is a lot of work in Python, Javascript and DOM management.
The footer is displayed on this page.

[![Mars.png](https://i.postimg.cc/JzCNFc9v/Mars.png)](https://postimg.cc/ZCjvB3Yx)

-	Exoplanets comparison:
This page is the most complex of the project, it has a dark background and a background of stars made with orbs generated by Javascript with random size, opacity and position.
By using the mouse wheel you can zoom in and out of the image.
By pressing the left mouse button you can change your position in X, Y and Z.
You will see the 8 exoplanets lined up and orbiting. The exoplanets simulate the movements of rotation and translation, this has been generated with Jasvascript.
Each exoplanet has a texture image that composes it and simulates the color and composition of some real planets.
This page was generated with a complex set of Javascript and Three JS functions.
I have used a JSON extracted from the NASA website with more than 9000 real exoplanets found.

[![Comparison.png](https://i.postimg.cc/G3ZgcDWJ/Comparison.png)](https://postimg.cc/Cdss7RLz)


7.	### Complexity (in order not to make this document too extensive, I will only explain the most complex pages)
It is a large project, with 9 pages, all very complex, we have used Django, Python, Javascript Sqlite3, CSS, HTML, Three JS, REST API, connected in real time with the NASA website.
-	As far as the Layout page has the main menu made by me (Not by Bootstrap), my idea was to make it with a more attractive design than the ones we found pre-designed by Bootstrap, the responsive design was created by me and carried out with Vanilla Javascript, and with features of hiding items generated with Python. The work is a combination of Python, Javascript and CSS. This menu will be present on the other pages.

-	On the Contact Us page this page will see a combination of Python, Javascript and CSS. It has a mousemove effect on the images, by means of Javascript the background images (Planets, stars, galaxies, etc) will be moved by moving the mouse over different places on the page.
You'll also see a combination of Python, Javascript, and CSS to catch the mouse cursor event, get the X and Y coordinates, and replace it with a glowing orb.
I could have made just one contact page, but I didn't settle for that, I wanted this one to be special.

-	As for the “Photo of this Day” page, it is made with CSS HTML and Javascript. I've taken various elements from the HTML via the querySelector method and the getElementById method and stored them in variables in our Javascript document.
I have registered on the NASA website to obtain our API Key, previously I have tried to interpret the data that we have available to use in our project, this has been a challenge.
Once we have obtained our API Key, we will use it in our asynchronous Javascript function, the function has to be asynchronous because when the function is executed to deliver my credentials and get the data that I have chosen to bring from the Nasa website it will pass a small span of time.
Once I have dynamically obtained the data from the NASA website I have created a function to create elements, this function will change elements of the “Photho of the Day” page for the elements that we have obtained in the asynchronous function.

-	On the “Mars Photos” page is made with CSS HTML and Javascript. I've taken various elements from the HTML via the querySelector method and the getElementById method and stored them in variables in our Javascript document. Once we've obtained our API Key, we'll use it in our asynchronous Javascript function in our app.js document.
In our asynchronous function we will get the images taken by the Rover Curiosity and all the image data, I have only used the date the photo was taken. This function will use the JSON data to process it and change the image of the Rover for the image it has taken and in the part where the explanation of what the page does when you press the "Observe Mars" button is for the date on which the photo has been taken. Also, it should change the photo and show the next one in the list each time the button is pressed and the date of the image will replace to the previous date (do not do an accumulation of dates, but should be replaced)

-	 The “Exoplanets Comparison” page is the most complex of the project, it is generated with HTML, CSS Javascript and Three JS.
I have already explained the operation of the page, but now I will explain the design of this page from a technical point of view, for this I will only explain how I have worked in the Javascript.nasaExoplamnets.js document:
First I have created the different elements that we will use in the different functions (for example, camera, scene, renderer, etc)
The "init" function will create the environment, the "space", the "camera" through which the user will see the scene, the different planets with their radii and their geometry, as well as the textures that each planet has.
The “animate” function will set the movements of the planets.
The functions randomFloat, randomInt, shuffle, addStarField will create the starry sky.
The distributedCopy function will work by choosing the 8 planets from the list or JSON provided by NASA.
The asynchronous function will call the JSON to process the data and will call the other functions to display everything on the page for the user to use.

The achievement of the project was long and ambitious, but I can say that it has been a pleasure to work on it.

8.	### Files and Folders

The Nasassistant project has several folders and files:
It has two main folders “nasassistant” and “project5”, it also has the database “db.sqlite3”, a file called “manage.py” and this file.
-	 Inside the “nasassistant” folder there are folders (__pycache__, migrations, static, templates) and Python documents (__init__.py, admin.py, apps.py, forms.py, models.py, tests.py, urls. py, views.py):
Inside the __pycache__ folder are several .pyc files; Inside the migrations folder there is another __pycache__ folder and several documents related to migrations, these have a .py extension; In the Static folder there is another folder called nasassistant, the nasassistant folders are css, imq, js, planetTextures (in css are the style files, in img are the images and videos of the project, in js are the javascript files, in planetTextures you have the images of the textures of the planets); In the templates folder we have a folder called nasassistant, in this are the different HTML files of the project (these are: day.html, exoplanets_comparison.html, exoplanets.html, form1.html, index.html, layout.html, login.html , mars.html, register.html.
-	Inside the “project5” folder there is another folder called __pycache__, there are also several Python files, these are: __init__.py, asgi.py, settings.py, url.py, wsgi.py.

9. ### The application is executed by opening a console (with a source-code editor for example if you open it with VSCode) call the manage.py file with the command "manage.py runserver" this will generate a local server http://127.0 .0.1:8000/.

## Checklist

1. Different from previous projects. DONE
2. More complex than previous projects. DONE
3. The Readme.md has to clarify why the project is different enough from other projects. DONE
4. Django with at least one model. DONE
5. Javascript on the front-end. DONE
6. Compatible with mobile devices. DONE 
7. Readme.md with length of several paragraphs. DONE 
8. Readme.md with full documentation of what you did and why you did it. DONE
9. Readme.md has to document your project thoroughly, defending its complexity. DONE
10. Readme.md in the main directory, with a description of the project. DONE

11. Under your own heading put a heading called "Distinctiveness and Complexity" below put an explanation of why it meets the above points. DONE 
12. Which contains each file you created. DONE 
13. How to run the application. DONE 
14. Any other additional information that staff need to know about your project. DONE
15. If there is a python package that needs to be installed add it to a file called requirements.txt. Donate (It has not been necessary). DONE
16. Readme.md of at least 500 words. DONE
