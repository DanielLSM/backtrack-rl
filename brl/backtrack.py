from brl.csp import CSPSchedule, Variable, Constraint, Schedule
from brl.tree import Node


class BacktrackSchedule:
    def __init__(self, csp, start_assign, *args, **kwargs):
        assert isinstance(csp, CSPSchedule), "problem is not CSP"
        assert isinstance(start_assign, Schedule), "assignment is not valid"
        self.csp = csp
        self.start_assign = start_assign

    #TODO
    def solve(self, schedule_assign):
        if self.csp.satisfied_assignment(schedule_assign):
            return schedule_assign

        var = self.csp.select_next_var(schedule_assign)
        if not var: return None

        value = self.csp.select_next_value(schedule_assign, var)


class BacktrackTreeDFS:
    def __init__(self, csp, start_assign, *args, **kwargs):
        assert isinstance(csp, CSPSchedule), "problem is not CSP"
        assert isinstance(start_assign, Schedule), "assignment is not valid"
        self.csp = csp
        # self.start_assign = start_assign
        self.root = Node(start_assign)

    def solve(self, node_schedule):
        if self.csp.satisfied_assignment(node_schedule.assignment):
            return node_schedule

        next_var = self.csp.select_next_var(node_schedule.assignment)
        if next_var == None:
            return None

        # here when we expand the childs, we need to fix domain
        for child in node_schedule.expand_no_heuristic(
                self.csp, node_schedule.assignment, next_var):
            next_node = self.solve(child)

            return next_node

        var = self.csp.select_next_var(schedule_assign)
        if not var: return None

        value = self.csp.select_next_value(schedule_assign, var)


if __name__ == "__main__":
    csp = CSPSchedule
    print("put sad wings around me now")

    # bb = BacktrackSchedule()