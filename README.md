A web application for managing events. 
The system allows users to create, view, update, and delete events. Each event has details such as name, description, date, time, and location.
Users are able to register for events.

Requirements:

Event Model:

Name: The name of the event (string, max length 200).
Description: A description of the event (text).
Date: The date of the event.
Time: The time of the event.
Location: The location of the event (string, max length 200).
Capacity: The maximum number of attendees (integer).


Attendee Model:

Name: The name of the attendee (string, max length 100).
Email: The email of the attendee (string, unique).
Event: ForeignKey to the Event model to link attendees to events.


Views:

Event List View: Display a list of all events with their details.
Event Detail View: Display detailed information about a single event.
Event Create View: Allow users to create a new event.
Event Update View: Allow users to update the details of an existing event.
Event Delete View: Allow users to delete an event.
Registration View: Allow users to register for an event.


Templates:

Used HTML templates to render the views.
Used Django's template language to loop through and display events in the list view.
Provided forms for creating and updating events and for registering attendees.

URL Configuration:
Set up URL routes for each view (list, detail, create, update, delete, register).


Admin Interface:
Use Django's admin interface to manage events and attendees.

Basic Styling:
Added basic CSS to make the application look presentable.











![Screenshot 2024-06-19 011235](https://github.com/tansrh/Eventify/assets/107149612/05c8b92f-568f-471e-97f8-bf90fe1f320c)
![Screenshot 2024-06-19 011257](https://github.com/tansrh/Eventify/assets/107149612/581f5354-bdc2-48f0-9676-5f2adc8a13b3)
![Screenshot 2024-06-19 011321](https://github.com/tansrh/Eventify/assets/107149612/1d791530-640a-4d5a-b8cd-f308bbbd9d5f)
![Screenshot 2024-06-19 011407](![Screenshot 2024-06-19 011452](https://github.com/tansrh/Eventify/assets/107149612/7c4a6fb1-2dc5-4cc7-89ca-5d69cd506db9)
https://github.com/tansrh/Eventify/assets/107149612/0207a0e7-32a7-4323-a280-e82f951e93c3)
