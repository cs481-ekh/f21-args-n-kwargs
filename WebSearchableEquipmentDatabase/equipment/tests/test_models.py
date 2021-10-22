from django.test import TestCase
from equipment.models import Equipment, Category, Location


class EquipmentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Equipment.objects.create(name="Rotary Disc cutter",
                                 model="Model 360",
                                 manufacturer="South Bay",
                                 year=2016,
                                 pi="Steve Jobs",
                                 contact="Steve Jobs",
                                 room="CS1001",
                                 lab="BSCMC",
                                 description="Cutting 3 mm",
                                 url="www.google.com",
                                 permission="Student")

    def test_equipment_name(self):
        equip = Equipment.objects.get(id=1)
        name_label = equip.name
        self.assertEqual(name_label, "Rotary Disc cutter")

    def test_equipment_model(self):
        equip = Equipment.objects.get(id=1)
        model_label = equip.model
        self.assertEqual(model_label, "Model 360")

    def test_equipment_year(self):
        equip = Equipment.objects.get(id=1)
        year_label = equip.year
        self.assertEqual(year_label, 2016)

    def test_equipment_pi(self):
        equip = Equipment.objects.get(id=1)
        pi_label = equip.pi
        self.assertEqual(pi_label, "Steve Jobs")

    def test_equipment_contact(self):
        equip = Equipment.objects.get(id=1)
        contact_label = equip.contact
        self.assertEqual(contact_label, "Steve Jobs")

    def test_equipment_room(self):
        equip = Equipment.objects.get(id=1)
        room_label = equip.room
        self.assertEqual(room_label, "CS1001")

    def test_equipment_lab(self):
        equip = Equipment.objects.get(id=1)
        lab_label = equip.lab
        self.assertEqual(lab_label, "BSCMC")

    def test_equipment_description(self):
        equip = Equipment.objects.get(id=1)
        description_label = equip.description
        self.assertEqual(description_label, "Cutting 3 mm")

    def test_equipment_url(self):
        equip = Equipment.objects.get(id=1)
        url_label = equip.url
        self.assertEqual(url_label, "www.google.com")

    def test_equipment_to_string(self):
        equip = Equipment.objects.get(id=1)
        self.assertEqual(equip.__str__(), "Rotary Disc cutter, Model 360")

    def test_equipment_permission(self):
        equip = Equipment.objects.get(id=1)
        permission_label = equip.permission
        self.assertEqual(permission_label, "Student")


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Equipment.objects.create(name="Rotary Disc cutter",
                                 model="Model 360",
                                 manufacturer="South Bay",
                                 year=2016,
                                 pi="Steve Jobs",
                                 contact="Steve Jobs",
                                 room="CS1001",
                                 lab="BSCMC",
                                 description="Cutting 3 mm",
                                 url="www.google.com",
                                 permission="Student")

    def test_category_equipment(self):
        cat = Category.objects.create(label="Processing", equipment=Equipment.objects.get(id=1))
        self.assertEqual("Rotary Disc cutter", cat.equipment.name)

    def test_category_category(self):
        cat = Category.objects.create(label="Processing", equipment=Equipment.objects.get(id=1))
        self.assertEqual("Processing", cat.label)


class LocationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Equipment.objects.create(name="Rotary Disc cutter",
                                 model="Model 360",
                                 manufacturer="South Bay",
                                 year=2016,
                                 pi="Steve Jobs",
                                 contact="Steve Jobs",
                                 room="CS1001",
                                 lab="BSCMC",
                                 description="Cutting 3 mm",
                                 url="www.google.com",
                                 permission="Student")

    def test_location_equipment_instance(self):
        location = Location.objects.create(location_label="BSCMC", equipment=Equipment.objects.get(id=1))
        self.assertEqual("Rotary Disc cutter", location.equipment.name)

    def test_category_category(self):
        location = Location.objects.create(location_label="BSCMC", equipment=Equipment.objects.get(id=1))
        self.assertEqual("BSCMC", location.location_label)
