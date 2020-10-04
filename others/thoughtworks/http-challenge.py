import requests

BASE_URL = 'https://http-hunt.thoughtworks-labs.net'


def validate_response(response):
    if response.status_code != 200:
        raise AssertionError('API response {} code not 200'.format(response))


challenge_input = requests.get(BASE_URL + '/challenge/input',
                               headers={'userId': 'HtjVvUpVU', 'Content-Type': 'application/json'})
print('Response for input gathering: {}'.format(challenge_input.json()))
# validate_response(challenge_input)

challenge_input_text = challenge_input.json().get('text').lower()
challenge_input_a_count = challenge_input_text.count('a')
challenge_input_e_count = challenge_input_text.count('e')
challenge_input_i_count = challenge_input_text.count('i')
challenge_input_o_count = challenge_input_text.count('o')
challenge_input_u_count = challenge_input_text.count('u')
challenge_output = {
    "a": challenge_input_a_count,
    "e": challenge_input_e_count,
    "i": challenge_input_i_count,
    "o": challenge_input_o_count,
    "u": challenge_input_u_count,
}
challenge_output_response = requests.post(BASE_URL + '/challenge/output',
                                          headers={'userId': 'HtjVvUpVU', 'Content-Type': 'application/json'},
                                          json=challenge_output)
print('Response for output submission: {}'.format(challenge_output_response.json()))
validate_response(challenge_output_response)
