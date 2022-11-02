# mypy: allow-untyped-defs

from recipe_scrapers.tasteline import Tasteline
from tests import ScraperTest


class TestTastelineScraper(ScraperTest):

    scraper_class = Tasteline

    def test_host(self):
        self.assertEqual("tasteline.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Mia Troberg", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Boeuf Bourguignon", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Burgundisk gryta", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual("https://eu-central-1.linodeobjects.com/tasteline/2021/10/Boeuf-Bourguignon-foto-Nurlan-Emir-Tasteline.jpg", self.harvester_class.image())

    def test_ingredients(self):
        self.assertEqual(
            [
                "600 g högrev",
                "1 msk mat- och baksmör",
                "100 g morot",
                "1 st gul lök",
                "0.5 tsk salt",
                "1 krm svartpeppar",
                "1 msk vetemjöl",
                "2.5 dl rött vin",
                "2 dl köttbuljong",
                "1 msk tomatpuré",
                "0.5 tsk torkad timjan",
                "1 st lagerblad",
                "1 vitlök",
                "8 st steklök",
                "1 msk mat- och baksmör",
                "0.5 dl vatten",
                "200 g färska champinjoner",
                "140 g bacon",
            ],
            self.harvester_class.ingredients(),
        )
    def test_instructions(self):
        self.assertEqual("Skär köttet i 2–3 cm stora tärningar. Bryn det i smör i omgångar i en stekpanna och lägg sedan över köttet i en rymlig gryta.\nSkär morötterna i skivor, inte alltför tunna, och skiva också löken. Fräs dem lätt och lägg över i grytan. Salta och peppra.\nPudra över mjölet och rör om under uppvärmning så att mjölet fördelar sig jämnt.\nHäll på vin och buljong så att det täcker. Tillsätt tomatpuré, timjan och lagerblad. Pressa i vitlök och koka upp grytan under omrörning.\nLåt grytan småputtra tills köttet är mört, ca 1½ tim.\nSkala under tiden smålökarna. Fräs dem i smör, häll på en skvätt vatten och koka dem mjuka.\nDela champinjonerna om de är stora och bryn dem. Klipp baconet i strimlor och bryn det lätt.\nLägg i smålökar, svamp och bacon och sjud några minuter. Smaka av om det behövs mer salt och peppar. Servera med ex. pressad potatis, ris eller pastafjärilar.", self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(3.99, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Frankrike", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual("En lättlagad och omtyckt fransk klassiker som sköter sig själv på spisen. Kallas även för Burgundisk köttgryta. En välsmakande gryta som värmer en ruggig höstkväll med fina smaker från rött vin och timjan.", self.harvester_class.description())
