import requests
import datetime

"""
Resources: https://apisetu.gov.in/public/marketplace/api/cowin
"""

BASE_URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public'
VACCINATIONS_TO_SEARCH = ('COVISHIELD', 'COVAXIN')
DAYS_TO_SEARCH_IN_FUTURE = 1
DISTRICTS = {'Amritsar': '485', 'Barnala': '483', 'Bathinda': '493', 'Faridkot': '499', 'Fatehgarh Sahib': '484',
             'Fazilka': '487', 'Ferozpur': '480', 'Gurdaspur': '489', 'Hoshiarpur': '481', 'Jalandhar': '492',
             'Kapurthala': '479', 'Ludhiana': '488', 'Mansa': '482', 'Moga': '491', 'Pathankot': '486',
             'Patiala': '494', 'Rup Nagar': '497', 'Sangrur': '498', 'SAS Nagar': '496', 'SBS Nagar': '500',
             'Sri Muktsar Sahib': '490', 'Tarn Taran': '495'}
DISTRICT_TO_SEARCH = DISTRICTS['Jalandhar']
TODAY = datetime.date.today()


# centers with 18+ vaccines in past -> 604825 (Ankur Kids Hospital), 604572 (Genesis Fertility)

def formatter(date_in_datetime: datetime.date) -> str:
    return date_in_datetime.strftime("%d-%m-%Y")


def find_favorable_centers_on_day(date_to_search: str, district_to_search: str):
    # date_to_search should be like 31-12-2021, district_to_search should be in DISTRICTS
    assert district_to_search in DISTRICTS
    favorable_center_sessions = {}
    query_params = {'district_id': DISTRICTS[district_to_search], 'date': date_to_search}
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
               and center_session['vaccine'] in VACCINATIONS_TO_SEARCH \
               and center_session['slots']

    for center in centers_data:
        sessions = center['sessions']
        for session in sessions:
            session_id = session['session_id']
            if isSessionFavourable(session) and session_id not in favorable_center_sessions:
                # print(center['name'], session)
                favorable_center_sessions[session_id] = session

    return favorable_center_sessions


favorable_sessions = {}
for district in DISTRICTS:
    for delta in range(DAYS_TO_SEARCH_IN_FUTURE):
        searching_date = formatter(TODAY + datetime.timedelta(days=delta))
        # print('Searching favorable centers for ', searching_date)
        favorable_sessions_on_day = find_favorable_centers_on_day(searching_date, district)
        favorable_sessions.update(favorable_sessions_on_day)

print(favorable_sessions.keys())
