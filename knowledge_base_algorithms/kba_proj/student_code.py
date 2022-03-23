import read, copy
from util import *
from logical_classes import *

verbose = 0

class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules
        self.ie = InferenceEngine()

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def _get_fact(self, fact):
        """INTERNAL USE ONLY
        Get the fact in the KB that is the same as the fact argument

        Args:
            fact (Fact): Fact we're searching for

        Returns:
            Fact: matching fact
        """
        for kbfact in self.facts:
            if fact == kbfact:
                return kbfact

    def _get_rule(self, rule):
        """INTERNAL USE ONLY
        Get the rule in the KB that is the same as the rule argument

        Args:
            rule (Rule): Rule we're searching for

        Returns:
            Rule: matching rule
        """
        for kbrule in self.rules:
            if rule == kbrule:
                return kbrule

    def kb_add(self, fact_rule):
        """Add a fact or rule to the KB
        Args:
            fact_rule (Fact or Rule) - Fact or Rule to be added
        Returns:
            None
        """
        printv("Adding {!r}", 1, verbose, [fact_rule])
        if isinstance(fact_rule, Fact): # if this Fact|Rule is a fact
            if fact_rule not in self.facts: # and this is a new fact
                self.facts.append(fact_rule) # add it to the list of new facts 
                for rule in self.rules: # then loop through each of the rules and infer the creation/retraction of new ones 
                    self.ie.fc_infer(fact_rule, rule, self)
            else: # if this Fact|Rule is a fact AND this is not a new fact (aka an inferred or asserted fact)
                if fact_rule.supported_by: # is it supported by any rules or facts?
                    ind = self.facts.index(fact_rule) # if so, get the index of where this inferred fact is stored and
                    for f in fact_rule.supported_by: # for every fact that this inferred fact is supported by 
                        self.facts[ind].supported_by.append(f) # append it to the inferred fact's supported_by list in its place @ ind in the facts list
                else: # if this is not a new fact and its not supported it mustve been asserted
                    ind = self.facts.index(fact_rule)
                    self.facts[ind].asserted = True
        elif isinstance(fact_rule, Rule): # if this Fact|Rule is a rule, do the same thing as if it were a fact, but a few key differences
            if fact_rule not in self.rules: 
                self.rules.append(fact_rule)
                for fact in self.facts: # instead of inferring rules we infer facts
                    self.ie.fc_infer(fact, fact_rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.rules.index(fact_rule)
                    for f in fact_rule.supported_by: # still appending facts the rule (this time) is supported by
                        self.rules[ind].supported_by.append(f)
                else:
                    ind = self.rules.index(fact_rule)
                    self.rules[ind].asserted = True

    def kb_assert(self, fact_rule):
        """Assert a fact or rule into the KB

        Args:
            fact_rule (Fact or Rule): Fact or Rule we're asserting
        """
        printv("Asserting {!r}", 0, verbose, [fact_rule])
        self.kb_add(fact_rule)

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Statement to be asked (will be converted into a Fact)

        Returns:
            listof Bindings|False - list of Bindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        if factq(fact):
            f = Fact(fact.statement)
            bindings_lst = ListOfBindings()
            # ask matched facts
            for fact in self.facts:
                binding = match(f.statement, fact.statement)
                if binding:
                    bindings_lst.add_bindings(binding, [fact])

            return bindings_lst if bindings_lst.list_of_bindings else []

        else:
            print("Invalid ask:", fact.statement)
            return []

    def kb_retract(self, fact_rule):
        """Retract a fact or a rule from the KB

        Args:
            fact_rule (Fact or Rule) - Fact or Rule to be retracted

        Returns:
            None
        """

        printv("Retracting {!r}", 0, verbose, [fact_rule])
        ####################################################
        fr_shell = None
        if isinstance(fact_rule, Rule):
            for rule in self.rules:
                if fact_rule == rule:
                    fr_shell = rule
                    break
        else:
            for fact in self.facts:
                if fact_rule == fact:
                    fr_shell = fact
                    break

        if len(fr_shell.supported_by) == 0:
            if fr_shell.name == "rule":
                self.rules.remove(fr_shell)
            elif fr_shell.name == "fact":
                self.facts.remove(fr_shell)

            for rule in fr_shell.supports_rules:
                for pair in rule.supported_by:
                    if fr_shell in pair:
                        rule.supported_by.remove(pair)
                if len(rule.supported_by) == 0:
                    self.kb_retract(rule)

            for fact in fr_shell.supports_facts:
                for pair in fact.supported_by:
                    if fr_shell in pair:
                        fact.supported_by.remove(pair)
                if len(fact.supported_by) == 0:
                    self.kb_retract(fact)









class InferenceEngine(object):
    def fc_infer(self, fact, rule, kb):
        """Forward-chaining to infer new facts and rules

        Args:
            fact (Fact) - A fact from the KnowledgeBase
            rule (Rule) - A rule from the KnowledgeBase
            kb (KnowledgeBase) - A KnowledgeBase

        Returns:
            Nothing
        """
        printv('Attempting to infer from {!r} and {!r} => {!r}', 1, verbose,
            [fact.statement, rule.lhs, rule.rhs])
        ####################################################
        
        substitutions = match(fact.statement, rule.lhs[0]) # test match function to be sure, statements w/o vars always output false
        if substitutions: #if a matching exists aka if substitution found
            if len(rule.lhs) == 1: #if lhs has only 1 statement
                rhs_copy = rule.rhs #copy rhs so rule original rule isn't overwritten
                rhs_copy = instantiate(rhs_copy, substitutions)
                #support_copy = fact.supported_by + rule.supported_by
                #support_copy.append([fact, rule]) # test if supported_by is like this: [[f1,r1]...[fn,rn]]
                new_fact = Fact(rhs_copy, [[fact, rule]])
                fact.supports_facts.append(new_fact)
                rule.supports_facts.append(new_fact)
                #kb.facts.append(new_fact)
                kb.kb_add(new_fact)
            else:
                rhs_copy = rule.rhs #copy rhs so rule original rule isn't overwritten
                rhs_copy = instantiate(rhs_copy, substitutions)
                lhs_copy = []
                for statement in rule.lhs:
                    shell = instantiate(statement, substitutions)
                    lhs_copy.append(shell)
                #support_copy = fact.supported_by + rule.supported_by
                #support_copy.append([fact, rule]) # test if supported_by is like this: [[f1,r1]...[fn,rn]]
                new_rule_array = []
                new_rule_array.append(lhs_copy[1:]) # assuming [1:] means 1 to the end of arr
                new_rule_array.append(rhs_copy)
                new_rule = Rule(new_rule_array, [[fact, rule]])
                fact.supports_rules.append(new_rule)
                rule.supports_rules.append(new_rule)
                #kb.rules.append(new_rule)
                kb.kb_add(new_rule)

