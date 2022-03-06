class Solution:
    @staticmethod
    def solution(stations_a: [str], stations_b: [str], stations_c: [str], origin: str, destination: str) -> str:
        ticket = ''
        # origin x destination
        if origin in stations_a:
            if destination in stations_a or destination in stations_b:
                ticket = 'AB'
            elif destination in stations_c:
                ticket = 'ABC'
        elif origin in stations_b:
            if destination in stations_b or destination in stations_a:
                ticket = 'AB'
            elif destination in stations_c:
                ticket = 'BC'
        elif origin in stations_c:
            if destination in stations_c or destination in stations_b:
                ticket = 'BC'
            elif destination in stations_a:
                ticket = 'ABC'
        return ticket


assert Solution.solution(stations_a=['g', 'h'],
                         stations_b=['m', 'br'],
                         stations_c=['f', 'b'],
                         origin='f',
                         destination='g') == 'ABC'
assert Solution.solution(stations_a=['g', 'h'],
                         stations_b=['m', 'br'],
                         stations_c=['f', 'b'],
                         origin='h',
                         destination='g') == 'AB'
assert Solution.solution(stations_a=['g'],
                         stations_b=['m'],
                         stations_c=['f'],
                         origin='h',
                         destination='f') == ''
