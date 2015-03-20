from eve import Eve
from eve.auth import BasicAuth

class Authenticate(BasicAuth):
    def check_auth(self, firstname, lastname, allowed_roles, resource,
                   method):
        print resource
        print method
        if resource == 'user' and method == 'GET':
            user = app.data.driver.db['user']
            print user
            user = user.find({'firstname': firstname})
            print 'GET'
            if user:
                print 'user is true'
                return True
            else:
                print 'user is false'
                return False
        elif resource == 'user' and method == 'POST':
            print firstname
            print lastname
            #return username == 'admin' and password == 'password'
            return True
        else:
            return True


#app = Eve()

if __name__ == '__main__':
    app = Eve(auth=Authenticate)
    app.run()