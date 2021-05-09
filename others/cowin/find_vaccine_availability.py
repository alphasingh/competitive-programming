import requests
import datetime

BASE_URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public'
DISTRICTS = {'JALANDHAR': '492'}
DISTRICT_TO_SEARCH = DISTRICTS['JALANDHAR']
TODAY = datetime.date.today()


# centers with 18+ vaccines in past -> 604825 (Ankur Kids Hospital), 604572 (Genesis Fertility)

def formatter(date_in_datetime: datetime.date) -> str:
    return date_in_datetime.strftime("%d-%m-%Y")


def find_favorable_centers_on_day(date_to_search):  # 31-12-2021
    favorable_center_sessions = {}
    query_params = {'district_id': DISTRICT_TO_SEARCH, 'date': date_to_search}
    headers = {'User-Agent': 'PostmanRuntime/7.18.0'}

    get_all_calendars = requests.get(
        BASE_URL + '/calendarByDistrict',
        headers=headers,
        params=query_params)

    # print(get_all_calendars.json())
    centers_data = get_all_calendars.json()['centers']

    # print('Total {} centers found'.format(len(centers_data)))

    def isSessionFavourable(center_session) -> bool:
        return center_session['min_age_limit'] == 18 \
               and center_session['available_capacity'] > 0 \
               and center_session['vaccine'] in ('COVISHIELD', 'COVAXIN') \
               and center_session['slots']

    for center in centers_data:
        sessions = center['sessions']
        for session in sessions:
            session_id = session['session_id']
            if isSessionFavourable(session) and session_id not in favorable_center_sessions:
                # print(center['name'], session)
                favorable_center_sessions[session_id] = session

    return favorable_center_sessions


DAYS_TO_SEARCH_IN_FUTURE = 5
favorable_sessions = {}
for delta in range(0, DAYS_TO_SEARCH_IN_FUTURE):
    searching_date = formatter(TODAY + datetime.timedelta(days=delta))
    # print('Searching favorable centers for ', searching_date)
    favorable_sessions_on_day = find_favorable_centers_on_day(searching_date)
    favorable_sessions.update(favorable_sessions_on_day)

print(favorable_sessions.keys())
