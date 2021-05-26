from LoginRadius import LoginRadius as LR
API_KEY = "a6fca4bf-efce-4686-8422-0b6f4889223e"
API_SECRET = "9b35be14-a44f-4fc9-9d30-33ef1f893281"

LR.API_KEY = API_KEY
LR.API_SECRET = API_SECRET
loginradius = LR()   
LR.API_REQUEST_SIGNING = True