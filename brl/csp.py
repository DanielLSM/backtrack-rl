class Constraint:
    def __init__(self, info, *args, **kwargs):
        self._info = info

    def satisfied(self, assignment):
        raise NotImplementedError

    def consistent(self, assignment):
        raise NotImplementedError


class Variable:
    def __init__(self, domain, info, *args, **kwargs):
        self.domain = domain
        self._info = info

    def get_info(self):
        return self._info


class Assignment:
    def __init__(self, vars, *args, **kwargs):
        self.vars = vars
        self.assignment = dict.fromkeys(vars)
        self.vars_domain = {var: var.domain for var in vars}

    def assign(self, var, value):
        self.assignment[var] = value
        self.vars_domain[var] = value

    def get_value(self, var):
        return self.assignment[var]

    def get_domain(self, var):
        return self.vars_domain[var]

    def restrict_domain(self, var, dom):
        self.vars_domain[var] = dom

    def __len__(self):
        return len(list(self.assignment.keys()))


class Schedule(Assignment):
    def __init__(self, vars, *args, **kwargs):
        super().__init__(self, vars, *args)

    def render(self):
        raise NotImplementedError


class CSP:
    def __init__(self, vars, constraints, *args, **kwargs):
        self.vars = vars
        self.constraints = constraints  #maps vars to constraints

    def change_domain(self, assignment, var):
        domain = assignment.get_domain(var)
        assert len(domain) != 0
        return domain

    def satisfied_assignment(self, assignment):
        assert len(self.vars) == len(assignment), "variables mismatch"
        for constraint in self.constraints:
            if not constraint.satisfied():
                return False
        return True

    def consistent_assignment(self, assignment, var):
        for constraint in self.constraints:
            if not constraint.consistent_assignment:
                return False
        return True


class CSPCalendar(CSP):
    def __init__(self, vars, domains, constraints, *args, **kwargs):
        super().__init__(self, vars, domains, constraints)


if __name__ == "__main__":
    print("hello")
