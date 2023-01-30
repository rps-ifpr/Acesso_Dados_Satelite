import earthaccess

earthaccess.__version__

from earthaccess import Auth, Store, DataCollections, DataGranules
auth = Auth()

auth.login(strategy="interactive", persist=True)

a = auth.login(strategy="environment")
# are we authenticated?
print(auth.authenticated)