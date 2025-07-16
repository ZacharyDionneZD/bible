import chapiters_table_generator
import chapiter_generator
from string import Template

class Book:
	def __init__(self, path, name, table_output_path, chapiter_output_path_template):
		self.path = path
		self.name = name
		self.table_output_path = table_output_path
		self.chapiter_output_path_template = chapiter_output_path_template

books = [
	Book("livres/genese.html", "Genèse", "www/genese/index.html", Template("www/genese/$chapiter_number/index.html")),
	Book("livres/exode.html", "Exode", "www/exode/index.html", Template("www/exode/$chapiter_number/index.html")),
	Book("livres/levitique.html", "Lévitique", "www/levitique/index.html", Template("www/levitique/$chapiter_number/index.html")),
	Book("livres/nombres.html", "Nombres", "www/nombres/index.html", Template("www/nombres/$chapiter_number/index.html")),
	Book("livres/deuteronome.html", "Deutéronome", "www/deuteronome/index.html", Template("www/deuteronome/$chapiter_number/index.html")),
	Book("livres/josue.html", "Josué", "www/josue/index.html", Template("www/josue/$chapiter_number/index.html")),
	Book("livres/juges.html", "Juges", "www/juges/index.html", Template("www/juges/$chapiter_number/index.html")),
	Book("livres/ruth.html", "Ruth", "www/ruth/index.html", Template("www/ruth/$chapiter_number/index.html")),
	Book("livres/1-samuel.html", "1 Samuel", "www/1-samuel/index.html", Template("www/1-samuel/$chapiter_number/index.html")),
	Book("livres/2-samuel.html", "2 Samuel", "www/2-samuel/index.html", Template("www/2-samuel/$chapiter_number/index.html")),
	Book("livres/1-rois.html", "1 Rois", "www/1-rois/index.html", Template("www/1-rois/$chapiter_number/index.html")),
	Book("livres/2-rois.html", "2 Rois", "www/2-rois/index.html", Template("www/2-rois/$chapiter_number/index.html")),
	Book("livres/1-chroniques.html", "1 Chroniques", "www/1-chroniques/index.html", Template("www/1-chroniques/$chapiter_number/index.html")),
	Book("livres/2-chroniques.html", "2 Chroniques", "www/2-chroniques/index.html", Template("www/2-chroniques/$chapiter_number/index.html")),
	Book("livres/esdras.html", "Esdras", "www/esdras/index.html", Template("www/esdras/$chapiter_number/index.html")),
	Book("livres/nehemie.html", "Néhémie", "www/nehemie/index.html", Template("www/nehemie/$chapiter_number/index.html")),
	Book("livres/esther.html", "Esther", "www/esther/index.html", Template("www/esther/$chapiter_number/index.html")),
	Book("livres/job.html", "Job", "www/job/index.html", Template("www/job/$chapiter_number/index.html")),
	Book("livres/psaumes.html", "Psaumes", "www/psaumes/index.html", Template("www/psaumes/$chapiter_number/index.html")),
	Book("livres/proverbes.html", "Proverbes", "www/proverbes/index.html", Template("www/proverbes/$chapiter_number/index.html")),
	Book("livres/ecclesiaste.html", "Ecclésiaste", "www/ecclesiaste/index.html", Template("www/ecclesiaste/$chapiter_number/index.html")),
	Book("livres/cantique.html", "Cantique", "www/cantique/index.html", Template("www/cantique/$chapiter_number/index.html")),
	Book("livres/esaie.html", "Esaïe", "www/esaie/index.html", Template("www/esaie/$chapiter_number/index.html")),
	Book("livres/jeremie.html", "Jérémie", "www/jeremie/index.html", Template("www/jeremie/$chapiter_number/index.html")),
	Book("livres/lamentations.html", "Lamentations", "www/lamentations/index.html", Template("www/lamentations/$chapiter_number/index.html")),
	Book("livres/ezechiel.html", "Ezéchiel", "www/ezechiel/index.html", Template("www/ezechiel/$chapiter_number/index.html")),
	Book("livres/daniel.html", "Daniel", "www/daniel/index.html", Template("www/daniel/$chapiter_number/index.html")),
	Book("livres/osee.html", "Osée", "www/osee/index.html", Template("www/osee/$chapiter_number/index.html")),
	Book("livres/joel.html", "Joël", "www/joel/index.html", Template("www/joel/$chapiter_number/index.html")),
	Book("livres/amos.html", "Amos", "www/amos/index.html", Template("www/amos/$chapiter_number/index.html")),
	Book("livres/abdias.html", "Abdias", "www/abdias/index.html", Template("www/abdias/$chapiter_number/index.html")),
	Book("livres/jonas.html", "Jonas", "www/jonas/index.html", Template("www/jonas/$chapiter_number/index.html")),
	Book("livres/michee.html", "Michée", "www/michee/index.html", Template("www/michee/$chapiter_number/index.html")),
	Book("livres/nahum.html", "Nahum", "www/nahum/index.html", Template("www/nahum/$chapiter_number/index.html")),
	Book("livres/habacuc.html", "Habacuc", "www/habacuc/index.html", Template("www/habacuc/$chapiter_number/index.html")),
	Book("livres/sophonie.html", "Sophonie", "www/sophonie/index.html", Template("www/sophonie/$chapiter_number/index.html")),
	Book("livres/aggee.html", "Aggée", "www/aggee/index.html", Template("www/aggee/$chapiter_number/index.html")),
	Book("livres/zacharie.html", "Zacharie", "www/zacharie/index.html", Template("www/zacharie/$chapiter_number/index.html")),
	Book("livres/malachie.html", "Malachie", "www/malachie/index.html", Template("www/malachie/$chapiter_number/index.html")),
	Book("livres/matthieu.html", "Matthieu", "www/matthieu/index.html", Template("www/matthieu/$chapiter_number/index.html")),
	Book("livres/marc.html", "Marc", "www/marc/index.html", Template("www/marc/$chapiter_number/index.html")),
	Book("livres/luc.html", "Luc", "www/luc/index.html", Template("www/luc/$chapiter_number/index.html")),
	Book("livres/jean.html", "Jean", "www/jean/index.html", Template("www/jean/$chapiter_number/index.html")),
	Book("livres/actes.html", "Actes", "www/actes/index.html", Template("www/actes/$chapiter_number/index.html")),
	Book("livres/romains.html", "Romains", "www/romains/index.html", Template("www/romains/$chapiter_number/index.html")),
	Book("livres/1-corinthiens.html", "1 Corinthiens", "www/1-corinthiens/index.html", Template("www/1-corinthiens/$chapiter_number/index.html")),
	Book("livres/2-corinthiens.html", "2 Corinthiens", "www/2-corinthiens/index.html", Template("www/2-corinthiens/$chapiter_number/index.html")),
	Book("livres/galates.html", "Galates", "www/galates/index.html", Template("www/galates/$chapiter_number/index.html")),
	Book("livres/ephesiens.html", "Ephésiens", "www/ephesiens/index.html", Template("www/ephesiens/$chapiter_number/index.html")),
	Book("livres/philippiens.html", "Philippiens", "www/philippiens/index.html", Template("www/philippiens/$chapiter_number/index.html")),
	Book("livres/colossiens.html", "Colossiens", "www/colossiens/index.html", Template("www/colossiens/$chapiter_number/index.html")),
	Book("livres/1-thessaloniciens.html", "1 Thessaloniciens", "www/1-thessaloniciens/index.html", Template("www/1-thessalonicienss/$chapiter_number/index.html")),
	Book("livres/2-thessaloniciens.html", "2 Thessaloniciens", "www/2-thessaloniciens/index.html", Template("www/2-thessaloniciens/$chapiter_number/index.html")),
	Book("livres/1-timothee.html", "1 Timothée", "www/1-timothee/index.html", Template("www/1-timothee/$chapiter_number/index.html")),
	Book("livres/2-timothee.html", "2 Timothée", "www/2-timothee/index.html", Template("www/2-timothee/$chapiter_number/index.html")),
	Book("livres/tite.html", "Tite", "www/tite/index.html", Template("www/tite/$chapiter_number/index.html")),
	Book("livres/philemon.html", "Philémon", "www/philemon/index.html", Template("www/philemon/$chapiter_number/index.html")),
	Book("livres/hebreux.html", "Hébreux", "www/hebreux/index.html", Template("www/hebreux/$chapiter_number/index.html")),
	Book("livres/jacques.html", "Jacques", "www/jacques/index.html", Template("www/jacques/$chapiter_number/index.html")),
	Book("livres/1-pierre.html", "1 Pierre", "www/1-pierre/index.html", Template("www/1-pierre/$chapiter_number/index.html")),
	Book("livres/2-pierre.html", "2 Pierre", "www/2-pierre/index.html", Template("www/2-pierre/$chapiter_number/index.html")),
	Book("livres/1-jean.html", "1 Jean", "www/1-jean/index.html", Template("www/1-jean/$chapiter_number/index.html")),
	Book("livres/2-jean.html", "2 Jean", "www/2-jean/index.html", Template("www/2-jean/$chapiter_number/index.html")),
	Book("livres/3-jean.html", "3 Jean", "www/3-jean/index.html", Template("www/3-jean/$chapiter_number/index.html")),
	Book("livres/jude.html", "Jude", "www/jude/index.html", Template("www/jude/$chapiter_number/index.html")),
	Book("livres/apocalypse.html", "Apocalypse", "www/apocalypse/index.html", Template("www/apocalypse/$chapiter_number/index.html"))
]

for book in books:
	chapiters_table_generator.generate(book.path, book.name, book.table_output_path)
	chapiter_generator.generate(book.path, book.chapiter_output_path_template)
