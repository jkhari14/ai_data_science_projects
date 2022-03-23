from bayesnet import BayesNet, BayesNode
import copy
import itertools

def partition(arr, bnnodes, bnnames, low, high):
    i = (low-1)         
    pivot = arr[high]     
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            bnnodes[i], bnnodes[j] = bnnodes[j], bnnodes[i]
            bnnames[i], bnnames[j] = bnnames[j], bnnames[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    bnnodes[i+1], bnnodes[high] = bnnodes[high], bnnodes[i+1]
    bnnames[i+1], bnnames[high] = bnnames[high], bnnames[i+1]
    return (i+1)

def quickSort(arr, bnnodes, bnnames, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, bnnodes, bnnames, low, high)
        quickSort(arr, bnnodes, bnnames, low, pi-1)
        quickSort(arr, bnnodes, bnnames, pi+1, high)
'''
def prob_generator(bn, evidenceList, evidenceDict, bN, inv):
	parent_fill_in = 0
	missing_parents = []
	parent_prob_rec_multiplier = 1
	
	if bn.get_var(evidenceList[0]).parents == None:
		if not inv:
			return bn.get_var(evidenceList[0]).probability(evidenceDict[evidenceList[0]], evidenceDict) 
		else: 
			return bn.get_var(evidenceList[0]).probability(not evidenceDict[evidenceList[0]], evidenceDict)
	for parent in bn.get_var(evidenceList[0]).parents:
		if parent not in evidenceDict:
			parent_fill_in += 1
			missing_parents.append(parent)

	if parent_fill_in == 0:
		if not inv:
			return bn.get_var(evidenceList[0]).probability(evidenceDict[evidenceList[0]], evidenceDict) 
		else: 
			return bn.get_var(evidenceList[0]).probability(not evidenceDict[evidenceList[0]], evidenceDict)

	missing_parent_bool_table = list(itertools.product([False, True], repeat = parent_fill_in))
	prob_acc = 0
	for row in missing_parent_bool_table:
		evidenceDict_copy = evidenceDict.copy()
		for bit in range(len(row)):
			evidenceDict_copy[missing_parents[bit]] = row[bit]
		if not inv:
			prob_acc += bn.get_var(evidenceList[0]).probability(evidenceDict[evidenceList[0]], evidenceDict_copy) # * parent_prob_rec_multiplier
			
		else: 
			prob_acc += bn.get_var(evidenceList[0]).probability(not evidenceDict[evidenceList[0]], evidenceDict_copy) # * parent_prob_rec_multiplier
	return prob_acc

def recurse(bn, evidenceDict, evidenceList, hypothesisprobList, bN):
	if len(evidenceList) == 0:
		return
	elif evidenceList[0] not in evidenceDict:
		evidence_dict_copy = evidenceDict.copy()
		evidence_dict_copy[evidenceList[0]] = True
		pos_and_neg_hyp = prob_generator(bn, evidenceList, evidence_dict_copy, bN, True) + prob_generator(bn, evidenceList, evidence_dict_copy, bN, False)
		hypothesisprobList.append(pos_and_neg_hyp)
		recurse(bn, evidenceDict, evidenceList[1:], hypothesisprobList, bN[1:])
	else:
		hypothesisprobList.append(prob_generator(bn, evidenceList, evidenceDict, bN, False))
		recurse(bn, evidenceDict, evidenceList[1:], hypothesisprobList, bN[1:])
'''
def recurse2(bn, evidenceDict, evidenceList):
	if len(evidenceList) == 0:
		return 1
	elif evidenceList[0] not in evidenceDict:
		# print(evidenceList[0], evidenceDict)
		evidence_dict_copy = evidenceDict.copy()
		evidence_dict_copy2 = evidenceDict.copy()
		evidence_dict_copy[evidenceList[0]] = True
		evidence_dict_copy2[evidenceList[0]] = False
		return (bn.get_var(evidenceList[0]).probability(True, evidence_dict_copy) * recurse2(bn, evidence_dict_copy, evidenceList[1:])) + (bn.get_var(evidenceList[0]).probability(False, evidence_dict_copy2) * recurse2(bn, evidence_dict_copy2, evidenceList[1:]))
	else:
		# print(evidenceList[0], evidenceDict)
		return bn.get_var(evidenceList[0]).probability(evidenceDict[evidenceList[0]], evidenceDict) * recurse2(bn, evidenceDict, evidenceList[1:])

def ask(var, value, evidence, bn):
	print('\n')
	print('\n')
	print("new test")
	evidence[var] = value
	parent_score = {}
	for node in bn.variables:
		if node.parents == None:
			parent_score[node.name] = 1
		else:
			parent_score[node.name] = len(node.parents)
	for node in bn.variables:
		if node.parents != None:
			for parent in node.parents:
					parent_score[node.name] += parent_score[parent]
	pss_arr = []
	for name in bn.variable_names:
		pss_arr.append(parent_score[name])
	quickSort(pss_arr, bn.variables, bn.variable_names, 0, len(bn.variables) - 1)

	bn_variable_names = bn.variable_names.copy()
	p = recurse2(bn, evidence, bn_variable_names)

	bn_variable_names = bn.variable_names.copy()
	evidence[var] = not value
	n = recurse2(bn, evidence, bn_variable_names)

	return p/(p + n)









