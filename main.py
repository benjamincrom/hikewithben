import datetime

import models
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


#@app.route('/')
#def hello():
#    """Return a friendly HTTP greeting."""
#    return 'Hello World!'


@app.route('/')
def ingest():
	"""Open a TSV and ingest into datastore"""
	with open('hiking_cal.tsv') as tsv_filehandle:
		for line in tsv_filehandle.readlines():
			list_of_row_cells = line.split('\t')

			date_str = list_of_row_cells[0]
			(month,day,year) = date_str.split('/')
			this_datetime = datetime.datetime(int(year),int(month),int(day),0,0)
			day_interval = datetime.timedelta(days=1)
			start_datetime = this_datetime - day_interval
			end_datetime = this_datetime + day_interval

			this_hike = models.Hike(
				hike_start_datetime=start_datetime,
				hike_end_datetime=end_datetime,
				hike_location_name=list_of_row_cells[1],
				hike_reservation_status=list_of_row_cells[4],
			)
			if len(list_of_row_cells) >= 8:
				this_hike.hike_notes=list_of_row_cells[8]
				this_hike.hike_hazards=list_of_row_cells[7]
				
			this_hike.put()

	return "Done"


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
