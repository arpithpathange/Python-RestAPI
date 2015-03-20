RESOURCE_METHODS = ['GET', 'POST']


'''
DOMAIN = {
        'user': {
            'schema':{
                'firstname':{
                    'type':'string'
                },
                'lastname':{
                    'type':'string'
                }
            },

          'additional_lookup': {
              'url': 'regex("[\w]+")',
              'field': 'firstname',
              }
        }
}'''


DOMAIN = {
    'user': {
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'firstname',
            },
        'schema': {
            'firstname': {
                'type': 'string'
            },
            'lastname': {
                'type': 'string'
            },
        }
    }
}