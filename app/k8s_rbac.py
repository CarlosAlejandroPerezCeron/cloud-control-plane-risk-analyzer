import yaml

def parse_k8s_rbac(yaml_content):
    data = yaml.safe_load(yaml_content)
    rules = data.get("rules", [])

    risky = []
    for rule in rules:
        if "*" in rule.get("verbs", []):
            risky.append("Wildcard verb detected")

        if "cluster-admin" in str(rule):
            risky.append("Cluster-admin level rule")

    return risky
