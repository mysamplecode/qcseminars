## Script (Python) "new_password_scr"
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

import random, crypt

pd = context.get_person_by_email_sql(email=request.email)
if not pd:
    RESPONSE.redirect("general_message.html?title=No Such Email&msg=This email doesn't appear in our database")
    return

pd = pd.dictionaries()[0]
ud = context.get_userdata_sql(person_id=pd['id'])

if not ud:
    RESPONSE.redirect("general_message.html?title=No Such User&msg=There is no user with this email in our database")
    return
ud = ud.dictionaries()[0]

newpass = int(random.random()*1000000)
#print "New password: %s" % newpass
#return printed
args = {}
args['person_id'] = pd['id']
args.update(ud)
args['password'] = newpass

password = crypt.crypt(str(newpass),args['username'][:2])
context.change_password_sql(person_id=args['person_id'], password=password,
    modifier_id=args['person_id'])

#bbsargs = {}
#bbsargs['id'] = str(args['person_id'])
#context.action_handler('VerifyPHPBB',bbsargs)
#

context.send_mail_by_id_scr(email_id=14, args=args)
RESPONSE.redirect('pass_sent_html')
 
 


