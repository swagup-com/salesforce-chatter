# salesforce-chatter
Python Library for Salesforce Chatter

# Chatter API
https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/intro_what_is_chatter_connect.htm

# How to run a the sample
- `sudo gem install dotenv`
- `cd examples && cp sample-env .env`
- fill out the params in .env file
- modify `post_text_with_mention` for `subject_id`, `text`, `mention_to` to use your objects
- run `dotenv ./sample.py`