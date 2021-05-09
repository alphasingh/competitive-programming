import requests
import datetime

BASE_URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public'
DISTRICTS = {'JALANDHAR': '492'}

TODAY = datetime.date.today()


def convert_to_required_date_format(date_in_datetime: datetime.date) -> str:
    return '{}-{}-{}'.format(date_in_datetime.day, date_in_datetime.month, date_in_datetime.year)


query_params = {'district_id': DISTRICTS['JALANDHAR'], 'date': '17-05-2021'}
headers = {'User-Agent': "PostmanRuntime/7.18.0"}

get_all_calendars = requests.get(
    BASE_URL + '/calendarByDistrict',
    headers=headers,
    params=query_params)

print(get_all_calendars.json())
centers_data = get_all_calendars.json()['centers']
print('Total {} centers found'.format(len(centers_data)))


def isSessionFavourable(center_session) -> bool:
    return center_session['available_capacity'] > 0 \
           and center_session['vaccine'] == 'COVISHIELD' \
           and center_session['slots']


for center in centers_data:
    sessions = center['sessions']
    for session in sessions:
        if isSessionFavourable(session):
            print(center['name'], session)
