def generate_report(identity, escalation_findings, risk_level):
    return {
        "identity": identity,
        "escalation_paths": escalation_findings,
        "risk_level": risk_level
    }
