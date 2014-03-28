hikewithben.com design requiqrements
====================================

Interface
---------

### hikewithben.com/index.html
1. Display a list of all hikes (past and future).  Each hike will receive its own block about 500 pixels high and 
  90% of page width (blog style)
2. Each block will contain the following trip data:
  * start of hike date and time
  * end of hike date and time
  * location
  * distance (mi)
  * elevation gain (ft)
  * reservation status
  * temperature range
  * weather
  * hazards
  * route
  * link to pictures (thumbnails?)
  * other notes
  * RSVPs for this hike
3. Link to recommended gear list
4. Link to recommended reading list
5. Display goofy animation of Ben hiking in header
6. Integrate Google Maps/Google Earth with "route" data in block

### User Capabilities 
1. Authenticate with Google account (OAuth)
2. RSVP for any future hike
3. Cancel RSVP for any future hike to which you RSVP'd
4. Google Calendar integration
5. Automatic email reminders (with opt-out/unsubscribe option)
6. Personal mileage calculator

### Stored Data
* User
  * Join date
  * Which hikes have RSVP responses and those responses ("Yes", "No", "Maybe")
  * First name
  * Last initial
  * Email address

* Hike
  * date
  * location title
  * location latitude (decimal degree) 
  * location longitude (decimal degree) 
  * hike distance (mi)
  * elevation gain (ft)
  * reservation status
  * temperature range
  * weather
  * hazards
  * route (GPX or KML)
  * picture locations
  * notes
  * users who have RSVP'd hike and their statuses
