import requests

# https://developers.google.com/maps/documentation/directions/get-directions

BASE_URL = 'https://maps.googleapis.com/maps/api/directions/json' \
           '?key=API_KEY' \
           '&origin=49.2472501,-122.7552604' \
           '&destination=49.2472501,-122.7552604' \
           '&waypoints=' \
           '49.2472501,-122.7552604|' \
           '49.2810138,-123.0602546|' \
           '49.2810138,-123.0602546|' \
           '49.2472501,-122.7552604'
get_directions = requests.get(BASE_URL).json()

print('directions: {}'.format(get_directions))

"""
            "visits": [
                {
                    "orderItemId": 1472,
                    "visited": true,
                    "visitedAt": "2021-09-22T15:03:42Z",
                    "driverNearbyNotificationSent": false,
                    "distance": 6248.2,
                    "type": "PICKUP",
                    "arrivalTime": "00:07",
                    "finishTime": "00:12",
                    "updatedAt": "2021-09-22T15:03:42Z"
                },
                {
                    "orderItemId": 1472,
                    "visited": true,
                    "visitedAt": "2021-09-22T15:56:59Z",
                    "driverNearbyNotificationSent": true,
                    "driverNearbyNotificationSentAt": "2021-09-22T15:53:15Z",
                    "distance": 28022.8,
                    "type": "DROPOFF",
                    "arrivalTime": "00:34",
                    "finishTime": "00:39",
                    "updatedAt": "2021-09-22T15:56:59Z"
                },
                {
                    "orderItemId": 1491,
                    "visited": true,
                    "visitedAt": "2021-09-22T16:04:43Z",
                    "driverNearbyNotificationSent": true,
                    "driverNearbyNotificationSentAt": "2021-09-22T15:53:22Z",
                    "distance": 0.0,
                    "type": "PICKUP",
                    "arrivalTime": "00:39",
                    "finishTime": "00:44",
                    "updatedAt": "2021-09-22T16:04:43Z"
                },
                {
                    "orderItemId": 1491,
                    "visited": true,
                    "visitedAt": "2021-09-22T16:20:42Z",
                    "driverNearbyNotificationSent": false,
                    "distance": 28317.1,
                    "type": "DROPOFF",
                    "arrivalTime": "01:05",
                    "finishTime": "01:10",
                    "updatedAt": "2021-09-22T16:20:42Z"
                }
            ],
"""
