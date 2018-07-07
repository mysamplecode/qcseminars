## Script (Python) "add_to_cart"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
# arch-tag: 4373ead8-c22d-4c82-adc0-99b78eead137

request = container.REQUEST
RESPONSE =  request.RESPONSE


def make_arg_dict(urlargs):
    parts = urlargs.split("&")
    nd = {}
    for p in parts:
        (l, r) = p.split("=")
        nd[l] = r
    return nd

if request.has_key('el'):
    # Encrypted Link
    try:
	elargs = make_arg_dict(context.html_decrypt(request['el']))
	receipt = context.get_receipt_sql(elargs).dictionaries()[0]
	body = receipt['body']
	bcl = ""
	if receipt['is_archived']:
	    bcl = """class="void" """
	print "<body>"
	print """<table width='100%%'><tr><td align='center'>"""
	print "<table style='border: thin solid black'><tr><td %s>" % bcl
	print body
	print """</td></tr></table></td></tr>
	<tr><td align='center'>Receipt #%(receipt_id)s</td></tr></table>""" %\
	receipt
	print "</body>"
    except Exception, e:
	print "Got a problem: %s." % e
else:
    print "Error - Invalid Parameter"


return printed

