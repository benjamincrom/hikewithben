#!/usr/bin/python


from google.appengine.ext import ndb
from protorpc import messages, message_types


# Appengine DB declaration
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
    rsvp_status = ndb.StringProperty()


# Message object declaration
class PersonNameMessage(messages.Message):
    """Message for containing an invidual first name and last initial"""
    first_name = messages.StringField(1)
    last_initial = messages.StringField(2)


class HikeMessage(messages.Message):
    """Message for containing all info related to a single hike"""
    hike_id = messages.IntegerField(1)
    hike_reservation_status = messages.StringField(2)
    hike_location_name = messages.StringField(3)
    hike_hazards = messages.StringField(4)
    hike_route_url = messages.StringField(5)
    hike_pictures_url = messages.StringField(6)
    hike_notes = messages.StringField(7)
    hike_start_datestring = messages.StringField(8)
    hike_end_datestring = messages.StringField(9)
    hike_distance_miles = messages.FloatField(10)
    hike_location_longitude = messages.FloatField(11)
    hike_location_latitude = messages.FloatField(12)
    hike_elevation_gain = messages.IntegerField(13)
    hike_total_capacity = messages.IntegerField(14)
    hike_in_future = messages.BooleanField(15)
    hike_start_datetime = message_types.DateTimeField(16)
    hike_end_datetime = message_types.DateTimeField(17)
    rsvp_yes_list = messages.MessageField(PersonNameMessage, 18, repeated=True)


class HikeMessageCollection(messages.Message):
    """Message for containing a list of HikeMessage objects"""
    hike_list = messages.MessageField(HikeMessage, 1, repeated=True)
