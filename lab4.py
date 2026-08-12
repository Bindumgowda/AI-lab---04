class RuleBasedSystem:
    def __init__(self, facts, rules):
        # Store facts in a set to ensure unique elements
        self.facts = set(facts)
        self.rules = rules

    def forward_chain(self):
        iterations = 0
        while True:
            new_fact_added = False
            for rule in self.rules:
                # Check if all 'if' conditions exist in current facts
                if all(cond in self.facts for cond in rule['if']):
                    if rule['then'] not in self.facts:
                        print(f"Rule Triggered: IF {rule['if']} THEN Add {rule['then']}")
                        self.facts.add(rule['then'])
                        new_fact_added = True
            
            # Stop if no new facts were added during the iteration
            if not new_fact_added:
                break
            iterations += 1
            
        return self.facts


# Example Execution
if __name__ == "__main__":
    # Define initial facts
    initial_facts = ['Socrates_is_human', 'All_humans_are_mortal']
    
    # Define production rules
    production_rules = [
        {
            'if': ['Socrates_is_human', 'All_humans_are_mortal'],
            'then': 'Socrates_is_mortal'
        }
    ]
    
    # Initialize and execute forward chaining
    rbs = RuleBasedSystem(initial_facts, production_rules)
    print("Initial Facts:", initial_facts)
    final_kb = rbs.forward_chain()
    print("Final Knowledge Base Facts:", final_kb)