ACCESS_TOKEN = 'EAAIM2ymqBYwBAC1AdFaH9A8GLCfNF53tLWGWT2ZCrTuz3pCac833ZCsXFfCFfCC0a8yzwqKrgobCTYKMNlhtxUzsO4i3ZAXBUZCLFnmTRiq40zgM' \
               'TMIrZAsyCF1YOgl4zZBLZA2OoZB5Mpu78UuqNtYznfUZCZAEUQeazbxbv1WZCqixDZAWPjEDclKr0bCodXC6WpvGXCZAOS62MZCZCF0ZAfOObiPzjJc3BudGzGGLDAUDrLwhMwZDZD'

import facebook
page_access_token = ACCESS_TOKEN
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = "2723663517714234"

graph.put_object(facebook_page_id, "feed", message='Hello Python API')

l=[1,2,3]
l.__all