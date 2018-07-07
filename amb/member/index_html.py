## Script (Python) "index_logged_in"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
# Example code:

# Import a standard function, and get the HTML request and response objects.
from Products.PythonScripts.standard import html_quote
request = container.REQUEST
RESPONSE =  request.RESPONSE

res = context.get_userid_sql(username=request.AUTHENTICATED_USER)

userid = res.dictionaries()[0]['id']
context.update_amb_login_sql(person_id=userid)

# The purpose of this script is to plant the wid & cpid cookies of the
# ambassador on his own computer. The idea being that if someone else signs
# up from their machine, the wid used will be the ambassador's.

username = request.AUTHENTICATED_USER
userdata = context.get_userdata_sql(username=username).dictionaries()[0]
wid = userdata['person_id']
cpid = context.get_default_amb_cpid()

expiry = str((DateTime()+(90)).strftime("%A, %d-%b-%Y 12:00:00 GMT"))

RESPONSE.appendHeader('Set-Cookie', 'wid=%s; path=/; expires=%s' % (wid,expiry))
RESPONSE.appendHeader('Set-Cookie', 'cpid=%s; path=/; expires=%s' % (cpid,expiry))


# simply check whether the payee has been set yet or not
ambassador = context.get_ambassador_by_personid_sql(person_id=wid).dictionaries()[0]

if ambassador['payee'] == None:
    RESPONSE.redirect("/amb/member/payee/")

else: RESPONSE.redirect('index_logged_in')
 
 


