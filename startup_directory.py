startups = {
        'Stripe': ['payments', 'infrastructure', 'fintech'],
        'OpenAI': ['AI', 'LLM', 'Sam Altman'],
        'Anthropic': ['AI', 'AI' 'LLM', 'AI Safety'],
        'Datadog': ['API Observability', 'Infra'],
        'Figma': ['Design', 'Browser'],
        'SpaceX': ['Space', 'Rockets'],
        'Scale AI': ['Datasets', 'Labeling'],
        'Meta': ['Social Networks', 'Instagram', 'Facebook'],
        'Anduril': ['War', 'Defense', 'AI'],
        'Vercel': ['Deploy', 'Web'],
        'Palantir': ['CIA', 'Gotham'],
        'Nvidia': ['Chips', 'GPU', 'AI'],
        'Apple': ['Steve Jobs', 'iPhone']
    }

def search(query: str) -> list[str]:
    result = []
    
    for n in startups:
        if n.lower() == query.lower():
            result.append(n)
            continue
        for param in startups[n]:
            if query.lower() in param.lower():
                result.append(n)
                break
    
    return result

print(search('a'))