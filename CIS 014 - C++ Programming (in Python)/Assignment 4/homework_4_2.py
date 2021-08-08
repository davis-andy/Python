def deduplicate(inp: str) -> str:









def main():
    print(deduplicate("AABB"))  # should output "Empty"
    print(deduplicate("A"))  # "A"
    print(deduplicate("ABBA"))  # should output "Empty"
    print(deduplicate("AAA"))  # "A"
    print(deduplicate("AKA"))  # "AKA" because there is no consecutive pair.