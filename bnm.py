def get_categories(json_data):
    all_categories = []
    if 'text_has_categorie' in json_data['@relations']:
        categories = json_data['@relations']['text_has_categorie']
        for c in categories:
            if 'displayName' in c:
                all_categories.append( c['displayName'].lower() )
    return all_categories

def get_locations(json_data):
    all_locations = []
    if 'textdrager_has_lokalisering' in json_data['@relations']:
        locations = json_data['@relations']['textdrager_has_lokalisering']
        for l in locations:
            if 'displayName' in l:
                all_locations.append( l['displayName'].lower() )
    return all_locations


def get_bibliography(json_data):
    refs = []
    if 'textdrager_has_doc' in json_data['@relations']:
        for r in json_data['@relations']['textdrager_has_doc']:
            ref = []
            ref.append( r.get('preText',''))
            ref.append( r.get('displayName',''))
            ref.append( r.get('postText',''))
            refs.append( ref )
    return refs


def get_languages(json_data):
    all_lang = []
    if 'text_has_language' in json_data['@relations']:
        languages = json_data['@relations']['text_has_language']
        for l in languages:
            if 'displayName' in l:
                all_lang.append( l['displayName'].lower() )
    return all_lang

def get_owners(json_data):
    all_owners = []
    if 'textdrager_has_owner' in json_data['@relations']:
        owners = json_data['@relations']['textdrager_has_owner']
        for o in owners:
            if 'displayName' in o:
                all_owners.append( o['displayName'] )
    return all_owners

def get_copyists(json_data):
    all_copyists = []
    if 'textdrager_has_kopiist' in json_data['@relations']:
        copyists = json_data['@relations']['textdrager_has_kopiist']
        #print(copyists)
        for c in copyists:
            if c['relationTypeId'] != 'RELT000000000011':
                print( c['relationTypeId']  )
            if 'displayName' in c:
                all_copyists.append( c['displayName'] )
    return all_copyists

def get_norm_title(json_data):
    all_norm_title = []
    if 'text_has_norm_title' in json_data['@relations']:
        norm_title = json_data['@relations']['text_has_norm_title']
        #print(copyists)
        for t in norm_title:
            if 'displayName' in t and 'id' in t:
                all_norm_title.append( (t['id'],t['displayName']) )
    return all_norm_title


def get_authors(json_data):
    all_authors = []
    if 'tekstdragerHasTextOfAuthor' in json_data['@relations']:
        authors = json_data['@relations']['tekstdragerHasTextOfAuthor']
        for a in authors:
            if 'displayName' in a:
                all_authors.append( (a['id'],a['displayName']) )
    return all_authors

def get_binders(json_data):
    all_binders = []
    if 'textdrager_has_binder' in json_data['@relations']:
        binders = json_data['@relations']['textdrager_has_binder']
        for b in binders:
            if 'displayName' in b:
                all_binders.append( b['displayName'])
    return all_binders


def get_texts(json_data):
    text_ids = []
    if 'contains_text' in json_data['@relations']:
        for t in json_data['@relations']['contains_text']:
            text_ids.append( (t['id']) )
    return text_ids


def get_text_carrier(json_data):
    carriers = []
    if 'text_part_of' in json_data['@relations']:
        for c in json_data['@relations']['text_part_of']:
            carriers.append( (c['id'],c['displayName']) )
    return carriers


def get_annotations(json_data):
    notes = []

    labels = ['annotatie_colofon',
              'annotatie_inhoud',
              'annotatie_datering',
              'annotatie_incipit',
              'annotatie_materiaal',
              'annotatie_overig',
              'annotatie_rel__gr_kl',
              'annotatie_schrift' ]
    
    for l in labels:
        if l in json_data and json_data[l] is not None:
            for n in json_data[l]:
                notes.append(n)
          
    return notes 


def get_annotatie_materiaal(json_data):
    notes = []
    if 'annotatie_materiaal' in json_data and json_data['annotatie_materiaal'] is not None:
        for n in json_data['annotatie_materiaal']:
            notes.append(n)
    return notes 



def get_annotatie_colofon(json_data):
    notes = []
    if 'annotatie_colofon' in json_data and json_data['annotatie_colofon'] is not None:
        for n in json_data['annotatie_colofon']:
            notes.append(n)
    return notes 


def get_annotatie_datering(json_data):
    notes = []
    if 'annotatie_datering' in json_data:
        for n in json_data['annotatie_datering']:
            notes.append(n)
    return notes 


def get_overige_hs_aanduiding(json_data):
    notes = []
    if 'overige_hs_aanduiding' in json_data and json_data['overige_hs_aanduiding'] is not None:
        for n in json_data['overige_hs_aanduiding']:
            notes.append(n)
    return notes 


def intersection(list1, list2):
    intersection = [value for value in list1 if value in list2]
    return intersection


def get_localisering(json_data):
    locations = []
    if 'textdrager_has_lokalisering' in json_data['@relations']:
        for l in json_data['@relations']['textdrager_has_lokalisering']:
            value = l['displayName']
            if 'refType' in l and l.get('refType') == "ebnmlexicon_institute":
                locations.append( value )
    return locations


def get_owners_id(json_data):
    all_owners = []
    if 'textdrager_has_owner' in json_data['@relations']:
        owners = json_data['@relations']['textdrager_has_owner']
        for o in owners:
            if 'id' in o:
                all_owners.append( o['id'] )
    return all_owners