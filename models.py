from google.appengine.ext import ndb 
from google.appengine.ext.ndb import msgprop

from protorpc import messages, message_types


# Appengine DB declaration
class RSVP(messages.Enum):
	"""RSVP Enum class with all possible choices for RSVP"""
	YES = "Yes"
	MAYBE = "Maybe"
	NO = "No"


class User(ndb.Model):
	"""Models an individual Google user and her OAuth info"""
	user_first_name = ndb.StringProperty()
	user_last_name = ndb.StringProperty()
	user_email_address = ndb.StringProperty()


class Hike(ndb.Model):
	"""Models an invidual hiking expedition"""
	hike_reservation_status = ndb.StringProperty()
	hike_location_name = ndb.StringProperty()
	hike_hazards = ndb.StringProperty()
	hike_route_url = ndb.StringProperty()
	hike_pictures_url = ndb.StringProperty()
	hike_notes = ndb.StringProperty()
	hike_distance_miles = ndb.FloatProperty()
	hike_location_longitude = ndb.FloatProperty()
	hike_location_latitude = ndb.FloatProperty()
	hike_elevation_gain = ndb.IntegerProperty()
	hike_total_capacity = ndb.IntegerProperty()
	hike_start_datetime = ndb.DateTimeProperty()
	hike_end_datetime = ndb.DateTimeProperty()


class User_Hike_RSVP():
	"""Models a single RSVP from a single user for a single hike"""
	user_key = ndb.KeyProperty()
	hike_key = ndb.KeyProperty()
	rsvp_status = msgprop.EnumProperty(RSVP)


# Message object declaration
class PersonNameMessage(message.Message):
	"""Message for containing an invidual first name and last initial"""
	first_name = messages.StringField(1)
	last_initial = messages.StringField(2)


class HikeMessage(messages.Message):
	"""Message for containing all info related to a single hike"""
	hike_reservation_status = messages.StringField(1)
	hike_location_name = messages.StringField(2)
	hike_hazards = messages.StringField(3)
	hike_route_url = messages.StringField(4)
	hike_pictures_url = messages.StringField(5)
	hike_notes = messages.StringField(6)
	hike_distance_miles = messages.FloatField(7)
	hike_location_longitude = messages.FloatField(8)
	hike_location_latitude = messages.FloatField(9)
	hike_elevation_gain = messages.IntegerField(10)
	hike_total_capacity = messages.IntegerField(11)
	hike_start_datetime = messages.DateTimeField(12)
	hike_end_datetime = message_types.DateTimeField(13)
    rsvp_yes_list = messages.MessageField(PersonNameMessage, 14, repeated=True)


class HikeMessageCollection(messages.Message):
	"""Message for containing a list of HikeMessage objects"""
    hike_list = messages.MessageField(HikeMessage, 1, repeated=True)
