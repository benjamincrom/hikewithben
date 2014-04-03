import datetime

import models
import webapp2


# All hikes begin at 7:30 PM
START_HOUR = 19
START_MINUTE = 30
# All hikes end at 3:30 PM
END_HOUR = 15
END_MINUTE = 30


class MainPage(webapp2.RequestHandler):
	def get(self):
		"""Open a CSV containing hike info and ingest into datastore"""
		with open('hiking_cal.csv') as csv_filehandle:
			for line in csv_filehandle.readlines():
				row_cells_list = line.split(';')

				start_date_str = row_cells_list[0]
				(start_month, start_day, start_year) = start_date_str.split('/')
				start_datetime = datetime.datetime(
					int(start_year),
					int(start_month),
					int(start_day),
					START_HOUR,  
					START_MINUTE,
				)

				end_date_str = row_cells_list[1]
				(end_month, end_day, end_year) = end_date_str.split('/')
				end_datetime = datetime.datetime(
					int(end_year),
					int(end_month),
					int(end_day),
					END_HOUR,  
					END_MINUTE,
				)

				this_hike = models.Hike(
					hike_start_datetime=start_datetime,
					hike_end_datetime=end_datetime,
					hike_location_name=row_cells_list[2],
					hike_reservation_status=row_cells_list[5],
					hike_hazards=row_cells_list[6],
					hike_route_url=row_cells_list[7],
					hike_notes=row_cells_list[8],
					hike_pictures_url=row_cells_list[9],
					hike_total_capacity=int(row_cells_list[10]),
				)
				# Check if string is just whitespace or actually contains a value
				if row_cells_list[3].strip(): 
					this_hike.hike_distance = float(row_cells_list[3])
				if row_cells_list[4].strip(): 
					this_hike.hike_elevation_gain = int(row_cells_list[4])
				if row_cells_list[11].strip(): 
					this_hike.hike_location_longitude = float(row_cells_list[11])
				if row_cells_list[12].strip():
					this_hike.hike_location_latitude = float(row_cells_list[12])

				this_hike.put()

	   	self.response.write("Data has been ingested!")


ingest_application = webapp2.WSGIApplication([
    ("/", MainPage),
], debug=True)