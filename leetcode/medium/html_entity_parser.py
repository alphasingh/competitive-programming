"""
https://leetcode.com/problems/html-entity-parser/
"""

import re


class Solution:

    @staticmethod
    def entityParser(text: str) -> str:
        text = re.sub(rf"&quot;", "\"", text)
        text = re.sub(rf"&apos;", "\'", text)
        text = re.sub(rf"&gt;", ">", text)
        text = re.sub(rf"&lt;", "<", text)
        text = re.sub(rf"&frasl;", "/", text)
        text = re.sub(rf"&amp;", "&", text)
        return text


input_html = "&amp;gt;"
output_html = "&gt;"
assert Solution.entityParser(input_html) == output_html

input_html = "&amp; is an HTML entity but &ambassador; is not."
output_html = "& is an HTML entity but &ambassador; is not."
assert Solution.entityParser(input_html) == output_html
"""Explanation: The parser will replace the &amp; entity by &"""

input_html = "and I quote: &quot;...&quot;"
output_html = "and I quote: \"...\""
assert Solution.entityParser(input_html) == output_html

input_html = "Stay home! Practice on Leetcode :)"
output_html = "Stay home! Practice on Leetcode :)"
assert Solution.entityParser(input_html) == output_html

input_html = "x &gt; y &amp;&amp; x &lt; y is always false"
output_html = "x > y && x < y is always false"
assert Solution.entityParser(input_html) == output_html

input_html = "leetcode.com&frasl;problemset&frasl;all"
output_html = "leetcode.com/problemset/all"
assert Solution.entityParser(input_html) == output_html
