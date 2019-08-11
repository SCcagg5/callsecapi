from Model.basic import check
from Object.evts import evts


def check_method(cn, nextc):
    err = check.contain(cn.pr, ["method"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    err = evts.check_method(cn.pr["method"])
    return cn.call_next(nextc, err)

def call_sec(cn, nextc):
    err = check.contain(cn.pr, ["url"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    err = evts.call(cn.pr["url"], cn.pr["method"], cn.pr["data"] if check.contain(cn.pr, ["data"])[0] else None)
    return cn.call_next(nextc, err)
