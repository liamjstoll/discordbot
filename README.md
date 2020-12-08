# discordbot
A discord bot that makes stock recommendations based off reddit

Currently, the bot is really elementary, and the runtime is trash. I will rewrite it. The code is in a single file, and the logic is close to the following...

counter for stock A, counter for stock B,...counter for stock n.
string associated with stock A, string associated with stock B, .... , string associated with stock n.

go to certain subreddits.
     for a certain number of 'hot' and 'top' posts in these subreddits
         look for the strings, if found, increment the respective stock's counter by one. 

im using the PRAW python module.
