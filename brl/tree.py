# Welcome to the first tree-search implementation for CSP's on the internet
from brl.csp import CSPSchedule, Variable, Constraint, Schedule


class Node:
    def __init__(self,
                 assignment,
                 parent=None,
                 action_var=None,
                 action_value=None):
        self.assignment = assignment  #state of the world
        self.parent = parent
        self.action_var = action_var
        self.action_value = action_value

    def __repr__(self):
        return "Node {}={}".format(self.action_var, self.action_value)

    # we need to fix domain here
    def expand_no_heuristic(self, csp, assignment, action_var):
        return [
            self.child_node(csp, assignment, action_var, action_value)
            for action_value in assignment.vars_domain[action_var]
        ]

    def child_node(self, csp, assignment, action_var, action_value):
        next_assignment = csp.do_next_assignment(assignment, action_var,
                                                 action_value)
        return Node(next_assignment, self, action_var, action_value)
