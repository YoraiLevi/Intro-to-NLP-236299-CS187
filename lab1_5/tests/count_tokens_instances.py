test = {   'name': 'count_tokens_instances',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> tokens = tokenizer.encode(geah[0]['text']).tokens;\n>>> all([count_tokens_instance(geah[0], word) > 0 for word in tokens])\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
