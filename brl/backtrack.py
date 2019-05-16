from brl.csp import CSPSchedule, Variable, Constraint, Schedule


class BacktrackSchedule:
    def __init__(self, csp, start_assign, *args, **kwargs):
        assert isinstance(csp, CSPSchedule), "problem is not CSP"
        assert isinstance(start_assign, Schedule), "assignment is not valid"
        self.csp = csp
        self.start_assign = start_assign

    def solve(self, assign):
        if self.csp.satisfied_assignment(assign):
            return assign

        var = self.csp.select_next_var(assign)
        if not var: return None

        value = self.csp.select_next_value(assign, var)


if __name__ == "__main__":
    csp = CSPSchedule
    print("put sad wings around me now")

    # bb = BacktrackSchedule()