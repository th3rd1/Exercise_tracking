# Exercise_tracking
A project using Nutritionix api and sheety api to track exercise in a google sheet. Nutritionix using natural language processing so you can type "ran 3 miles" as if speaking normally and the api will provide the expected duration and calories burned. Sheetly pushes the data generated as well as today's date and time to the spreadsheet to log data.

NOTES
This was a fun project. I spent the most time by far trying to figure out how to post a request using sheety. needing
to have the inputs nested in a root property, tripped me up for longer than I care to admit. I kept trying to just
write the property but that would invalidate the refrences to exercise stats and the date/time. Lots of googling
later I was able to find an example and use a for loop to get the job done.

For ease of use in the future I added this codebase to replit for access on the go. This helped practice some additional
environmental variable use.
