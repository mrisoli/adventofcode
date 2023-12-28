type Rule = [str]
type Workflow = dict[str, [Rule]]

def get_rule(rule: str) -> Rule:
    rs = rule.split(':')
    if len(rs) == 1:
        rs.insert(0, '1')
    return rs

def get_workflow(ws: str) -> Workflow:
    name, rules = ws[:-1].split('{')
    return (name, [get_rule(r) for r in rules.split(',')])

def gen_workflows(ws: str) -> Workflow:
    return dict([get_workflow(w) for w in ws.split('\n')])
