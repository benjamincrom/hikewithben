#!/usr/bin/python

import datetime
import endpoints

from protorpc import message_types
from protorpc import messages
from protorpc import remote

import models


ENTRY_REQUEST_RESOURCE_CONTAINER = endpoints.ResourceContainer(
    message_types.VoidMessage,
    hike_id=messages.IntegerField(2, required=True)
)

LIST_REQUEST_RESOURCE_CONTAINER = endpoints.ResourceContainer(
    message_types.VoidMessage,
)


@endpoints.api(name="hikewithben", version="v1")
class HikeWithBenApi(remote.Service):
    """Concierge API v1."""
    @staticmethod
    @endpoints.method(LIST_REQUEST_RESOURCE_CONTAINER,
                      models.HikeMessageCollection,
                      path="hike_list",
                      http_method="GET",
                      name="hike.listHikes")
    def list_hikes(self, request):
        hike_message_collection_obj = models.HikeMessageCollection(hike_list=[])
        hike_query = models.Hike.query().order(-models.Hike.hike_start_datetime)

        for this_query in hike_query.iter():
            hike_message_collection_obj.hike_list.append(
                self.get_hike_message_from_query_obj(this_query)
            )

        return hike_message_collection_obj

    @staticmethod
    @endpoints.method(ENTRY_REQUEST_RESOURCE_CONTAINER,
                      models.HikeMessage,
                      path="hike_display/{hike_id}",
                      http_method="GET",
                      name="hike.displayHike")
    def display_hike(self, request):
        hike_obj = models.Hike.get_by_id(request.hike_id)
        return self.get_hike_message_from_query_obj(hike_obj)

    @classmethod
    def convert_datetime_to_str(cls, datestring):
        if datestring:
            this_datetime = datetime.datetime.strptime(str(datestring), "%Y-%m-%d %H:%M:%S")
            formatted_str = this_datetime.strftime('%A, %d %B %Y')
        else:
            formatted_str = ''

        return formatted_str
    
    @classmethod
    def is_date_in_future(cls, given_datetime):
        return given_datetime > datetime.datetime.now()

    @classmethod
    def get_hike_message_from_query_obj(cls, query_obj):
        # Get hike data into message object
        this_hike_message = models.HikeMessage(
            hike_id=query_obj.key.id(),
            hike_reservation_status=query_obj.hike_reservation_status,
            hike_location_name=query_obj.hike_location_name,
            hike_hazards=query_obj.hike_hazards,
            hike_route_url=query_obj.hike_route_url,
            hike_pictures_url=query_obj.hike_pictures_url,
            hike_notes=query_obj.hike_notes,
            hike_distance_miles=query_obj.hike_distance_miles,
            hike_location_longitude=query_obj.hike_location_longitude,
            hike_location_latitude=query_obj.hike_location_latitude,
            hike_elevation_gain=query_obj.hike_elevation_gain,
            hike_total_capacity=query_obj.hike_total_capacity,
            hike_start_datetime=query_obj.hike_start_datetime,
            hike_in_future=cls.is_date_in_future(query_obj.hike_start_datetime),
            hike_end_datetime=query_obj.hike_end_datetime,
            hike_start_datestring=cls.convert_datetime_to_str(query_obj.hike_start_datetime),
            hike_end_datestring=cls.convert_datetime_to_str(query_obj.hike_end_datetime),
        )

        return this_hike_message


api_application = endpoints.api_server([HikeWithBenApi])
