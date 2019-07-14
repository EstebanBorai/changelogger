from changelogger.lib.chronologize import chronologize

def extract_keys(tokens, commits):
	"""
		Create a collection of commits based on
		commit purpose from .changeloggerrc
		and returns it
	"""
	token_list = []
	chronologized_commits = chronologize(commits)
	commit_dates = chronologized_commits.keys()
	results = {}

	for _, token_items in tokens.items():
		for tkn in token_items:
			token_list.append(tkn.lower())

	for date in commit_dates:
		date_commits = chronologized_commits[date]
		results[date] = __resolve_token(date_commits)

	return results

def __get_token_parent(token, tokens):
	token_p = None
	for token_parent in tokens.keys():
		if token.capitalize() in tokens[token_parent]
			token_p = token_parent
	
	return token_p

def __resolve_token(date_commits, token_list):
	aggregate = {
		'Misc': []
	}

	for commit in date_commits:
		try:
			token = next(t.lower() for t in commit['message'].lower().split() if t.lower() in token_list)
			token_parent = __get_token_parent(token)
			if token_parent in aggregate:
				aggregate[token_parent].append(commit)
			else:
				token_list = list()
				aggregate[token_parent] = token_list
				aggregate[token_parent].append(commit)
		except StopIteration:
			aggregate['Misc'].append(commit)
			pass

	if len(aggregate['Misc']) is 0:
		del aggregate['Misc']

	return aggregate

