# DESIGN

Possible approaches:

expansive view:
specify search period
Go to each sitting date, scrape all sittings, compile the whole corpus
parsing work: create database with text objects, identify speaker, root of 'exchange', type of exchange, people mentioned, people replying

Keyword view:
specify keyword and search period e.g. 'climate change'

Person view:
specify person and get a summary of said person, and what they talk about

	Trivial: word cloud of the 'title'
	more involved: keyBERT to identify keywords in each speech


# Goal?

- Make Hansard more searchable
- Answer question of: what did X MP say on Y topic
	- which MPs spoke less or not at all on Y topic, whose interests do they consider (question of interpretation)
- Cluster MPs by interest in topic?

Maybe impossible: trace the various lines of arguments for each policy? outline the issues?
isn't that just a summary

outline the key issues i.e. question, response, question response
i.e. what is in contention, and is the response sufficient / what does it hinge on
isn't this very nuanced then

the goal is then to focus on discovery and providing context by assuming that Parl speeches contain sufficient contextual information on bills etc


Question detector: "Person asked" or just use the first


Choice: solve the general approach first
Atomic object: finite text of speaker
Database: use SQLite

keys:
- name
- associated position
- date / sitting
- detected keywords using keyBERT
- title of exchange
- detected keywords from title of exchange
- special hash / ID
- related IDs e.g. before and after in time i.e. the initial question, replies, 
- root ID


maybe:
- keywords from chatgpt
gpt-3.5-turbo	$0.002 / 1K tokens

1M tokens for $2? worth


