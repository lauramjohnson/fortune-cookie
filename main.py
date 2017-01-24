#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    fortunes = [
        "You will find a bushel of money",
        "Your smile will tell you what makes you feel good.",
        "Don't panic",
        "The best year-round temperature is a warm heart and a cool head",
        "It could be better, but it's good enough.",
        "You will find a thing. It may be important",
        "Your reality check is about to bounce.",
        "When chosen for jury duty, tell judge fortune cookie say 'guilty!'",
        "Stop eating now. Food poisoning no fun.",
        "Okay to look at past and future. Just don't stare.",
        "He who dies with most toys, still dies.",
        "Person who argues with idiot is taken for fool.",
        "This fortune no good. Try another.",
    ]
    return fortunes[random.randint(0,len(fortunes)-1)]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"
        fortune="<strong>" + getRandomFortune() + "</strong>"
        fortune_sentence = "Your fortune:  " + fortune
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"

        lucky_number = "<strong>" + str(random.randint(1,100)) + "</strong>"
        number_sentence = "Your Lucky numbers: " + lucky_number
        number_paragraph = "<p>" + number_sentence + "</p>"


        morecookie_button = "<a href='.'><button>Another cookie please!</button></a>"

        self.response.write(header + fortune_paragraph + number_paragraph + morecookie_button)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
