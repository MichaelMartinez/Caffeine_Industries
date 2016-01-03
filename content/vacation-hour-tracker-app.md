Title: Vacation Hour Tracker App 
Date: 2012-01-23 21:13
Author: Michael
Category: Blog, code, Google, Javascript, jQuery Mobile, knockout, localStorage, Programming, Uncategorized
Slug: vacation-hour-tracker-app
Status: published

Most of us deal with some aspect of our job/career that isn't directly
under our control. For those who do not know, I am a firefighter for a
medium to large metropolitan fire department that is located 1.5 hours
south of Phoenix, Az. There are many of aspects in my job that I have
very little control over.

Recently, I was charged for three days of vacation time that I did not
take. I have to admit that I caught the error by mistake as I generally
glance at the number of hours without much thought. When I realized the
error, I decided to go back and inspect the last six months and I found
two more errors... Which prompted another 6 months of inspection and one
more error.

I really don't want to painstakingly evaluate and cross reference my pay
stub to our staffing software for correctness every two weeks. That
isn't exactly my idea of a good time. So I wrote this little application
that should, in theory, be my ever watchful vacation hour sentry. As a
great by product of writing this app, I investigated several javascript
MV\* / MVVM frameworks and various libraries.

The libraries used for this app are:

1.  [Phonegap / Cordova - Phone
    version](https://github.com/brianleroux/Cordova)
2.  [Knockoutjs - MVVM Framework / Data
    Binding](https://github.com/SteveSanderson/knockout)
3.  [jQuery Mobile - 1.0](http://www.jquerymobile.com)
4.  [jStorage - localStorage](https://github.com/andris9/jStorage)
5.  [Momentjs - JavaScript Date
    Library](https://github.com/timrwood/moment)
6.  [Mobiscroll jQuery Mobile
    plugin](http://code.google.com/p/mobiscroll/)
7.  Zend Framework GData Library - PHP

The file tree and code are completely UGLY and it is not
my prettiest work to be sure. So when you go snooping around the
src remember I've been HACKING on this like crazy. I have three or four
implementations of this app contained within the asset/www file so be
sure to snoop around and look at the backbone version and vanilla jQuery
mobile version.

I chose to go with Knockout for a variety of reasons for the main app.
The big reason was that it works with my brain and I was able to
accomplish a ton with very little boilerplate. I really eff'ing hate
boilerplate. I watched several Backbone tutorials and I read countless
lines of Backbone code and I was (am?) still pretty much lost. It made
me work way too hard to get basic functionality. I had several "aha"
moments with Backbone... only to have them stuffed in my pie-hole
minutes later. Not a good experience but I plan on re-visiting Backbone
in the future.

I'll have several follow on posts regarding this app in the coming days.
I will also spend some time styling this app as its is default to a
fault right now using non-standard icons and Adobe Fireworks. I can post
that as a tutorial if there is interest.

Here is the fully functional app (tested with Safari 5+, Firefox 9,
Chrome 16 on Mac):

\[advanced\_iframe
securitykey="da39a3ee5e6b4b0d3255bfef95601890afd80709"
src="http://lab.caffeineindustries.com/VacationBalance2/assets/www/indexTestKO.html"
width="450" height="800" scrolling="yes" marginwidth="2"
marginheight="2" frameborder="2"\]
