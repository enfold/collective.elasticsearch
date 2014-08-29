

def BrainFactory(catalog):
    def factory(result):
        path = result.get('path', {}).get('path', None)
        if path:
            rid = catalog.uids.get(path)
            brain = catalog[rid]
            meta = result.get_meta()
            if 'highlight' in meta and 'SearchableText' in meta['highlight']:
                highlights = meta['highlight']['SearchableText']
                brain.eshighlight = highlights
            return brain
    return factory
