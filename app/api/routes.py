from fastapi import APIRouter
from app.parsers.aws_iam import parse_iam_policy, extract_privileged_actions
from app.engine.escalation_detector import detect_escalation
from app.engine.risk_scoring import calculate_risk_score
from app.reports.generator import generate_report

router = APIRouter()

@router.post("/analyze/aws")
def analyze_aws(identity: str, policy_json: str):
    policy = parse_iam_policy(policy_json)
    actions = extract_privileged_actions(policy)
    findings = detect_escalation(actions)
    risk = calculate_risk_score(findings)

    return generate_report(identity, findings, risk)
