expand_count = 0

def expand(node, _map):
	global expand_count
	print(node)
	expand_count = expand_count + 1
	return [next for next in _map[node] if _map[node][next] is not None] # returns list of every key pair in the node array of key pairs that has an existing value i.e. is not None.  
# does this function return a full fledged list?