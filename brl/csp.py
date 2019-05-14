class Constraint:
    def __init__(self, *args, **kwargs):
        pass


class Variable:
    def __init__(self, name, domain, *args, **kwargs):
        self.name = name
        self.domain = domain
        self.info = args


class Assignment:
    def __init__(self, vars, *args, **kwargs):
        self.vars = vars
        self.assignment = dict.fromkeys(vars)
        self.vars_domain = {var: var.domain for var in vars}

    def assign(self, var, value):
        self.assignment[var] = value

    def getValue(self, var):
        return self.assignment[var]

    def getDomain(self, var):
        return self.vars_domain[var]

    def restrictDomain(self, var, dom):
        self.vars_domain[var] = dom


class Schedule(Assignment):
    def __init__(self, vars, *args, **kwargs):
        super().__init__(self, vars, *args)

    def render(self):
        pass


class CSP:
    def __init__(self, vars, domains, constraints, *args, **kwargs):
        self.vars = vars
        self.constraints = constraints  #maps vars to constraints
        self.domains = domains  #maps vars to domains


class CSPCalendar(CSP):
    def __init__(self, vars, domains, constraints, *args, **kwargs):
        super().__init__(self, vars, domains, constraints)


if __name__ == "__main__":
    print("hello")
