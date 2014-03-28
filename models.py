from google.appengine.ext import ndb 


class User(ndb.Model):
	"""Models an individual Google user and her OAuth info"""
	user_first_name = ndb.StringProperty()
	user_last_name = ndb.StringProperty()
	user_email_address = ndb.StringProperty()


class Hike(ndb.Model):
	"""Models an invidual hiking expedition"""
	hike_reservation_status = ndb.StringProperty()
	hike_weather = ndb.StringProperty()
	hike_location_name = ndb.StringProperty()
	hike_hazards = ndb.StringProperty()
	hike_route_url = ndb.StringProperty()
	hike_pictures_url = ndb.StringProperty()
	hike_notes = ndb.StringProperty()
	hike_distance = ndb.FloatProperty()
	hike_location_longitude = ndb.FloatProperty()
	hike_location_latitude = ndb.StringProperty()
	hike_elevation_gain = ndb.IntegerProperty()
	hike_start_datetime = ndb.DateTimeProperty()
	hike_end_datetime = ndb.DateTimeProperty()


class User_Hike_RSVP():
	"""Models a single RSVP from a single user for a single hike"""
	user_key = ndb.KeyProperty()
	hike_key = ndb.KeyProperty()
	rsvp_status = ndb.StringProperty()
