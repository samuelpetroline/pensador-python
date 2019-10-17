
# pensador-python

Python library to query quotes from https://www.pensador.com/

Created for studying purposes

# How to use

    import pensador
    
    query = pensador.Pensador()
	
	# to search by something
	quote_list = query.quote('amor')  

	# you can search by whole phrases
	quote_list = query.quote('sentido da vida')

	# you can paginate and set a quote limit per page
	quote_list = query.quote('amizade', page=2, limit=8)

	# and you can search by an specific author
	quote_list = query.author('José Saramago')
	

# This is a work in progress

Please feel free to discuss new features and changes to the existing codebase.

