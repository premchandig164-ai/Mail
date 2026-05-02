import random, string

base = "yourgmail"  # put your gmail username here, no @, no dots

def dot_variant():
    chars = list(base)
    positions = list(range(1, len(chars)))
    dots = sorted(random.sample(positions, random.randint(1, min(4, len(positions)))))
    result = []
    for i, c in enumerate(chars):
        if i in dots:
            result.append('.')
        result.append(c)
    return ''.join(result) + "@gmail.com"

def plus_variant():
    tag = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{base}+{tag}@gmail.com"

print("=== DOT VARIANTS ===")
for _ in range(10):
    print(dot_variant())

print("\n=== PLUS VARIANTS ===")
for _ in range(10):
    print(plus_variant())
