import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('keyjsonfile.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'databaseURL'
})

i =1
while (i ==1):

	THERAPRUTIQUE = input('CLASSE THERAPRUTIQUE')
	
	PHARMACOLOGIQUE = input('CLASSE PHARMACOLOGIQUE')
	NOM = input('NOM')
	DCI= input('DCI')
	FORME = input('FORME')
	CONDITIONNEMENT= input('CONDITIONNEMENT')
	TYPE = input('TYPE')
	REMBOURSABLE = input('REMBOURSABLE')
	TARIF = input('TARIF')
	LABORATOIRE = input('LABORATOIRE')
	PAYS = input('PAYS')
	IMG = input('IMG')
	NOTES = input('NOTES')
	
	ref = db.reference('/dawadz')
	ref.push({
		        		'CLASSE THERAPRUTIQUE':THERAPRUTIQUE,
		        		'CLASSE PHARMACOLOGIQUE':PHARMACOLOGIQUE,
		        		'NOM':NOM,
		        		'DCI':DCI,
		        		'FORME':FORME,
		        		'CONDITIONNEMENT':CONDITIONNEMENT,
		        		'TYPE':TYPE,
		        		'REMBOURSABLE':REMBOURSABLE,
		        		'TARIF':TARIF,
		        		'LABORATOIRE':LABORATOIRE,
		        		'PAYS':PAYS,
		        		'IMG':IMG,
		        		'NOTES':NOTES
		        })

	i = input('NEXT PRESS 1 ELSE QUIT')
		        
		        

