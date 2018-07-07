## Script (Python) "unsub_scr"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

# The unsubscriber will be the currently authorized user, if there is one. If not, we use the wid.

# This is who we're operating on
person_id = request['wid']

# unsub_id is who is doing the operating. Defaults to the indicated person,
# but will be overridden if being done by someone logged in. This allows us
# to track changes made by staff.

unsub_id = request['wid']
username = str(request.AUTHENTICATED_USER)

if username[ :len('Anonymous')] != 'Anonymous':
    userdata = context.get_userdata_sql(username=username).dictionaries()[0]
    unsub_id = userdata['person_id']

def unsub_selected():
    if request.has_key('subs'):
	for sub in request.subs:
	    if sub.has_key('checkbox'):
		context.zunsub.unsub_list_sql(person_id=person_id, list_id=sub['id'],
		    unsubber_id=unsub_id)

def unsub(level=1):
    cur = context.zunsub.get_current_unsub_status_sql(person_id=person_id)

    if cur:
        context.zunsub.unsub_general_update_sql(person_id = person_id, level=level, unsubber_id=unsub_id)
    else:
        context.zunsub.unsub_general_insert_sql(person_id = person_id, level=level, unsubber_id=unsub_id)


def unsub_general():
    unsub()

def unsub_all():
    unsub(level=2)

types = {'Unsubscribe Me From The Selected Lists Only':unsub_selected,
'Unsubscribe Me From General Mailings':unsub_general,
'Permanently Unsubscribe Me':unsub_all}

action = request.action

types[action]()

RESPONSE.redirect('general_message.html?title=Unsubscribed&msg=Unsubscribe%20Successful')
 
 


